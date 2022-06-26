#!/usr/bin/env/python3

from kafka import KafkaProducer 
from kafka.errors import KafkaError
import json 
from time import time
from kafka import KafkaAdminClient

producer = KafkaProducer(bootstrap_servers = ['localhost:9092'])


## Get a list of topics that are currently present in the brokers 

admin_client = KafkaAdminClient(bootstrap_servers=['localhost:9092'])

topics = admin_client.list_topics()
print(f'Topics currently present in the brokers  ${topics}') 


while True:
    print('>' , end = ' ')
    user_input = input('Enter the message that you want to send')
    print('>', end = ' ')
    topic = input('Enter the topic name that you want to send')
    
    current_time = time()
    val = {'user': user_input, 'current_time' : current_time}
    future = producer.send('test-topic', bytes(json.dumps(val), 'utf-8'))
    try: 
        record_metadata = future.get(timeout = 10 ) 
    except KafkaError as ex: 
        print(ex) 
    print(record_metadata.topic)
    print(record_metadata.partition) 
    print(record_metadata.offset)
    print('Message sent')

