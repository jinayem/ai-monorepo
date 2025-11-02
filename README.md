# AI-Monorepo

Monorepo skeleton for an AI stack combining:
- Backend: FastAPI (Python)
- Frontend: React + Vite + Tailwind CSS

## Overview

This monorepo provides a unified structure for full-stack AI development and deployment. It supports both local development and Docker-based isolated environments for ML workloads.

## Day 1: Initialization

- Created base monorepo structure.
- Added backend/ and frontend/ skeleton folders.
- Initialized Git repository and .gitignore.
- verified FastAPI backend setup.

**Run backend locally:**

cd backend
uvicorn app.main:app --reload

## Day 2: ML Development Environment (Docker)

- Added a multi-stage Dockerfile for backend with:
    - builder → Python 3.10-slim base image
    - dev → ML environment (PyTorch, Transformers, TRL)
    - runtime → Production-ready lightweight image
- Installed:
    - PyTorch 2.3.0
    - Transformers 4.44.0
    - TRL 0.11.4
- Verified ML environment via scripts/torch_test.py.
- Confirmed Hugging Face model runs successfully inside container.

**Run and test in Dev Container:**

cd backend
docker build --target dev -t ai-backend:day2dev .
docker run -it --rm ai-backend:day2dev bash
python scripts/torch_test.py