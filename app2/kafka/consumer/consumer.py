from confluent_kafka import Consumer, KafkaError
import pymongo
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("URL")
connection = pymongo.MongoClient(url)
Device_Data = connection[os.getenv("Database_Name")]
device_collection = Device_Data[os.getenv("Collection")]

config = {
    'bootstrap.servers': os.getenv("bootstrap_servers"),
    'group.id': os.getenv("Group_Id"),
    'auto.offset.reset': 'earliest', # using earliest to get the data where stopped from the consumer
    'enable.auto.commit': False  # Disabling auto commit
}

consumer = Consumer(config)
consumer.subscribe([os.getenv("topic")])

try:
    while True:

        # It will wait for 1 sec and check again there are new messages or not 
        message = consumer.poll(1.0)
        if message is None:
            continue
        if message.error():
            if message.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(f"Error: {message.error()}")
                break

        json_str = message.value().decode('utf-8')
        # print("consumer",json_str)

        try:
            document = json.loads(json_str)
            print("document: ",document)
            if isinstance(document, dict):
                device_collection.insert_one(document)
            else:
                print("Invalid document format:", document)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

        # Commit the offset
        consumer.commit()

except KeyboardInterrupt:
    print("Interrupted. Closing consumer.")
finally:
    # Close down consumer to commit final offsets.
    consumer.close()
    print("Consumer closed.")