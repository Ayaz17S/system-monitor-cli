# Use a lightweight official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker layer caching
# Note: Since the prompt didn't include a requirements.txt, we assume the necessary library (psutil) is listed here.
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
# Assuming your script is named 'monitor.py'
COPY monitor.py .

# Define the default command to run when the container starts
# This runs your script with the default CPU sort and 1.0s interval
# The -u flag prevents stdout buffering issues in Docker
CMD ["python", "-u", "monitor.py"]