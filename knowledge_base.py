# knowledge_base.py

# Knowledge Base representing diseases and their associated attributes.
# Core symptoms have higher weight in the diagnosis process.
# Secondary symptoms help refine the diagnosis but are less critical.

KNOWLEDGE_BASE = {
    "Common Cold": {
        "Core": ["Runny Nose", "Sore Throat", "Congestion"],
        "Secondary": ["Sneezing", "Mild Cough", "Mild Fatigue"],
        "Next Steps": "Rest, stay hydrated, and take over-the-counter cold medications if needed.",
        "Precautions": ["Wash hands frequently", "Avoid close contact with sick people"]
    },
    "COVID-19": {
        "Core": ["Loss of Taste or Smell", "Fever", "Continuous Cough"],
        "Secondary": ["Shortness of Breath", "Extreme Fatigue", "Sore Throat", "Muscle Aches"],
        "Next Steps": "Isolate immediately to prevent spreading. Take a PCR or rapid antigen test. Contact a healthcare provider if breathing becomes difficult.",
        "Precautions": ["Wear a mask in crowded spaces", "Maintain social distancing", "Get vaccinated and boosted"]
    },
    "Pneumonia": {
        "Core": ["High Fever", "Deep Cough", "Shortness of breath"],
        "Secondary": ["Chest pain", "Phlegm", "Chills", "Fatigue"],
        "Next Steps": "Seek immediate medical evaluation; may require antibiotics or X-ray.",
        "Precautions": ["Avoid smoke", "Use a humidifier", "Rest strictly."]
    },
    "Bronchitis": {
        "Core": ["Persistent Cough", "Mucus Production", "Chest Discomfort"],
        "Secondary": ["Fatigue", "Slight Fever", "Shortness of breath"],
        "Next Steps": "Hydrate and use a humidifier; see a doctor if cough lasts >3 weeks.",
        "Precautions": ["Avoid lung irritants", "Wash hands to prevent spread."]
    },
    "Asthma": {
        "Core": ["Wheezing", "Chest Tightness", "Shortness of breath"],
        "Secondary": ["Coughing at night", "Rapid breathing", "Anxiety"],
        "Next Steps": "Use rescue inhaler; follow your specialized asthma action plan.",
        "Precautions": ["Identify triggers like dust/pollen", "Keep inhaler nearby."]
    },
    "Sinusitis": {
        "Core": ["Facial Pain", "Nasal Congestion", "Thick Nasal Discharge"],
        "Secondary": ["Headache", "Sore Throat", "Cough", "Ear Pressure"],
        "Next Steps": "Saline nasal rinse and steam inhalation.",
        "Precautions": ["Avoid sudden temperature changes", "Stay hydrated."]
    },
    "Strep Throat": {
        "Core": ["Severe Sore Throat", "Painful Swallowing", "Swollen Lymph Nodes"],
        "Secondary": ["Fever", "Red spots on roof of mouth", "Headache"],
        "Next Steps": "Consult a professional for a throat culture/strep test.",
        "Precautions": ["Do not share utensils", "Replace toothbrush after 24hrs of antibiotics."]
    },

    # --- Digestive & Gastro ---
    "GERD (Acid Reflux)": {
        "Core": ["Heartburn", "Regurgitation", "Chest Pain"],
        "Secondary": ["Difficulty swallowing", "Chronic cough", "Sensation of a lump in throat"],
        "Next Steps": "Avoid spicy foods; stay upright for 3 hours after eating.",
        "Precautions": ["Eat smaller meals", "Quit smoking if applicable."]
    },
    "Gastroenteritis (Stomach Flu)": {
        "Core": ["Watery Diarrhea", "Abdominal Cramps", "Nausea"],
        "Secondary": ["Vomiting", "Occasional muscle aches", "Low-grade fever"],
        "Next Steps": "Focus on electrolyte replacement and clear fluids.",
        "Precautions": ["Disinfect shared surfaces", "Frequent hand washing."]
    },
    "Food Poisoning": {
        "Core": ["Vomiting", "Frequent Diarrhea", "Stomach Pain"],
        "Secondary": ["Fever", "Weakness", "Loss of appetite"],
        "Next Steps": "Rest and rehydrate; seek care if blood appears in stool.",
        "Precautions": ["Cook meat thoroughly", "Avoid unpasteurized dairy."]
    },
    "Constipation": {
        "Core": ["Infrequent Bowel Movements", "Hard Stools", "Straining"],
        "Secondary": ["Abdominal bloating", "Sensation of incomplete evacuation"],
        "Next Steps": "Increase fiber intake (fruits/veg) and water consumption.",
        "Precautions": ["Maintain a regular exercise routine", "Don't ignore the urge."]
    },
    "IBS (Irritable Bowel Syndrome)": {
        "Core": ["Abdominal Pain", "Bloating", "Changed Bowel Habits"],
        "Secondary": ["Gas", "Mucus in stool", "Feeling of incomplete evacuation"],
        "Next Steps": "Manage stress and track trigger foods in a diary.",
        "Precautions": ["Limit caffeine and high-gas foods", "Eat at regular times."]
    },

    # --- Neurological & Head ---
    "Migraine": {
        "Core": ["Throbbing Headache", "Nausea", "Sensitivity to Light"],
        "Secondary": ["Sensitivity to sound", "Blurred vision", "Aura/flashing lights"],
        "Next Steps": "Rest in a dark, quiet room; apply a cold compress.",
        "Precautions": ["Maintain a sleep schedule", "Track triggers like aged cheese/chocolate."]
    },
    "Tension Headache": {
        "Core": ["Dull Head Pain", "Tightness across forehead", "Neck tenderness"],
        "Secondary": ["Scalp tenderness", "Muscle tension in shoulders"],
        "Next Steps": "Improve posture and practice stress-reduction techniques.",
        "Precautions": ["Take breaks from screens", "Stay hydrated."]
    },
    "Vertigo": {
        "Core": ["Spinning Sensation", "Loss of Balance", "Dizziness"],
        "Secondary": ["Nausea", "Ringing in ears", "Nystagmus (jerking eye movements)"],
        "Next Steps": "Avoid sudden head movements; consult for Epley maneuver.",
        "Precautions": ["Use bright lighting at home", "Get up slowly from bed."]
    },
    "Concussion": {
        "Core": ["Headache", "Confusion", "Dizziness"],
        "Secondary": ["Nausea", "Slurred speech", "Fatigue", "Sensitivity to noise"],
        "Next Steps": "Immediate physical/mental rest; seek care for loss of consciousness.",
        "Precautions": ["Avoid screens", "Do not drive until cleared."]
    },

    # --- Skin & Allergy ---
    "Eczema": {
        "Core": ["Dry Skin", "Severe Itching", "Red to brownish-gray patches"],
        "Secondary": ["Small raised bumps", "Thickened or scaly skin"],
        "Next Steps": "Apply fragrance-free moisturizers twice daily.",
        "Precautions": ["Avoid harsh soaps", "Wear soft, breathable fabrics."]
    },
    "Allergic Rhinitis (Hay Fever)": {
        "Core": ["Sneezing", "Runny Nose", "Itchy Eyes"],
        "Secondary": ["Watery eyes", "Cough", "Itchy roof of mouth"],
        "Next Steps": "Identify allergens; use saline spray or antihistamines.",
        "Precautions": ["Keep windows closed during high pollen", "Shower after being outside."]
    },
    "Urticaria (Hives)": {
        "Core": ["Raised Red Welts", "Itching", "Burning/Stinging"],
        "Secondary": ["Swelling of lips or eyelids", "Welts that change shape"],
        "Next Steps": "Apply cool compresses; avoid known triggers like specific foods.",
        "Precautions": ["Wear loose clothing", "Keep a food/medication diary."]
    },
    "Contact Dermatitis": {
        "Core": ["Red Rash", "Itching", "Dry/Cracked Skin"],
        "Secondary": ["Blisters", "Burning sensation", "Swelling"],
        "Next Steps": "Identify the substance (soap/jewelry/plants) and avoid it.",
        "Precautions": ["Use protective gloves", "Apply barrier creams."]
    },

    # --- Infections & Systemic ---
    "UTI (Urinary Tract Infection)": {
        "Core": ["Painful Urination", "Frequent Urge to Urinate", "Cloudy Urine"],
        "Secondary": ["Pelvic pain", "Strong-smelling urine", "Blood in urine"],
        "Next Steps": "Drink plenty of water; consult a professional for antibiotics.",
        "Precautions": ["Urinate after intercourse", "Wipe front to back."]
    },
    "Influenza (Flu)": {
        "Core": ["High Fever", "Body Aches", "Extreme Fatigue"],
        "Secondary": ["Dry Cough", "Headache", "Chills", "Sore Throat"],
        "Next Steps": "Bed rest and fluids; monitor for breathing difficulties.",
        "Precautions": ["Annual vaccination", "Stay home until fever-free for 24h."]
    },
    "Dengue Fever": {
        "Core": ["High Fever", "Severe Bone/Joint Pain", "Pain behind eyes"],
        "Secondary": ["Rash", "Nausea", "Mild bleeding (nose/gums)"],
        "Next Steps": "Hydrate and rest; seek care for severe abdominal pain.",
        "Precautions": ["Use mosquito repellent", "Eliminate stagnant water near home."]
    },
    "Chickenpox": {
        "Core": ["Itchy Red Blisters", "Fever", "Loss of appetite"],
        "Secondary": ["Headache", "Tiredness", "General feeling of being unwell"],
        "Next Steps": "Avoid scratching; use calamine lotion for itching.",
        "Precautions": ["Isolate from non-immune people", "Trim fingernails short."]
    },
    "Conjunctivitis (Pink Eye)": {
        "Core": ["Redness in Eye", "Itchiness", "Eye Discharge"],
        "Secondary": ["Tearing", "Crusting of eyelids", "Sensitivity to light"],
        "Next Steps": "Avoid contact lenses; wash eyes with warm water.",
        "Precautions": ["Don't share towels", "Wash hands frequently."]
    },

    # --- Musculoskeletal ---
    "Osteoarthritis": {
        "Core": ["Joint Pain", "Stiffness in the morning", "Loss of flexibility"],
        "Secondary": ["Grating sensation", "Bone spurs", "Swelling near joints"],
        "Next Steps": "Engage in low-impact exercise (swimming/cycling).",
        "Precautions": ["Maintain a healthy weight", "Use heat/cold therapy."]
    },
    "Muscle Strain": {
        "Core": ["Sudden Pain", "Soreness", "Limited Range of Motion"],
        "Secondary": ["Swelling", "Bruising", "Muscle spasms"],
        "Next Steps": "Follow R.I.C.E (Rest, Ice, Compression, Elevation).",
        "Precautions": ["Warm up before exercise", "Use proper lifting techniques."]
    },
    "Plantar Fasciitis": {
        "Core": ["Stabbing Heel Pain", "Pain after waking up", "Pain after exercise"],
        "Secondary": ["Tight calf muscles", "Swelling in heel area"],
        "Next Steps": "Stretch the arches and calves; wear supportive shoes.",
        "Precautions": ["Avoid walking barefoot", "Replace worn-out sneakers."]
    },

    # --- Miscellaneous ---
    "Anemia": {
        "Core": ["Extreme Fatigue", "Pale Skin", "Weakness"],
        "Secondary": ["Cold hands/feet", "Brittle nails", "Chest pain", "Fast heartbeat"],
        "Next Steps": "Blood test for iron levels; increase intake of leafy greens.",
        "Precautions": ["Avoid tea/coffee with meals (inhibits iron absorption).", "Monitor vitamin C intake."]
    },
    "Hypoglycemia": {
        "Core": ["Shakiness", "Sweating", "Hunger"],
        "Secondary": ["Dizziness", "Irritability", "Fast heartbeat", "Confusion"],
        "Next Steps": "Consume 15g of fast-acting sugar (juice/honey).",
        "Precautions": ["Carry glucose tablets", "Eat regular, balanced meals."]
    },
    "Dehydration": {
        "Core": ["Extreme Thirst", "Dark Colored Urine", "Dizziness"],
        "Secondary": ["Dry mouth", "Fatigue", "Confusion"],
        "Next Steps": "Drink water or oral rehydration solutions slowly.",
        "Precautions": ["Drink more in hot weather", "Monitor fluid loss during exercise."]
    },
    "Heat Exhaustion": {
        "Core": ["Heavy Sweating", "Rapid Pulse", "Faintness"],
        "Secondary": ["Nausea", "Muscle cramps", "Cool, moist skin"],
        "Next Steps": "Move to a cool area and drink cool water.",
        "Precautions": ["Wear lightweight clothing", "Stay hydrated in the sun."]
    },
    "Insomnia": {
        "Core": ["Difficulty falling asleep", "Waking up during night", "Not feeling well-rested"],
        "Secondary": ["Daytime sleepiness", "Irritability", "Difficulty concentrating"],
        "Next Steps": "Establish a consistent sleep schedule and routine.",
        "Precautions": ["Avoid caffeine late in the day", "Limit screen time before bed."]
    },
    "Gout": {
        "Core": ["Intense Joint Pain", "Redness/Swelling (often big toe)", "Heat in joint"],
        "Secondary": ["Limited range of motion", "Lingering discomfort"],
        "Next Steps": "Drink plenty of water; avoid high-purine foods (red meat).",
        "Precautions": ["Limit alcohol consumption", "Maintain healthy weight."]
    },
    "Hypothyroidism": {
        "Core": ["Fatigue", "Weight Gain", "Cold Intolerance"],
        "Secondary": ["Dry skin", "Thinning hair", "Slow heart rate", "Constipation"],
        "Next Steps": "Blood test for TSH levels; consult for hormone therapy.",
        "Precautions": ["Ensure adequate iodine intake", "Monitor energy levels."]
    },
    "Iron Deficiency": {
        "Core": ["Tiredness", "Shortness of breath", "Pale tongue"],
        "Secondary": ["Headaches", "Heart palpitations", "Strange cravings (ice/dirt)"],
        "Next Steps": "Increase iron-rich foods (red meat, beans, fortified cereals).",
        "Precautions": ["Combine iron with Vitamin C for better absorption."]
    },
    "Laryngitis": {
        "Core": ["Hoarseness", "Weak Voice", "Loss of Voice"],
        "Secondary": ["Tickling in throat", "Dry throat", "Dry cough"],
        "Next Steps": "Rest your voice; stay hydrated and use throat lozenges.",
        "Precautions": ["Avoid whispering (strains vocal cords)", "Avoid irritants like smoke."]
    },
    "Mononucleosis (Mono)": {
        "Core": ["Extreme Fatigue", "Fever", "Severe Sore Throat"],
        "Secondary": ["Swollen lymph nodes", "Swollen spleen", "Headache"],
        "Next Steps": "Primary treatment is rest and hydration; avoid contact sports.",
        "Precautions": ["Don't share drinks/kisses", "Avoid heavy lifting (spleen risk)."]
    },
    "Shingles": {
        "Core": ["Painful localized rash", "Fluid-filled blisters", "Burning/Tingling"],
        "Secondary": ["Fever", "Headache", "Sensitivity to light", "Fatigue"],
        "Next Steps": "Seek care within 72 hours for antiviral medication.",
        "Precautions": ["Cover the rash", "Avoid contact with pregnant women/infants."]
    },
    "Tonsillitis": {
        "Core": ["Red/Swollen Tonsils", "White/Yellow Coating", "Sore Throat"],
        "Secondary": ["Painful swallowing", "Fever", "Bad breath", "Neck stiffness"],
        "Next Steps": "Gargle with salt water; consult if symptoms are severe.",
        "Precautions": ["Get plenty of rest", "Use a cool-mist humidifier."]
    },
    "Hyperthyroidism": {
        "Core": ["Rapid Heartbeat", "Unintentional Weight Loss", "Nervousness"],
        "Secondary": ["Tremor in hands", "Increased sweating", "More frequent bowel movements"],
        "Next Steps": "Consult for blood tests (T3, T4); monitor heart rate.",
        "Precautions": ["Avoid excessive caffeine", "Manage stress levels."]
    },
    "Carpal Tunnel Syndrome": {
        "Core": ["Tingling in thumb/fingers", "Numbness in hand", "Weakness"],
        "Secondary": ["Pain traveling up arm", "Dropping objects"],
        "Next Steps": "Use a wrist splint at night; take frequent hand breaks.",
        "Precautions": ["Ensure ergonomic workspace", "Perform wrist stretches."]
    }
}

