# engine.py
# Inference Engine for the Medical Expert System

from knowledge_base import KNOWLEDGE_BASE

# (Forced file change to trigger Streamlit's cache to reload the new Knowledge Base)

# Constants for our Goal-Based Agent
CONFIDENCE_THRESHOLD = 0.80
CORE_WEIGHT = 2.0
SECONDARY_WEIGHT = 1.0

def calculate_max_score(disease_name):
    """Calculates the maximum possible score for a disease to compute confidence."""
    disease = KNOWLEDGE_BASE[disease_name]
    return (len(disease["Core"]) * CORE_WEIGHT) + (len(disease["Secondary"]) * SECONDARY_WEIGHT)

def extract_all_symptoms():
    """Extracts all unique symptoms from the knowledge base for the initial UI."""
    symptoms = set()
    for disease in KNOWLEDGE_BASE.values():
        symptoms.update(disease["Core"])
        symptoms.update(disease["Secondary"])
    return sorted(list(symptoms))

def forward_chaining(initial_symptoms):
    """
    Data-driven step: Identifies diseases that match at least one initial symptom.
    Returns a sorted dict of candidates based on initial confidence scores.
    """
    candidates = {}
    
    for disease_name, info in KNOWLEDGE_BASE.items():
        score = 0.0
        matched_symptoms = []
        
        # Check core symptoms
        for sym in info["Core"]:
            if sym in initial_symptoms:
                score += CORE_WEIGHT
                matched_symptoms.append(sym)
                
        # Check secondary symptoms
        for sym in info["Secondary"]:
            if sym in initial_symptoms:
                score += SECONDARY_WEIGHT
                matched_symptoms.append(sym)
                
        if score > 0:
            max_score = calculate_max_score(disease_name)
            confidence = score / max_score
            candidates[disease_name] = {
                "score": score,
                "confidence": confidence,
                "matches": matched_symptoms
            }
            
    # Sort candidates by descending confidence
    ranked_candidates = sorted(candidates.items(), key=lambda item: item[1]["confidence"], reverse=True)
    return {k: v for k, v in ranked_candidates}

def backward_chaining_next_question(candidates, confirmed_symptoms, denied_symptoms):
    """
    Hypothesis-driven step: For the top candidate(s), find the next missing piece
    of evidence (symptom) to ask the user to confirm or deny.
    Implements State-Space Search: Prioritizes Core over Secondary symptoms.
    """
    for disease_name in candidates.keys():
        info = KNOWLEDGE_BASE[disease_name]
        
        # Search Core symptoms first (State-Space Search ordering)
        for sym in info["Core"]:
            if sym not in confirmed_symptoms and sym not in denied_symptoms:
                return {"disease": disease_name, "symptom": sym, "type": "Core"}
                
        # Then Search Secondary symptoms
        for sym in info["Secondary"]:
            if sym not in confirmed_symptoms and sym not in denied_symptoms:
                return {"disease": disease_name, "symptom": sym, "type": "Secondary"}
                
    # If no more questions for any candidate
    return None

def update_confidence(candidates, confirmed_symptoms):
    """Recalculates confidence for all candidates based on new evidence."""
    for disease_name in candidates.keys():
        info = KNOWLEDGE_BASE[disease_name]
        score = 0.0
        matches = []
        
        for sym in info["Core"]:
            if sym in confirmed_symptoms:
                score += CORE_WEIGHT
                matches.append(sym)
                
        for sym in info["Secondary"]:
            if sym in confirmed_symptoms:
                score += SECONDARY_WEIGHT
                matches.append(sym)
                
        max_score = calculate_max_score(disease_name)
        candidates[disease_name]["score"] = score
        candidates[disease_name]["confidence"] = score / max_score
        candidates[disease_name]["matches"] = matches
        
    # Re-rank
    ranked_candidates = sorted(candidates.items(), key=lambda item: item[1]["confidence"], reverse=True)
    return {k: v for k, v in ranked_candidates}

def is_goal_reached(candidates):
    """Checks if any candidate has reached the target confidence threshold."""
    if not candidates:
        return False, None
        
    top_candidate_name = list(candidates.keys())[0]
    top_candidate_state = candidates[top_candidate_name]
    
    if top_candidate_state["confidence"] >= CONFIDENCE_THRESHOLD:
        return True, top_candidate_name
        
    return False, None
