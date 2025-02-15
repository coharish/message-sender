# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    chromium-browser \
    chromium-chromedriver \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV DISPLAY=:99

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run the script
CMD ["python", "WhatsApp_Automation.py"]