# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /Voice-Assistant/

# Copy the application files to the container
COPY . /Voice-Assistant/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on (adjust as necessary)
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]