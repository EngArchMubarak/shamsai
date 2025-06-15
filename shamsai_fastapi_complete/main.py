from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class DesignRequest(BaseModel):
    num_floors: int
    num_bedrooms: int
    has_pool: bool
    pool_type: Optional[str] = None  # "indoor" or "outdoor"
    has_yard: bool
    yard_type: Optional[str] = None  # "front" or "back"
    notes: Optional[str] = None

@app.get("/")
def read_root():
    return {"message": "ShamsAI FastAPI backend is running!"}

@app.post("/generate-design")
def generate_design(request: DesignRequest):
    # Generate architectural zones (mock logic for now)
    zones = []

    if request.num_floors >= 1:
        zones.append("Ground floor: Entrance lobby, living room, kitchen, bathroom")
    if request.num_floors >= 2:
        zones.append("First floor: " + f"{request.num_bedrooms} bedrooms, family hall, bathrooms")

    if request.has_pool:
        if request.pool_type == "indoor":
            zones.append("Indoor swimming pool included")
        elif request.pool_type == "outdoor":
            zones.append("Outdoor pool in backyard")

    if request.has_yard:
        if request.yard_type == "front":
            zones.append("Front yard with green landscaping")
        elif request.yard_type == "back":
            zones.append("Backyard with seating area")

    if request.notes:
        zones.append(f"Notes: {request.notes}")

    return {
        "status": "success",
        "zones": zones
    }
