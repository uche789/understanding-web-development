# System Design

This page cover all topics related to system design.

## Distributed systems

Distributed systems are network of computers that work together as a single unit and communicate with one another to process information.

Some key characteristics of a distributed system are:
- Communication
- Availability
- Fault tolerance
- Shared goal
- Resource sharing
- Concurrency
- Geographical distribution

Examples of distrubuted systems include:
- Content Delivery Networks (CDNs)
- Microservices
- Client-server architecture
- Distributed dtabases
- Cloud computing networks
- The internet

## Microservices

Microservices are independent, deployable services that are responsible to perform a specific business function or task within a distributed system.

Benefits of microservices include:
- Decoupling
- Flexibility
- Scalability
- Ease of Deployment
- Fault isolation
- Technology Agnostic
- Independence
- Single Responsibility
- Decentralization: _Responsibility for data, logic, and other components is decentralized across microservices, promoting modularity._
- Communication: _Microservices communicate with each other through APIs, often using lightweight protocols like HTTP or messaging systems._

### Use case
- An **e-commerce application** could have separate microservices to handle authentication, orders, products, and fulfillment.
- A **ride-sharing app** could have separate microservices for rider matching, payment processing, and ride tracking.

## What does Single Point of Failure mean?

A Single Point of Failure (SPOF) is a component of a system which, if it fails, causes the entire system to stop working.

Single Point of Failures are flaws in architecture design that can be mitigated by introducing redundancy for critical components, as well as implementing backups or failover mechanisms.

## Fault tolerance

Fault tolerance refers to the design of a system to tolerate flaws and handle errors in a way that allows it to continue functioning as expected, possibly at a reduced level of performance, rather than experiencing a complete failure. Fault tolerance is essential for systems that require high reliability and availability, as it enables them to continue functioning correctly even when components fail or errors occur.

### Techniques to improve fault tolerance

- **Redundancy:** Replication data or resources across multiple systems and locations to ensure high availaibity and reliability.
- **Fail over:** Switch to backup system or component when the primary system fails.
- **Replication:** Replicate data across multiple databases (database replication) and create multiple instances of the same application (server replication).
- **Checkpointing and Rollback**
- **Error Detection and Correction:** Self-healing system, parity checks and check sums.
- **Load balancing**
- **Decoupling and Isolation**
- **Geographic Distribution**
- **Graceful Degradation:** Designing a system to maintain partial functionality or essential services, even when a majority of it is inoperative or has limited functionality.

## CAP Theorem

CAP Theorem (also known as Brewer's Theorem) states that in the event of a network partition, a distributed system can only guarantee two of the following properties at a given time:

- **Consistency (C):** Every read operation returns the most recent write, or an error.
- **Availabilit (A):** Every request (read or write) to a non-failing node should receive a response, even if the data might not be up-to-date.
- **Partial Intolerance (P):** The system continues to function even though there is a network partition that disruption the communication between nodes of a system.

A system must choose whether it remains available (always responds to requests, possibly with stale data) or consistent (no stale reads). Partition tolerance is considered mandatory in real-world distributed systems.

### Real-world example

Imagine a system with three ATM machines connected to a bank database, where one or more ATMs experience total or partial failure due to network or hardware issues. A customer tries to withdraw 120 dollars from their account, which has a balance of 1000 dollars.

The system must decide what to prioritize:
- To maintain **consistency**, the system may prevent withdrawals to ensure the data remains the same until all ATMs are synchronized.
- To maintain **availability**, the system may allow the withdrawal to proceed even if some ATMs are temporarily out of sync, ensuring that the customer receives a response, but potentially showing outdated balances.

## What does Graceful shutdown mean?

A graceful shutdown (also known as a graceful exit) describe the process of shutting down a system in a controlled manner, ensuring that all ongoing operations are completed or safely interrupted. This minimizes data loss, corruption, or service disruptions. It typically includes closing database connections, performing clean-up tasks, and finalizing requests.

The advantages of a graceful shutdown includes:
- Minimizing data loss, corruption, or service disruptions
- Better user experience
- Improved reliablity and availability of the system

### Example of handing graceful shutdowns wwith Node.js

Handling graceful shutdowns can be done by listening for termination signals such as `SIGINT` or `SIGTERM`.

```javascript
const express = require('express');
const app = express();
const HOST_NAME = '0.0.0.0';
const POST_NUMBER = 3000;

app.get('/', (req, res) => {
    res.send('testing');
});

const server = app.listen(POST_NUMBER, HOST_NAME, () => {
    console.log(`Server running at http://${HOST_NAME}:${POST_NUMBER}/`);
});

process.on('SIGINT', () => {
    server.close(() => {
        console.log('closed server');
    })
});
```

### Further reading(s)

https://www.geeksforgeeks.org/graceful-shutdown-in-distributed-systems-and-microservices/

## Content Delivery Network (CDN)

Content Delivery Network (CDN) is a distributed network of servers located geographically close to clients. These servers cache and deliver content (such as images, videos, scripts, and other static files) to users, reducing latency and improving website performance.

There are two types of CDNs: Push CDNs and Pull CDNs.
- **Push CDNs:** In a Push CDN, resources are proactively uploaded to the CDN servers from the original web server. The URLs for the resources must be updated to point to the files stored on the CDN. Push CDNs are best suited for resources that change infrequently and are less commonly used for dynamic content due to the manual effort required for updates.
- **Pull CDNs:** In a Pull CDN, resources remain stored on the original web server, and the CDN fetches (or "pulls") the resources when users request them. The CDN then caches the fetched resources for future requests. Pull CDNs do not require manual uploads, making them more suitable for websites with dynamic or frequently updated content, as they automatically stay in sync with the original server.

## Eventual vs immediate consistency

**Eventual consistency** in distributed systems is a consistency model that ensures high availability by allowing temporary discrepancies in data visibility across nodes. The system guarantees that, given enough time without new updates, all replicas will eventually converge to the same state. This model is suitable when the most current data does not need to be immediately visible to the client.

**Immediate consistency** is a consistency model that ensures changes are immediately visible to all clients across the system. This requires all updates to be propagated to all replicas before any client can see the change, introducing higher latency and reduced availability compared to eventual consistency.

## What is the difference between load testing and stress testing of an application?

Load tests checks system with expected load conditions to see how well it performs under average or slightly above-average usage. Stress tests apply extreme load to your system to identify the point at which it fails due to high traffic and heavy usage.

## What is a relational database?

A relational database is a type of database that organizes data into tables with rows and columns, where the entities can be related to one another through relationships, often using primary and foreign keys.

Examples of relational databases include:
- PostgreSQL
- SQLite
- MySQL
- MariaDB (a fork of MySQL)

## Cache

A cache is a temporary storage used to store expensive responses or frequently access resources to minimize latency and throughput.

### Cache policy

A cache policy is an algorithm used to manage cache memory with the aim of minimizing latency and maintaining data consistency.

Cache policy categories consist of "Cache Eviction (Replacement) Policies" and "Cache Write Policies".

#### Cache Eviction (Replacement) Policies

- **LRU (Least Recently Used):** removes the items that has not been accessed for the longest time.
- **LFU (Least Frequently Used):** removes the item with the lowest access frequency.
- **FIFO (First In, First Out):** removes the oldest item added to the cache, regardless of how recent or often it has been accessed.
- **TTL (Time-to-Live):** evicts an item from the cache once it reaches end of its lifespan.
- **Random Replacement (RR):** randomly picks an item to remove, which can outperform LRU in specific scenarios.

#### Cache Write Policies
- **Cache-Aside (lazy-loading):** the application writes data to the cache on demand.  The application directly manages data interaction with both the cache and the database. Very flexible and popular for read-heavy systems.
- **Write-Through:** data is written to both cache and database simultaneously, ensuring consistency but slowing writes.
- **Read-Through:** application treats the cache as the main datastore, allowing the cache to automatically handle loading data from the database upon a cache miss.
- **Write-Back:** writes to cache first, then asynchronously to the database. Offers high performance but risks data loss.

#### Further Reading
- https://www.geeksforgeeks.org/system-design/cache-aside-pattern/

## Containerization and Virtual Machines
Containerization is a method of packaging an application, including its dependencies (such as libraries, frameworks and tools), into a lightweight, portable unit that can run consistently across environments. Containers provide isolation to reduce the impact on the host machine, while still utilizing the host's kernel and resources.

Virtual machines encapsulate an instance of an operating system, sharing the physical hardware and resources of the host machine through a hypervisor. While VMs provide strong isolation between systems, they still consume the host machine's physical resources. Unlike containers, which virtualize the operating system, VMs virtualize the underlying hardware.

### Benefits of containers and VMs
Containers are ideal for ensuring that applications run consistently across different environments. They allow developers to replicate development environments reliably, minimizing the risk of inconsistencies between development and production.

Virtual machines provide stronger security that containers through full isolation of operating systems, making them suitable for scenarios requiring higher security. However, they are generally heavier than containers in terms of resource usage.

### Further reading(s)
- [What is a virtual machine?](https://cloud.google.com/learn/what-is-a-virtual-machine)
- [Are virtual machines safe for end users?](https://www.techtarget.com/searchvirtualdesktop/answer/Are-virtual-machines-safe-for-end-users#:~:text=While%20VMs%20have%20certain%20security,to%20maintain%20vigilance%20regarding%20cybersecurity.)

## Kubernetes

Kubernetes is an orchestration platform for containers. It manages the deployments, scaling, and operations of containerized applications across a cluster of nodes.

### Key components of Kubernetes
- **Control panel:** Consists of several components to manage the Kubernetes cluster, including the kube-apiserver, etcd, kube-scheduler, controller-manager, and often the cloud-controller-manager. 
  - **etcd:** a distributed key-value store for storing the entire cluster's state, including configuration data, metadata, and secrets.
  - **API server (`kube-apiserver`):** It exposes the Kubernetes API, acting as a communication hub for all components. It also interacts with etcd to retrieve and store cluster state.
  - **Scheduler (`kube-scheduler`):** Assigns pods to nodes based on resource availability and scheduling policies.
  - **Controller Manager (`kube-controller-manager`):** Runs controllers to manage the state of the cluster, such as replication and endpoint controllers.
- **Worker node:**  A worker node is a machine (virtual or physical) in the Kubernetes cluster that runs containerized applications. It includes components such as the container runtime (e.g., Docker, containerd), kubelet, and kube-proxy.
  - **Pod:** Pods run on worker nodes and it represents a single instance of a running process in the cluster and can contain one or more tightly coupled containers that share the same network namespace and storage.
  - **Kubelet:** An agent that runs on each node to ensure that the containers are running in a pod. It communicates with the API server to receive instructions and report back the status of the node
  - **kube-proxy:** A network proxy and load balancer that routes traffic to the appropriate pods in a service. It manages networking rules on worker nodes to ensure communication between services, pods, and external clients.

### Further readings(s)
- [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/)
- [etcd in Kubernetes](https://www.armosec.io/glossary/etcd-kubernetes/#:~:text=etcd%20role%20in%20Kubernetes&text=The%20etcd%20stores%20all%20cluster,API%20to%20manage%20the%20clusters.)

## Further resources
- [Designing Data-Intensive Applications The Big Ideas Behind Reliable, Scalable, and Maintainable Systems](https://www.amazon.de/-/en/Designing-Data-Intensive-Applications-Reliable-Maintainable/dp/1449373321)
- [System Design Primer](https://github.com/donnemartin/system-design-primer)
- [Scalability Harvard Web Development](https://youtu.be/-W9F__D3oY4?si=5YY_dLx8k3lf8VTM) by David Malan

## Data Centres

### Multi-Data Centre Replication

Data centre replication is the process of copy data accross multiple data centres located in different geographical locations.  

Benefits includes:
- **Geographic distribution:** data is replicated across multiple geographical locations.
- **High latency:** data is access from the nearest geographical location
- **High availability:** system remains available when one data centre fails.
- **Data synchronization:** changes are propagated across multiple data centres 

### Futher information
- https://youtu.be/9DEi-AcA_Os?si=cRDJ1fiKJ5Uaq431

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

## Message Queues

Message queues are used in distributed systems (e.g. microservices) for asynchronous communicate between the different the components. Producers/publishers create messages and publish them to a queue. Consumers/subscribers connect to the queue and proceses the messages.


### Message signals

In message queues (RabitMQ or Kafka), consumers use signals to communicate the result of a message back to the queue systems.

#### ACK (Acknowledged)
This signal is sent when a message has been successfully processed. It tells the broker that it can safely remove it from the queue and prevents re-delivery.

#### NACK (Negative Acknowledgement)
This signal is sent when a message has failed to process. The broker may then try to requeue the message, move it to a dead-letter queue after a certain number of retries or drop it (in poorly configured systems).

#### REJECT
While similar to NACK, REJECT instructs the consumer whether to discard of requeue an individual message, possibly by use of a flag.

### Important points
- **Dead-lettering:** messages that fail repeatedly after max NACKs will be moved to a dead-letter queue for further inspection and possibly manual requeuing. 
- **Auto-ACK:** The consumer automatically signals that the message is acknowledged as soon as it's delivered. However, this poses the risk of the message being lost if the consumer crashes before delivery.
- **Manual-ACK:** The consumer explicitly signals that the message has been successfully processed. This guarantees at-least-once delivery.
- **At-least-once delivery:** at least one attempt of processing a delivered messaged is successful.

## OAuth

### Resources

- [OAuth 2.0 and OpenID Connect (in plain English)](https://youtu.be/996OiexHze0?si=q3gn7bsBj-PjZIoQ)