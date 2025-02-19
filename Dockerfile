# Use Python base image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    python3-dev \
    gcc \
    --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory in container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files into container
COPY . /app/

# Expose port for Django app (default: 8000)
EXPOSE 8000

# Command to start Django server (adjust if using Gunicorn)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
