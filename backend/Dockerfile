# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.10-slim

# Set the working directory.
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies.
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend directory contents into the container at /app
COPY backend /app/backend

# Copy the manage.py file into the container at /app
COPY manage.py /app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the Django development server.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
