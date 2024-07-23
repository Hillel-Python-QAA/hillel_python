# Використовуємо офіційний образ Python
FROM python:3.12.4-slim-bullseye

COPY . /app
WORKDIR /app

# Виконуємо команди
RUN pip install -r requirements.txt --no-cache

# COPY




CMD ["python"]