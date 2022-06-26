
from kafka import KafkaConsumer
from kafka import KafkaAdminClient

topic = input('Enter the name of the topic that you want to list messages to\n')
client = KafkaAdminClient(bootstrap_servers=['localhost:9092'])

if topic not in client.list_topics():
    print(f'${topic} not in ${client.list_topics()}')
    exit()     

consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'])

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))




