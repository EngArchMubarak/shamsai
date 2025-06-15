from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Room(BaseModel):
    name: str
    area: float

class FloorPlanRequest(BaseModel):
    total_area: float
    rooms: List[Room]

@app.get("/")
def read_root():
    return {"message": "ShamsAI FastAPI backend for floorplans is running!"}

@app.post("/generate_plan/")
def generate_plan(data: FloorPlanRequest):
    room_count = len(data.rooms)
    avg_allocation = round(data.total_area / room_count, 2) if room_count else 0
    plan = {room.name: {"requested_area": room.area, "allocated_area": avg_allocation} for room in data.rooms}
    return {"floor_plan": plan}
