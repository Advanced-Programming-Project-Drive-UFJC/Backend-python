# Use the official Python image as the base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the FastAPI application code
COPY /backend_python/ .

# Expose the port the app runs on
EXPOSE 5000

# Run the FastAPI application with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]

# docker build -t condor_backend_python:1.0 .
# docker run -d -p 8000:8000 --name condor_backend condor_backend_python:1.0