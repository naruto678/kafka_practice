
from kafka import KafkaConsumer
from kafka import KafkaAdminClient
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

client = KafkaAdminClient(bootstrap_servers=['localhost:9092'])


executor = ThreadPoolExecutor(max_workers= 5)

def callback(message):
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))


consumer = KafkaConsumer('Topic1', bootstrap_servers=['localhost:9092'])

for message in consumer:
    future = executor.submit(callback, message)
    print(future.result()) 


