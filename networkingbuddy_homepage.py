import streamlit as st
st.set_page_config(
    page_title="NetworkingBuddy Admin Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded")
# Custom CSS for better styling
st.markdown(""" <style>
.stApp{background-color: #f4c2c2  ;}
</style>""", unsafe_allow_html= True)

st.markdown("""
<style>
h2 {
    font-size: 2.5rem;
    font-weight: bold;
    color: #8e5151    ;
    text-align: center;
    margin-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
"""
<style>
h1 {
    font-size: 2.25rem;        /* Larger size for title */
    font-weight: bold;
    color: #8e5151;         /* Your chosen color */
    text-align: justify;
    margin-bottom: 2rem;
}

p {
    font-size: 1.2rem;      /* Size for paragraphs (st.write content) */
    color: #333333;
    text-align: justify;    /* Or 'center' if preferred */
    margin-bottom: 1.5rem;
}
</style>
""",
unsafe_allow_html=True
)
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #8e5151;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #f4c2c2;
    }
    </style>
""", unsafe_allow_html=True)

st.header("Welcome to NetworkingBuddy")
st.title("About NetworkingBuddy AI")
st.write("Welcome to Nexus AI — the smart connect app created for students who want to grow, but sometimes don’t know how to start.")
st.title("Our Mission")
st.write("To empower students with the confidence, insights, and tools they need to build meaningful connections, strengthen their productivity, and thrive in college and beyond.")
st.title("What We Do")
st.write("""With NetworkingBuddy, you can:

Jump into conversations effortlessly — Explore curated topics from pop culture, entertainment, technology, and current trends so you always have something to talk about.

Ask the right questions — Use smart conversation prompts to learn from your peers and build deeper connections.

Boost your productivity — Get study hacks, time-management techniques, and routines tailored for student life.

Build social skills — Learn practical communication strategies to overcome social anxiety and feel more confident.""")
st.title("Why We Built It")
st.write("Networking and social interaction can be daunting, especially when you're juggling academics, new environments, and high expectations. We built Nexus AI to make those first steps easier, helping you navigate social spaces and unlock opportunities — even if you struggle with what to say or how to start.")
st.title("Our vision")
st.write("We envision a world where every student feels confident to connect, collaborate, and create — without letting fear or uncertainty hold them back.")

col1,col2,col3=st.columns([2,2,2])
st.write("\n")
with col1:
    st.write("Make sure you login for a better experience!")
    if st.button("LOGIN"):
         st.switch_page("pages/networkingbuddy_login.py")
with col3:
    st.write("Make sure you sign in for amazing deals!")
    if st.button("SIGNUP"):
        st.switch_page("pages/networkingbuddy_signup.py")
st.write("---")
