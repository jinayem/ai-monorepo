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

```bash
cd backend
uvicorn app.main:app --reload
```

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

```bash
cd backend
docker build --target dev -t ai-backend:day2dev .
docker run -it --rm ai-backend:day2dev bash
python scripts/torch_test.py
```

## Day 3: Add Dummy AI Inference + CI Pipeline Validation

- Added a minimal /predict API endpoint for dummy AI inference.
- Implemented CPU-fallback inference logic for environments without GPU.
- Added request/response validation for predictable behavior.
- Extended GitHub Actions CI pipeline to:
    - install backend dependencies
    - start FastAPI server on port 9000
    - verify /health endpoint
    - validate /predict inference with test payload
- Ensured backend boots correctly inside CI using Uvicorn in background mode.

**Run backend locally (dev mode):**

```bash
cd backend
uvicorn app.main:app --reload
```

**Run backend for CI-style test locally:**

```bash
cd backend
python -m uvicorn app.main:app --host 127.0.0.1 --port 9000
```

**Test Endpoints:**

```bash
curl http://127.0.0.1:9000/health
curl -X POST http://127.0.0.1:9000/predict \
  -H "Content-Type: application/json" \
  -d '{"input": [1, 2, 3]}'
```

**ML Runtime Dependencies (Updated):**

Our backend service now includes runtime machine learning dependencies required for model inference. These packages are installed from requirements.txt so that production Docker images contain only what is needed to serve requests efficiently.

**Why this change?**

Previously, only development dependencies (Torch, Transformers, TRL) were included in ``dev-requirements.txt``, which meant the final runtime Docker image did not contain required ML packages. This caused:

```ModuleNotFoundError: No module named 'torch'```

To support inference in the production container, we added the following dependencies to ``requirements.txt``:

```bash
# Runtime ML dependencies for inference
torch==2.3.0
transformers==4.44.0
trl==0.11.4
```