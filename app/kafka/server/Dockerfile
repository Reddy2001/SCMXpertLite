# Use the official Python 3.12.1 base image
FROM python:3.12.1

# Set the working directory inside the container
WORKDIR /SCMXPERTLITE/app/kafka/server/

# Copy the contents of the current directory to the container's working directory
COPY . /SCMXPERTLITE/app/kafka/server/

# Install required Python packages using pip
RUN pip install python-dotenv

# Expose port 12121 for communication
EXPOSE 12121

# Set the default command to run the Python script "server.py" when the container starts
CMD ["python", "server.py"]
