from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class DesignRequest(BaseModel):
    num_floors: int
    num_bedrooms: int
    has_pool: bool
    pool_type: Optional[str] = None
    has_yard: bool
    yard_type: Optional[str] = None

@app.get("/")
def read_root():
    return {"message": "ShamsAI FastAPI backend is running!"}

@app.post("/generate-design")
def generate_design(req: DesignRequest):
    return {"status": "received", "data": req}
