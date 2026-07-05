import streamlit as st
import requests

st.title("Personalized Networking Assistant")

st.write("Enter your details below.")

name = st.text_input("Name")
skills = st.text_input("Skills (comma separated)")
interests = st.text_input("Interests (comma separated)")
career_goals = st.text_input("Career Goals")

if st.button("Generate Networking Message"):

    data = {
        "name": name,
        "skills": [s.strip() for s in skills.split(",") if s.strip()],
        "interests": [i.strip() for i in interests.split(",") if i.strip()],
        "career_goals": career_goals
    }

    response = requests.post(
        "http://127.0.0.1:8000/generate-message",
        json=data
    )

    if response.status_code == 200:
        st.success(response.json()["message"])
    else:
        st.error("Something went wrong!")