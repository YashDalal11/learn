from confluent_kafka import Producer

# create callback for delivery reports
def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}], offset: {msg.offset()}, timestamp: {msg.timestamp()[1]}")

producer = Producer({"bootstrap.servers": "localhost:9092"})

for i in range(20):
    # produce message
    producer.produce(
        "demo-topic-2", key=f"key {i}", value=f"hello {i}".encode("utf-8"), callback=delivery_report
    )
    # serve delivery reports for previous messages
    producer.poll(0)


producer.flush()
