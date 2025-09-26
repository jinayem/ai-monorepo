# backend/app/main.py
from fastapi import FastAPI

app = FastAPI(title="AI Platform - Backend", version="0.1.0")

@app.get("/")
async def root():
    return {"status": "ok", "service": "ai-backend"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
