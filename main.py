from fastapi import FastAPI
from pydantic import BaseModel
import json
from datetime import datetime
from services.fact_checker import fact_check
from event_analyzer import extract_event_themes
from topic_generator import generate_topics

app = FastAPI()


class UserProfile(BaseModel):
    name: str
    skills: list[str]
    interests: list[str]
    career_goals: str

@app.post("/analyze-profile")
def analyze_profile(profile: UserProfile):
    return {
        "name": profile.name,
        "skills": profile.skills,
        "interests": profile.interests,
        "career_goal": profile.career_goals,
        "analysis":
        f"{profile.name} has strong skills in "
        f"{', '.join(profile.skills)} and is interested in "
        f"{', '.join(profile.interests)}."
    }
@app.post("/generate-recommendations")
def generate_recommendations(profile: UserProfile):
    recommendations = []

    if "Python" in profile.skills:
        recommendations.append(
            "Build AI and automation projects."
        )

    if "Google Cloud" in profile.skills:
        recommendations.append(
            "Pursue Google Cloud certifications."
        )

    if "AI" in profile.interests:
        recommendations.append(
            "Participate in AI hackathons and networking events."
        )

    if len(recommendations) == 0:
        recommendations.append(
            "Continue improving technical and networking skills."
        )

    return {
        "recommendations": recommendations
    }
@app.post("/generate-message")
def generate_message(profile: UserProfile):

    description = (
        f"{profile.name} has skills in "
        f"{', '.join(profile.skills)} "
        f"and interests in "
        f"{', '.join(profile.interests)}."
    )

    themes = extract_event_themes(description)

    suggestions = generate_topics(
        themes,
        profile.interests
    )

    history = []

    try:
        with open("history.json", "r") as f:
            history = json.load(f)
    except:
        history = []

    history.append(
        {
            "name": profile.name,
            "themes": themes,
            "suggestions": suggestions,
            "time": str(datetime.now())
        }
    )

    with open("history.json", "w") as f:
        json.dump(history, f, indent=4)

    return {
        "themes": themes,
        "suggestions": suggestions
    }


@app.get("/")
def home():
    return {"message": "Personalized Networking Assistant API is running!"}


@app.get("/history")
def get_history():
    try:
        with open("history.json", "r") as f:
            return json.load(f)
    except:
        return []
@app.get("/fact-check/{topic}")
def check_fact(topic: str):
    return {
        "result": fact_check(topic)
    }
@app.post("/feedback")
def save_feedback(
    suggestion: str,
    action: str
):
    try:
        with open("feedback.json", "r") as f:
            feedback = json.load(f)
    except:
        feedback = []

    feedback.append(
        {
            "suggestion": suggestion,
            "action": action,
            "time": str(datetime.now())
        }
    )

    with open("feedback.json", "w") as f:
        json.dump(
            feedback,
            f,
            indent=4
        )

    return {
        "message": "Feedback saved"
    }