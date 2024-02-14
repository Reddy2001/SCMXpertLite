# Use the official Python 3.12.1 base image
FROM python:3.12.1

# Set the working directory inside the container
WORKDIR /SCMXPERTLITE/app/kafka/consumer

# Install required Python packages using pip
RUN pip install confluent-kafka pymongo python-dotenv

# Copy the contents of the current directory to the container's working directory
COPY . /SCMXPERTLITE/app/kafka/consumer

# Set the default command to run the Python script "consumer.py" when the container starts
CMD ["python", "consumer.py"]

