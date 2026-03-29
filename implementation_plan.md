# Medical Expert System Implementation Plan

This implementation plan outlines the creation of an interactive Medical Expert System built using Python and Streamlit. The system will serve as an educational simulation demonstrating key Artificial Intelligence concepts, specifically focusing on diagnostic problem-solving.

## User Review Required

> [!CAUTION]
> This application is strictly an educational simulation. It does **not** provide actual medical advice. A clear disclaimer will be permanently displayed on the UI.

> [!IMPORTANT]
> The target confidence threshold is set to 80%. Once an illness reaches this threshold, the agent achieves its "Goal", concludes the diagnosis, and displays its reasoning path.

## Proposed Architecture

The application will be divided into modular components for clarity and maintainability.

### 1. Knowledge Representation Layer

We will implement a structured Knowledge Base (KB) to store disease information.

#### [NEW] [knowledge_base.py](file:///c:/Users/user/Desktop/ai%20health/knowledge_base.py)
This file will contain the knowledge base as a structured Python dictionary. 
- Each entity (Disease) will be an object detailing its symptoms and remedies.
- **Attributes per Disease**:
  - `Core`: Highly indicative primary symptoms.
  - `Secondary`: Supporting or less specific symptoms.
  - `Next Steps`: Recommended actions if diagnosed.
  - `Precautions`: Preventive measures.

### 2. Inference Engine

This component will act as our Goal-Based Agent, implementing both Forward and Backward chaining.

#### [NEW] [engine.py](file:///c:/Users/user/Desktop/ai%20health/engine.py)
This module will house the core logic:
- **State-Space Search**: The search path will be logically ordered, evaluating `Core` symptoms before `Secondary` symptoms.
- **Forward Chaining**: A data-driven function that takes the user's initial symptoms (Percepts) and filters the KB to identify and rank candidate diseases.
- **Backward Chaining**: A hypothesis-driven function that focuses on the top-ranked candidates. It will identify "missing" evidence (unconfirmed symptoms) and trigger targeted Yes/No questions.
- **Goal Checking**: Continuously evaluates if the confidence score of the top candidate meets the 80% threshold.

### 3. User Interface Layer

We will leverage Streamlit to create an interactive web interface.

#### [NEW] [app.py](file:///c:/Users/user/Desktop/ai%20health/app.py)
The main entry point for the Streamlit application.
- **Initial State**: Presents a multi-select box for the user to input initial perceived symptoms.
- **Interactive Questioning**: Uses the inference engine to dynamically render Yes/No questions based on Backward Chaining. Will utilize Python's `hashlib` to generate stable Streamlit widget keys.
- **Explanation Module**: Once a diagnosis is reached (or unresolvable), this module will trace and display the path the AI took—showing the initial matches, the questions asked, and how the confidence score evolved, culminating in the final recommendation.

#### [NEW] [requirements.txt](file:///c:/Users/user/Desktop/ai%20health/requirements.txt)
Dependencies required to run the application (e.g., `streamlit`).

## Open Questions

> [!NOTE]
> 1. **Knowledge Base Scope**: Do you have a specific list of diseases and symptoms you want included in the KB, or should I populate it with a standard set of common illnesses (e.g., Common Cold, Flu, COVID-19, Strep Throat)?
> 2. **Scoring Mechanism**: By default, I will assign higher weights to `Core` symptoms and lower to `Secondary` symptoms to calculate confidence. Does this align with your expectations for the Goal-Based Agent?

## Verification Plan

### Automated/Code Verification
- Ensure the `hashlib` implementation maintains session state stability during Streamlit re-renders.
- Verify module imports and dictionary accesses work correctly.

### Manual Verification
- Run the app via `streamlit run app.py` and interact with it.
- Select a specific set of initial symptoms.
- Observe whether the Forward Chaining identifies the correct candidate pool.
- Answer the Backward Chaining Yes/No questions and verify that the confidence score updates correctly and stops at the 80% threshold.
- Check the Explanation Module to ensure it accurately traces the decision path.
