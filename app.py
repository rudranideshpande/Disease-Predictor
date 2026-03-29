import streamlit as st
import hashlib
from knowledge_base import KNOWLEDGE_BASE
import engine

# ---------- Helper Functions ----------

def generate_key(text):
    """Create a unique key for buttons/questions"""
    return hashlib.md5(text.encode()).hexdigest()


def reset_app():
    """Reset everything to start fresh"""
    keys = [
        'started',
        'initial_symptoms',
        'confirmed_symptoms',
        'denied_symptoms',
        'candidates',
        'questions_asked'
    ]
    for k in keys:
        if k in st.session_state:
            del st.session_state[k]


# ---------- Initialize State ----------

def init_state():
    defaults = {
        'started': False,
        'confirmed_symptoms': [],
        'denied_symptoms': [],
        'candidates': {},
        'questions_asked': 0
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_state()
MAX_QUESTIONS = 7

# ---------- UI Setup ----------
st.set_page_config(page_title="Symptom Checker")
st.title(" Symptom Checker")

st.warning(
    "⚠️ This tool is only for learning purposes. "
    "It is NOT a medical diagnosis. Always consult a doctor."
)


# ---------- Step 1: Select Symptoms ----------
if not st.session_state.started:
    st.header("Select Your Symptoms")
    st.write("Choose what you're currently experiencing:")

    symptoms_list = engine.extract_all_symptoms()
    selected = st.multiselect("Symptoms:", symptoms_list)

    if st.button("Start"):
        if len(selected) == 0:
            st.error("Please select at least one symptom.")
        else:
            st.session_state.started = True
            st.session_state.initial_symptoms = selected
            st.session_state.confirmed_symptoms = selected.copy()

            # Find possible diseases
            st.session_state.candidates = engine.forward_chaining(selected)
            st.rerun()


# ---------- Step 2: Ask Questions ----------
else:
    st.header("Answer a Few Questions")

    goal_done, result = engine.is_goal_reached(st.session_state.candidates)

    # ---------- Case 1: Diagnosis Found ----------
    if goal_done:
        st.success("Diagnosis Completed")
        st.subheader(f"Most Likely: {result}")

        details = KNOWLEDGE_BASE[result]
        st.write("**What you can do next:**")
        st.write(details['Next Steps'])

        st.write("**Precautions:**")
        st.write(", ".join(details['Precautions']))

        if st.button("Restart"):
            reset_app()
            st.rerun()

    # ---------- Case 2: Max Questions Reached ----------
    elif st.session_state.questions_asked >= MAX_QUESTIONS:
        st.info("Enough information collected.")

        if st.session_state.candidates:
            best = list(st.session_state.candidates.keys())[0]
            st.subheader(f"Best Guess: {best}")

            details = KNOWLEDGE_BASE[best]
            st.write(details['Next Steps'])
            st.write(", ".join(details['Precautions']))

        if st.button("Restart"):
            reset_app()
            st.rerun()

    # ---------- Case 3: Ask Next Question ----------
    else:
        next_question = engine.backward_chaining_next_question(
            st.session_state.candidates,
            st.session_state.confirmed_symptoms,
            st.session_state.denied_symptoms
        )

        if next_question:
            symptom = next_question['symptom']

            question_text = f"Do you have: {symptom}?"
            st.write(f"### {question_text}")

            key = generate_key(question_text)
            col1, col2 = st.columns(2)

            # YES button
            with col1:
                if st.button("Yes", key=key + "_yes"):
                    st.session_state.questions_asked += 1
                    st.session_state.confirmed_symptoms.append(symptom)

                    st.session_state.candidates = engine.update_confidence(
                        st.session_state.candidates,
                        st.session_state.confirmed_symptoms
                    )
                    st.rerun()

            # NO button
            with col2:
                if st.button("No", key=key + "_no"):
                    st.session_state.questions_asked += 1
                    st.session_state.denied_symptoms.append(symptom)
                    st.rerun()

        else:
            st.info("No more questions needed.")

            if st.session_state.candidates:
                best = list(st.session_state.candidates.keys())[0]
                st.subheader(f"Best Guess: {best}")

                details = KNOWLEDGE_BASE[best]
                st.write(details['Next Steps'])
                st.write(", ".join(details['Precautions']))

            if st.button("Restart"):
                reset_app()
                st.rerun()
