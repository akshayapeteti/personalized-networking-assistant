from fastapi import FastAPI
from pydantic import BaseModel
import json
from datetime import datetime
from services.fact_checker import fact_check

app = FastAPI()


class UserProfile(BaseModel):
    name: str
    skills: list[str]
    interests: list[str]
    career_goals: str


@app.post("/generate-message")
def generate_message(profile: UserProfile):

    message = (
        f"Hi, I'm {profile.name}. "
        f"I have skills in {', '.join(profile.skills)} "
        f"and I'm interested in {', '.join(profile.interests)}. "
        f"My career goal is {profile.career_goals}."
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
            "message": message,
            "time": str(datetime.now())
        }
    )

    with open("history.json", "w") as f:
        json.dump(history, f, indent=4)

    return {"message": message}


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