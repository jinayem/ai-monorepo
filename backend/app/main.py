# backend/app/main.py
from fastapi import FastAPI
from app.logic.ai_logic import run_dummy_inference

app = FastAPI(title="AI Platform - Backend", version="0.1.0")

@app.get("/")
async def root():
    return {"status": "ok", "service": "ai-backend"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/predict")
async def predict(data: dict):
    """
    Accepts JSON: {"input": [1, 2, 3]}
    Runs dummy inference using PyTorch.
    """
    input_data = data.get("input", [])
    result = run_dummy_inference(input_data)
    return {"prediction": result}
