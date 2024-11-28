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

### Further reading(s)
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

### Load balancing using Nginx and Docker

This is the file structure:

```
my-app/
│
├── docker-compose.yml
├── Dockerfile
├── server.js
└── nginx/
    └── default.conf
```

Create a `server.js` file:

```javascript
const express = require('express');
const app = express();
const HOST_NAME = '0.0.0.0';
const POST_NUMBER = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.send('testing');
});

app.listen(POST_NUMBER, HOST_NAME, () => {
    console.log(`Server running at http://${HOST_NAME}:${POST_NUMBER}/`);
});
```

Create `Dockerfile`:

```Dockerfile
# Use an official Node.js image as a base
FROM node:21

# Set the working directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies (if any, for this example, none are needed)
RUN npm install

# Copy the application code
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Command to run the application
CMD ["node", "server.js"]
```

Create `docker-compose.yml` file:

```yml
services:
  node_app:
    build:
      context: .
      dockerfile: Dockerfile
    # container_name: node-app
    expose:
      - "3000"  # Expose port 3000 to other services but not to the host
    networks:
      - loadbalancing
    deploy:
      replicas: 3  # Run 3 instances of the node_app

  nginx:
    image: nginx:latest
    container_name: nginx
    volumes:
      - ./nginx/default.conf:/etc/nginx/conf.d/default.conf  # Mount the Nginx config file
    ports:
      - "80:80"  # Expose Nginx to the host on port 80
    depends_on:
      - node_app  # Ensure Node.js starts before Nginx
    networks:
      - loadbalancing # Creates a custom network

networks:
  loadbalancing:
    driver: bridge
```

Create `nginx/default.conf` file:

```
upstream node_app {
    server node_app:3000;
}

server {
    listen 80;
    
    location / {
        # proxy_pass http://node_app:3000;  # Forward requests to the Node.js container

        proxy_pass http://node_app;

        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

Run the following commands to build and remove containers:

```bash
# Build the Docker images and start the containers:
docker-compose up --build

# Remove the containers after stopping them
docker-compose down
```


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

TBP

### Push CDN vs Pull CDN

TBP

## ACID  (atomicity, consistency, isolation, durability)

TBP