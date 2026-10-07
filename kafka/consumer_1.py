from confluent_kafka import Consumer, KafkaException

# Consumer configuration
conf = {
    'bootstrap.servers': 'localhost:9092',   # Kafka broker
    'group.id': 'consumer-group-demo',         # Consumer group ID
    'auto.offset.reset': 'latest'          # Start from beginning if no offset stored
}

# Create consumer
consumer = Consumer(conf)

# Subscribe to topic(s)
consumer.subscribe(['demo-topic-2'])

try:
    while True:
        msg = consumer.poll(1.0)  # waits up to 1 second for new message

        if msg is None:
            continue   # no message yet
        if msg.error():
            raise KafkaException(msg.error())

        print(f"{msg.value().decode('utf-8')} "
              f"{msg.topic()} partition: {msg.partition()} offset: {msg.offset()}")

except KeyboardInterrupt:
    pass
finally:
    # Leave group and commit final offsets
    consumer.close()
