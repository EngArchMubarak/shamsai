from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Temporary in-memory store
user_sessions = {}


class DesignAnswers(BaseModel):
    user_id: str
    answer: str


questions = [
    "How many floors do you want?",
    "How many bedrooms?",
    "Do you want a swimming pool?",
    "Is the pool indoor or outdoor?",
    "Do you want a yard?",
    "Is the yard in front or back?"
]


@app.get("/")
def read_root():
    return {"message": "ShamsAI FastAPI backend is running!"}


@app.post("/start")
def start_design(user_id: str):
    user_sessions[user_id] = {"step": 0, "answers": []}
    return {"question": questions[0]}


@app.post("/answer")
def answer_question(answer: DesignAnswers):
    session = user_sessions.get(answer.user_id)
    if session is None:
        return {"error": "Session not found. Start again."}

    step = session["step"]
    session["answers"].append(answer.answer)
    session["step"] += 1

    if session["step"] < len(questions):
        return {"question": questions[session["step"]]}
    else:
        return {
            "message": "Thank you! Generating architectural layout...",
            "user_input": session["answers"]
        }
