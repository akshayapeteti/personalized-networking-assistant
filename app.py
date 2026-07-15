import streamlit as st
import requests

st.title("🤝 Personalized Networking Assistant")

st.markdown(
    """
    Welcome to the Personalized Networking Assistant.

    Fill in your information and receive AI-powered networking suggestions.
    """
)

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

        result = response.json()

        st.success("AI Analysis Completed!")

        st.subheader("Detected Themes")

        for theme in result["themes"]:
            st.write("•", theme)


        st.subheader("Networking Suggestions")


        for i, suggestion in enumerate(result["suggestions"]):

            st.write("•", suggestion)

            col1, col2 = st.columns(2)


            with col1:

                if st.button("👍", key=f"like{i}"):

                    requests.post(
                        "http://127.0.0.1:8000/feedback",
                        params={
                            "suggestion": suggestion,
                            "action": "like"
                        }
                    )

                    st.success("Liked!")


            with col2:

                if st.button("👎", key=f"dislike{i}"):

                    requests.post(
                        "http://127.0.0.1:8000/feedback",
                        params={
                            "suggestion": suggestion,
                            "action": "dislike"
                        }
                    )

                    st.success("Disliked!")


    else:

        st.error("Something went wrong!")


# History Section

st.markdown("---")

st.subheader("Conversation History")


try:

    response = requests.get(
        "http://127.0.0.1:8000/history"
    )

    history = response.json()


    if len(history) == 0:

        st.write("No conversations yet.")


    else:

        for item in reversed(history):

            st.write("👤", item["name"])
            st.write(item["message"])
            st.caption(item["time"])
            st.markdown("---")


except:

    st.write("Could not load history.")