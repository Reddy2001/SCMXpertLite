import socket
import json
import time
import random
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Creating socket connection [default parameters are TCP and IPV4(If needed we can change it)]
socket_connection = socket.socket()
print("Socket Created")

# Binding socket connection with local host and some random port number between 0 to 65535
# socket_connection.bind(("", int(os.getenv("port"))))
socket_connection.bind((os.getenv("host"), int(os.getenv("port"))))

# Server accepts 3 clients at a time 
socket_connection.listen(3)
print("waiting for connections")

#accept() accept the client address
#addr: This contains the address and port of the connected client. 
#client_socket is the new socket object returned by the accept(). It is used to send data to the client
client_socket, addr = socket_connection.accept()

print(f'Connection from {addr} has been Established.')


# Method to generate fake data
def generate_fake_data():

    device=[1122334455, 6677889900]

    # choosing id 
    device_id = str(random.choice(device))

    # Generate random Battery Level (assuming it's a percentage between 0 and 100)
    battery_level = round(random.uniform(0, 100), 2)

    # Generate random First Sensor Temperature with one decimal digit (assuming it's in Celsius)
    sensor_temperature = round(random.uniform(-10, 50), 1)

    route_fm=["Tirupati","Kadapa"]
    route_dest=["Nellore","Hyderabad"]

    # Choosing route_from and route_to
    route_from = str(random.choice(route_fm))
    route_to = str(random.choice(route_dest))

    # Get the current timestamp
    timestamp = datetime.now()
    

    # Format timestamp to "day-month-year" format
    timestamp_formatted = timestamp.strftime("%d-%m-%Y %H:%M:%S")

    # print(timestamp_formatted)
    return {
        "Device_Id": device_id,
        "Battery_Level": battery_level,
        "First_Sensor_Temperature": sensor_temperature,
        "Route_From": route_from,
        "Route_To": route_to,
        "Timestamp": timestamp_formatted,
    }



while True:
    try:

        # getting data from generate_fake_data() method
        data = generate_fake_data()
        
        # Serializing the data to json string and enconding it with UTF[It suitable for storage or transmission]
        display_Data = (json.dumps(data, indent=1)).encode("utf-8")
        print("Display_Data",display_Data)
        client_socket.send(display_Data)
        time.sleep(10)
    except Exception as e:
        print(e)
        client_socket.close()
        
    
