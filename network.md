# Network

## HTTP

HTTP stands for Hypertext Transfor Protocol. It is a top-level application protocol that exchanges information between a client (usually a browser) and a local or remote web server.

## TCP

TCP stands for Transmission Control Protocol. TCP ensures that data is reaches its destination and in the correct order, even if the network is busy or there are errors.

TCP/IP (Transmission Control Protocol/Internet Protocol) is a suite of communication protocols. It consists of four primarly layers: Application, Transport, Network and Data Link layers.

## UDP

UDP stands for user datagram Protocol.

## When to use TCP and UDP

TCP is ideal for direct communication where a reliable connection is needed, such as web browsing, email, text messaging, and file transfers. UDP is ideal for live and real-time data transmission where speed is more a priority.

## OSI model

The Open Systems Interconnection (OSI) model describes 7 layers that computer systems use to communicate over a network.

These are the seven layers:

### 1. Application Layer

The application layer is an abstract layer that ensure effective communication. 

### 2. Presentation

TBP

### 4. Session

TBP

### 3. Transport Layer

TBP 

### 4. Network

TBP 

### 6. Data Link

The Data Link layer is an second layer and it is responsible for the transfers of datagram between nodes or physical links in a network. It basically hides all the underlying handware complexies or physical layer from the layers above it. Examples of data link protocols are Ethernet, the IEEE 802.11 WiFi protocols, ATM and Frame Relay.

Real-word examples includes the following:

- **Ethernet:**
When your computer sends data over an Ethernet cable, the Data Link layer that data into frames and adds the Media Access Control (MAC) addresses of the sender and receiver. It ensures the data reaches the right device on the local network without errors.
- **Wi-Fi**
In a Wi-Fi network, the Data Link layer controls how different devices share the wireless signal, ensuring only one device transmits at a time to avoid collisions.

*MAC addresses indentifies devices on the same network.* 

### 7. Physical

The physical layer (raw bits) is the first layer and it is commonly associated with physical connection between devices such as fiber optic cables, ethernet cables, wireless transmissions, and hubs and repeaters.

## Client-server architecture

TBP

## Differences between HTTP and HTTPS

HTTP operates on port 80, where as HTTPS operates on port 443. While HTTP transfers data as plain text, HTTPS transfers data as encrypted text. HTTPS requires a valid SSL certificate issued by a certificate authority (CA). 

## RESTful API

A RESTful API is an application program interface (API) that uses HTTP requests to retrieve and update data via methods. REST stands for Representational state transfer and is a software architectural style for designing network applications.

## gRPC

gRPC is a high performance Remote Procedure Call (RPC) that allows communication betweens services in and across data centers.

### References:
- [Remote procedural call](https://en.wikipedia.org/wiki/Remote_procedure_call)
- [Introduction to gRPC video](https://youtu.be/njC24ts24Pg)

## GraphQL

GraphQL is a query langiage for APIs and a runtime for fulfilling those queries with your existing data. GraphQL allows you to request exactly the data you need and nothing more.


## ETag header

The ETag response header is an identifier for a specific version of a resource. This helps caches to be more efficient and saves bandwidth as the web server does not need to send a full response if the content is unchanged.

## Difference between Latency, Throughput, and Bandwidth

Latency is the response time of the content transfer from the client to the server and back.

Throughput is the amount of information that can be handled at a given time (for example, the number of http requests a web server can handle per second).

Bandwidth is the maximum data volume of a network. Simply put, it indicates how much data in network can possible travel within a given period of time.

## Race condition

A race condition is an undesirable situation where an attempt is made to perform two or more operations (such as network requests) simultaneously. This typically occurs in multi-threaded or asynchronous environments, where tasks execute concurrently on shared resources.

For example, if two or more services attempt to update the same record in the database simultaneously, one update may overwrite another, leading to data loss or inconsistency.

Another real world example is two people try to withdraw money from the same bank account at the same time. 

## CORS

CORS (Cross-origin Resource Sharing) is a mechanism that uses additional HTTP headers to give a web application with a different origin access to a specific resource.

"preflighted" requests first send a HTTP request with the `OPTIONS` method to the resource on the other domain, to determine if the actual request is safe to send, and the options and requirements associated with a resource.

The HTTP `Access-Control-Allow-Origin` response header specifies which origins are allowed to access access the response from a server.

The HTTP `Access-Control-Allow-Credentials` header indicates whether credentials should be included in a cross-origin HTTP request.

## HTTP response status codes

[HTTP response](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) status codes indicate whether a specific HTTP request has been successfully completed. 

- `10x` status codes are used for informational responses.
- `20x` status codes are used for successful or partially successful responses.
- `30x` status codes are reserved for redirects.
- `40x` status codes are reserved for client error responses.
- `50x` status codes indicated server error.