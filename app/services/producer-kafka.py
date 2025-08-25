from kafka import KafkaProducer
import json

class ProducerKafka:

    def __init__(self):
        pass
    


if __name__ =="__main__":
    


    topic = "topic-1"

    event = {"App":"Producer 1"}
    event_1 = {"App": "Producer 2"}

    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                value_serializer=lambda x:
                                json.dumps(x).encode('utf-8'))


    print(producer.metrics())
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                value_serializer=lambda x:
                                json.dumps(x).encode('utf-8'))

    print(producer.config)

    producer.send(topic, event)
    producer.flush()
