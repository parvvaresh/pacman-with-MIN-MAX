# Use the official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python file into the container
COPY . .

# Run the Python file
CMD ["python", "play.py"]
