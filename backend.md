# Backend

This page covers backend-specific topics that do not fall under system design. For system design topics, refer to the [System Design](system-design.md) page.

## Message brokers

Message brokers are middleware systems used in distributed systems to send, recieve and process information between applications or services. A message broker typically involves provider (node sending information) and consumers (node recieving information).

Message brokers like RabbitMQ, Apache Kafka, Redis, or ActiveMQ help decouple systems, ensuring reliable and scalable communication in distributed architectures.

Key functions of a message brokers include:
- **Validation, storing, routing, and reliable delivery of a message** to the appropriate destination.
- **Message Queuing:** Stores messages temporarily to ensure delivery, even if the consumer is unavailable or slow to process them.
- **Load Balancing:** Distributes messages across multiple consumers to balance the workload.
- **Publish/Subscribe model:** Supports sending messages to multiple consumers subscribed to a topic.

Benefits of message brokers include:
- **Decoupling:** Producers and consumers don’t need to know about each other’s implementation.
- **Fault tolerance:** Ensures messages aren't lost if a consumer or producer fails temporarily
- **Asynchronous Processing**
- **Scalability:** Simplifies adding more producers or consumers.

## Meaning of ACK and NACK

In message queues (RabitMQ or Kafka), consumers use signals to communicate the result of a message back to the queue systems.

### ACK (Acknowledged)
This signal is sent when a message has been successfully processed. It tells the broker that it can safely remove it from the queue and prevents re-delivery.

### NACK (Negative Acknowledgement)
This signal is sent when a message has failed to process. The broker may then try to requeue the message, move it to a dead-letter queue after a certain number of retries or drop it (in poorly configured systems).

### REJECT
While similar to NACK, REJECT instructs the consumer whether to discard of requeue an individual message, possibly by use of a flag.

### Important points
- **Dead-lettering:** messages that fail repeatedly after max NACKs will be moved to a dead-letter queue for further inspection and possibly manual requeuing. 
- **Auto-ACK:** The consumer automatically signals that the message is acknowledged as soon as it's delivered. However, this poses the risk of the message being lost if the consumer crashes before delivery.
- **Manual-ACK:** The consumer explicitly signals that the message has been successfully processed. This guarantees at-least-once delivery.
- **At-least-once delivery:** at least one attempt of processing a delivered messaged is successful.