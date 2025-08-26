from kafka import KafkaConsumer
import json

class ConsumerKafka:
    def __init__(self):
        pass



if __name__ =="__main__":
    topic = "topic-1"
    group_id_1 = "group_id-1"

    consumer = KafkaConsumer(topic,
                                group_id= group_id_1,
                                value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                bootstrap_servers=['localhost:9092'],
                                consumer_timeout_ms=10000)

    print(consumer)



    # Iterate through the messages
    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                             message.offset, message.key,
                                             message.value))
    
    


