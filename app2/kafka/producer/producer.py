import os
from confluent_kafka import Producer
from dotenv import load_dotenv
import socket

load_dotenv()

# Creating socket connection [default parameters are TCP and IPV4(If needed we can change it)]
server = socket.socket()

# Setting connection with server
server.connect((os.getenv("host"), int(os.getenv("port"))))

config = {
    'bootstrap.servers': os.getenv('bootstrap_servers')
}

# Creating Producer instance
producer = Producer(config)

while True:
    try:
        data = server.recv(1024).decode('utf-8')
        producer.produce(os.getenv("topic"), key="SCMXpert", value=data)
        print(data)
        
    
      
    except socket.timeout:
        print("No data received in the last 10 seconds.")
    except ConnectionResetError:
        print("Connection reseted.")
        break

# Wait for any outstanding messages to be delivered and delivery reports received
producer.flush()


# Closing server
server.close()