# backend/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# copy requirements then install (caching)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 🔥 Add dev requirements (optional, for ML env)
COPY dev-requirements.txt /app/
RUN pip install --no-cache-dir -r dev-requirements.txt

# copy app
COPY app /app/app
COPY scripts /app/scripts

ENV PYTHONUNBUFFERED=1
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
