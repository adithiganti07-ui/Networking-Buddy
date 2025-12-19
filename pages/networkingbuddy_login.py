import streamlit as st
st.set_page_config(
    page_title="NetworkingBuddy Admin Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded")

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

st.title("Login")

login_form = st.form("login_form")
username_input = login_form.text_input("Username").strip()
password_input = login_form.text_input("Password", type="password").strip()
login_button = login_form.form_submit_button("Login")
with open("users.csv","r") as users:
    c=0
    if login_button:
        for i in users:
            b=i.split(",")
            for j in b:
                if b[1]==username_input and b[2]==password_input:
                    name=b[0]
                    desc=b[-1][:-1]
                    c=1
                    break
        if c==0:
            st.error("Invalid username or password")
        else:
            st.success("successful")
            st.session_state.username =username_input
            st.session_state.nou=name
            st.session_state.descp = desc
            st.switch_page("pages/networkingbuddy_mainpage.py")
st.page_link("pages/networkingbuddy_signup.py", label="Dont have an account? Sign up here!")


