# Use an official Python runtime as the base image
FROM python:latest

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirement.txt file to the container
COPY requirements.txt .

# Install the packages listed in the requirement.txt file
RUN python3 -m pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .


# Run the chatbot application
CMD ["python", "training.py"]
