# Use the official Python 3.12.1 base image
FROM python:3.12.1

# Set the working directory inside the container
WORKDIR /SCMXPERTLITE/app/kafka/producer

# Install required Python packages using pip
RUN pip install python-dotenv confluent-kafka

# Copy the contents of the current directory to the container's working directory
COPY . /SCMXPERTLITE/app/kafka/producer

# Set the default command to run the Python script "producer.py" when the container starts
CMD [ "python", "producer.py" ]
