# Use a Python base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the Flask application code into the container
COPY app.py app.py
COPY static static
COPY templates templates

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port the Flask app runs on
EXPOSE 5000

# Command to run the application
CMD ["flask", "run"]
