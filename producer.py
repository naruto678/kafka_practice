#!/usr/bin/env/python3

from kafka import KafkaProducer 
from kafka.errors import KafkaError
import json
from random import random 
from time import time

from concurrent.futures import ThreadPoolExecutor

from kafka import KafkaAdminClient
from kafka.admin.new_topic import NewTopic
producer = KafkaProducer(bootstrap_servers = ['localhost:9092'])

## Get a list of topics that are currently present in the brokers 

admin_client = KafkaAdminClient(bootstrap_servers=['localhost:9092'])

#admin_client.delete_topics(['topic list'])
#topics =admin_client.list_topics()
topics=['Topic1','Topic2','Topic3']


for topic in admin_client.list_topics():
    print(topic)

print(f'Topics currently present in the brokers  ${topics}') 
new_topics = [NewTopic(topic, num_partitions=3, replication_factor=1) for topic in topics]

# Call create_topics to asynchronously create topics. A dict
# of <topic,future> is returned.
try:    
    fs = admin_client.create_topics(new_topics)
except Exception as ex: 
    print(ex) 

def send_message(): 
    print("sending messsage") 
    future = producer.send('Topic1', bytes(json.dumps(str(time())+' '+str(random())), 'utf-8'))
    return future

while True: 
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(send_message)
        print(future.result())
