import streamlit as st
import re
import csv
st.set_page_config(page_title="Signup — NetworkingBuddy", page_icon="🎓", layout="wide")
st.markdown(
    """<style>
    .stApp { background-color: #f4c2c2; }
    h1 { color: #8e5151; text-align: center; }
    div.stButton > button { background-color: #8e5151; color: white; border-radius: 8px; padding: 8px 20px; }
    </style>""",
    unsafe_allow_html=True
)
def isvalidmail(mail):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.fullmatch(pattern,mail):
        return True
    else:
        return False
st.title("Create an Account")
with st.form("signup_only_form"):
    username = st.text_input("Username").strip()
    password = st.text_input("Password", type="password").strip()
    confirm = st.text_input("Confirm Password", type="password").strip()
    full_name = st.text_input("Full name").strip()
    age = st.number_input("Age", min_value=1, max_value=120, value=18, step=1)
    gmail = st.text_input("Email (Gmail)").strip()
    desc=st.text_input("Enter social personality desc")
    submit = st.form_submit_button("Create Account")
def al():
    b=full_name.split()
    c=0
    for i in b:
        if i.isalpha():
            c=1
        else:
            c=0
    if c==0:
        return False
    else:
        return True
            
if submit:
    # Basic validation
    if not username :
        st.error("Username is required.")
    elif username.isdigit():
        st.error("Username invalid include charecters a-z")
    elif not password:
        st.error("Password is required.")
    elif len(password)<5:
        st.error("password must be atleast 5 charecters")
    elif password != confirm:
        st.error("Passwords do not match.")
    elif not full_name:
        st.error("Full name is required.")
    elif not al():
        st.error("invalid name")
    elif not gmail:
        st.error("Email is required.")
    elif not isvalidmail(gmail):
        st.error("invalid gmail")
    elif not desc:
        st.error("desc required")
    else:
        with open("users.csv", "a", newline="") as users:
            writer = csv.writer(users)
            writer.writerow([full_name,username,password,gmail,age,desc])
        st.switch_page("pages/networkingbuddy_login.py")
