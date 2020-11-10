FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

# Code dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
WORKDIR /app
COPY . .
