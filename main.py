from fastapi import FastAPI
from pydantic import BaseModel
import json
from datetime import datetime

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