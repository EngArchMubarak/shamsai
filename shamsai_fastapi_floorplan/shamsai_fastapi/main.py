from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class DesignRequest(BaseModel):
    location: str
    num_floors: int
    num_bedrooms: int
    has_pool: bool
    pool_type: Optional[str] = None  # 'indoor' or 'outdoor'
    has_yard: bool
    yard_type: Optional[str] = None  # 'front' or 'back'

@app.get("/")
def read_root():
    return {"message": "ShamsAI FastAPI backend is running!"}

@app.post("/generate-design")
def generate_design(request: DesignRequest):
    # (راح نكمل لاحقاً من هنا بناء الذكاء الصناعي أو المخططات)
    return {
        "status": "received",
        "data": request.dict()
    }