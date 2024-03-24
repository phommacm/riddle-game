# Using the official Python 3.10 base image
FROM python:3.10.12-slim

# Setting the working directory in the container
WORKDIR /app

# Copying the application files into the container
COPY . /app

# Instalting dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Exposing the port the app will run on
EXPOSE 5000

# Set the command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]
