# Start from an official Python base image
FROM python:3.11-slim

# Prevent Python from writing .pyc files and buffer logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create and set working directory
WORKDIR /app

# Install system dependencies (for Pillow, psycopg2, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
 && rm -rf /var/lib/apt/lists/*

# Copy only requirements first for caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy project files into container
COPY . .

# Collect static files (ignore if settings.STATIC_ROOT is not set yet)
RUN python manage.py collectstatic --noinput || true

# Expose port for Render
EXPOSE 8000

# Default command — start Gunicorn server
CMD ["gunicorn", "hamperbox.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
