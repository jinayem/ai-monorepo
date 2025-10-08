# backend/Dockerfile
# Multi-stage: builder -> dev (optional) -> runtime (final small image)

# -------- builder (compile & install runtime deps) ----------
FROM python:3.11-slim AS builder
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /build

# Minimal system packages required to build wheels (kept only in builder)
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      build-essential gcc ca-certificates curl \
 && rm -rf /var/lib/apt/lists/*

# Ensure pip tooling is fresh
RUN python -m pip install --upgrade pip setuptools wheel

# Copy and install runtime requirements into a predictable prefix (/install)
COPY requirements.txt /build/requirements.txt
RUN pip install --no-cache-dir --prefix=/install -r /build/requirements.txt

# -------- dev stage (optional; heavy ML/dev deps) ----------
FROM builder AS dev
WORKDIR /app

# install heavy ML/dev dependencies
COPY dev-requirements.txt /build/dev-requirements.txt
RUN pip install --no-cache-dir --prefix=/install -r /build/dev-requirements.txt

# copy runtime site-packages from builder
COPY --from=builder /install /usr/local

# copy app source code so you can test/run it inside the dev container
COPY app /app/app
COPY scripts /app/scripts
COPY requirements.txt /app/requirements.txt

# expose port for local FastAPI debugging
EXPOSE 8000

# default command for dev: interactive shell or you can override in docker run
CMD ["bash"]

# -------- runtime stage (final small image) ----------
FROM python:3.11-slim AS runtime
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# minimal runtime OS deps (certificates)
RUN apt-get update \
 && apt-get install -y --no-install-recommends ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# copy installed python packages from builder -> this brings only site-packages, no build tools
COPY --from=builder /install /usr/local

# copy application code (no .venv)
COPY app /app/app
COPY scripts /app/scripts
COPY requirements.txt /app/requirements.txt

EXPOSE 8000

# production command (no reload). For development use the dev image.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
