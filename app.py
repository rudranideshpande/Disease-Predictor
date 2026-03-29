import streamlit as st
import hashlib
from knowledge_base import KNOWLEDGE_BASE
import engine

def generate_key(prompt: str) -> str:
    """Generate a stable key using hashlib for streamlit widgets."""
    return hashlib.md5(prompt.encode('utf-8')).hexdigest()

def reset_state():
    for key in ['started', 'initial_symptoms', 'confirmed_symptoms', 'denied_symptoms', 'candidates', 'questions_asked']:
        if key in st.session_state:
            del st.session_state[key]

# Setup session state
if 'started' not in st.session_state:
    st.session_state.started = False
if 'confirmed_symptoms' not in st.session_state:
    st.session_state.confirmed_symptoms = []
if 'denied_symptoms' not in st.session_state:
    st.session_state.denied_symptoms = []
if 'candidates' not in st.session_state:
    st.session_state.candidates = {}
if 'questions_asked' not in st.session_state:
    st.session_state.questions_asked = 0

MAX_QUESTIONS = 7

st.set_page_config(page_title="Symptom Checker", page_icon="🩺")

st.title("🩺 Symptom Checker")

# Educational Disclaimer
st.warning("⚠️ **Educational Disclaimer:** This application is for educational purposes only. It does not provide medical advice. Consult a healthcare professional for actual medical concerns.")

if not st.session_state.started:
    st.header("Step 1: Your Symptoms")
    st.write("Select the symptoms you are currently experiencing.")
    
    all_symptoms = engine.extract_all_symptoms()
    selected_symptoms = st.multiselect("Select Symptoms:", all_symptoms)
    
    if st.button("Start Diagnosis"):
        if not selected_symptoms:
            st.error("Please select at least one symptom to begin.")
        else:
            st.session_state.started = True
            st.session_state.initial_symptoms = selected_symptoms
            st.session_state.confirmed_symptoms = selected_symptoms.copy()
            
            # Get Candidates
            st.session_state.candidates = engine.forward_chaining(selected_symptoms)
            st.rerun()
else:
    # We are in the diagnostic process
    st.header("Step 2: Additional Questions")
    
    # Check if goal is reached
    goal_reached, diagnosis = engine.is_goal_reached(st.session_state.candidates)
    
    if goal_reached:
        st.success("Diagnosis Complete")
        st.subheader(f"Likely Diagnosis: {diagnosis}")
        
        info = KNOWLEDGE_BASE[diagnosis]
        st.write(f"**Next Steps:** {info['Next Steps']}")
        st.write(f"**Precautions:** {', '.join(info['Precautions'])}")
        
        if st.button("Start New Diagnosis", key="restart_goal"):
            reset_state()
            st.rerun()
            
    elif st.session_state.questions_asked >= MAX_QUESTIONS:
        st.info("We have gathered enough information.")
        
        if st.session_state.candidates:
            top_candidate = list(st.session_state.candidates.keys())[0]
            st.subheader(f"Best Guess: {top_candidate}")
            
            info = KNOWLEDGE_BASE[top_candidate]
            st.write(f"**Next Steps:** {info['Next Steps']}")
            st.write(f"**Precautions:** {', '.join(info['Precautions'])}")
        
        if st.button("Start New Diagnosis", key="restart_max_q"):
            reset_state()
            st.rerun()
            
    else:
        # Ask next question
        next_q = engine.backward_chaining_next_question(
            st.session_state.candidates, 
            st.session_state.confirmed_symptoms, 
            st.session_state.denied_symptoms
        )
        
        if next_q:
            disease = next_q['disease']
            symptom = next_q['symptom']
            
            question = f"Do you also have this symptom: **{symptom}**?"
            key = generate_key(question)
            
            st.write(f"### {question}")
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("Yes", key=key+"_yes"):
                    st.session_state.questions_asked += 1
                    st.session_state.confirmed_symptoms.append(symptom)
                    st.session_state.candidates = engine.update_confidence(st.session_state.candidates, st.session_state.confirmed_symptoms)
                    st.rerun()
                    
            with col2:
                if st.button("No", key=key+"_no"):
                    st.session_state.questions_asked += 1
                    st.session_state.denied_symptoms.append(symptom)
                    st.rerun()
        else:
            st.info("We have gathered enough information.")
            
            if st.session_state.candidates:
                top_candidate = list(st.session_state.candidates.keys())[0]
                st.subheader(f"Best Guess: {top_candidate}")
                
                info = KNOWLEDGE_BASE[top_candidate]
                st.write(f"**Next Steps:** {info['Next Steps']}")
                st.write(f"**Precautions:** {', '.join(info['Precautions'])}")
            
            if st.button("Start New Diagnosis", key="restart_failed"):
                reset_state()
                st.rerun()
