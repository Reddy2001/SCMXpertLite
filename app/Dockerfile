# Use the official Python 3.12.1 base image
FROM python:3.12.1

# Set the working directory inside the container
WORKDIR /SCMXPERTLITE/app/

# Copy the requirements.txt file to the container's working directory
COPY requirements.txt /SCMXPERTLITE/app/

# Install Python dependencies from requirements.txt
# Note: --no-cache-dir is used to avoid caching downloaded packages, --trusted-host is used for specifying the trusted host (pypi.python.org)
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the application code to the container's working directory
COPY . /SCMXPERTLITE/app/

# Expose port 8067 for communication
EXPOSE 8067

# Set the default command to run the Uvicorn server with the specified parameters
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8067"]
