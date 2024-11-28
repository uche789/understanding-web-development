# System design

## Client-server architecture

Client-server architecture is a design model where tasks and services are partitioned between resource providers, called servers, and requesters, called clients.

Examples of clients include web browsers and mobile apps. Example of servers include web servers, database servers, and file servers.

Clients and servers typically communicate over a protocol such as gRPC or HTTP.

## What does Single Point of Failure mean?

A Single Point of Failure (SPOF) is a component of a system which, if it fails, causes the entire system to stop working.

Single Point of Failures are flaws in architecture design that can be mitigated by introducing redundancy for critical components, as well as implementing backups or failover mechanisms.

## What is Database normalization?

Database normalization is the process of organizing your data to reduce redundancy and improve data integrity.

For example, a customer table for an ecommerce website is created with a field for customer addresses. Since a customer can have multiple billing and shipping addresses, we will introduce redundancy to the table, resulting in update anomalies. The solution would be to create a separate table for customer addresses.

### Resources
- [Designing Data-Intersive Applications](https://www.amazon.de/-/en/Designing-Data-Intensive-Applications-Reliable-Maintainable/dp/1449373321)
- [System Design Primer](https://github.com/donnemartin/system-design-primer)
- [Scalability Harvard Web Development](https://youtu.be/-W9F__D3oY4?si=5YY_dLx8k3lf8VTM) by David Malan

## Sharding

Sharding is a design pattern for horizontally partitioning data across separate database server instances, known as shards, to enhance scalability and performance.

### Example

TBP

### Further reading(s)
- [Shard (database architecture)](https://en.wikipedia.org/wiki/Shard_(database_architecture))
- [Sharding](https://www.mongodb.com/docs/manual/sharding/#:~:text=Sharding%20is%20a%20method%20for,capacity%20of%20a%20single%20server.)
- [Database Sharding – System Design](https://www.geeksforgeeks.org/database-sharding-a-system-design-concept)

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

## Load balancing

Load balancing is the distribution of incoming network traffic or workload across multiple instances to ensure high availability and maximize uptime. Load balancing not only ensures availability but also optimizes resource utilization and system performance.

Load balancing can be performed at the Transport Layer (Layer 4) and the Application Layer (Layer 7) of the OSI model.

### Layer 4 (Transport Layer) load balancers

Layer 4 load balancing operates based on network information such as IP addresses and TCP/UDP port numbers. It does not inspect the contents of the packets being delivered.

### Layer 7 (Application Layer) load balancers

Layer 7 load balancing operates based on application-level information such as HTTP headers, URLs, or cookies, allowing for more granular traffic distribution based on content.

### Load balancer techniques

- **Round robin:** distribute traffic to a list of servers in a rotation.
- **Weighted round:** distribute more traffic to servers with higher weights or higher traffic capacity.
- **Least connections:** direct traffic to servers with the least active connections.
- **IP Hash:** use a hash of the client's IP to determine which server will receive the request. This ensure that a server is consistently assigned to a given client.
- **Random:** randomly direct traffic to servers of equal capacity.
- **Geolocation-Based:** direct traffic to servers closer to the client to improve latency and user experience.
- **URL Hashing:** direct traffic to a server based on the hash of a URL.
- **Adaptive Load Balancing:** distribute workload based on system performance metrics such as CPU usage, memory or latency.
- **Consistent Hashing:** Often used in distributed caching systems, requests are mapped to servers in a way that minimizes disruptions when a server is added or removed.

### Example with nginx

TBP