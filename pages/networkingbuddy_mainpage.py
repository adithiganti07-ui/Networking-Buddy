import streamlit as st
import google.generativeai as genai
if "nou" in st.session_state:
    name = st.session_state.nou
    st.write("Name:",name)
if "descp" in st.session_state:
    desc=st.session_state.descp



st.title("Conversation Starter AI")
genai.configure(api_key='Google API key')
model=genai.GenerativeModel("gemini-2.5-flash")


people_to_approach = st.number_input(
    "How many people do you want to approach? (1 for single person, >1 for group)",
    min_value=1,
    step=1
)

# Situation around them
situation = st.text_area(
    "Describe your surroundings/situation (what's happening around you)",
    placeholder="e.g., I'm in the library, a group is sitting near me talking softly..."
)

# Motivation request
motivation_request = st.radio(
    "Do you want motivation?",
    ["Yes", "No"]
)

# Submit button
submit = st.button("Generate")
if submit:
    prompt = f"""
You are a personalized social-skills and motivation assistant.

Here is the user's information:
- Personality description of user: {desc}
- Number of people they want to approach (group or single): {people_to_approach}
- Current situation described by the user: {situation}
- Whether they want motivation: {motivation_request}

YOUR TASKS:

1. Conversation Starters:
   Based on the user's personality, the number of people they want to talk to, and the situation they described, generate:
   - 3 to 5 conversation starters
   - Make them realistic, simple, natural, and ready to use immediately
   - Match the tone to the user's personality
   - If it's a group → give group-appropriate openers
   - If it's one person → give one-on-one openers

2. Motivation (ONLY if requested):
   If motivation_request is YES:
       - Give short, personalized, energetic motivation connected to their personality and situation.
   If motivation_request is NO:
       - Do NOT give any motivation.

3. Keep your tone friendly, concise, and tailored to the user.
"""



    response=model.generate_content(prompt)
    st.write(response.text)


