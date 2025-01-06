# Network

## HTTP

HTTP stands for Hypertext Transfor Protocol. It is a top-level application protocol that exchanges information between a client (usually a browser) and a local or remote web server.

## TCP

TCP stands for Transmission Control Protocol. TCP ensures that data is reaches its destination and in the correct order, even if the network is busy or there are errors.

TCP/IP (Transmission Control Protocol/Internet Protocol) is a suite of communication protocols. It consists of four primarly layers: Application, Transport, Network and Data Link layers.

## UDP

UDP stands for user datagram Protocol. UDP is a protocol for time-sensitive communication such as Domain Name System (DNS) lookups, playing videos, and gaming.

## When to use TCP and UDP

TCP is ideal for direct communication where a reliable connection is needed, such as web browsing, email, text messaging, and file transfers. UDP is ideal for live and real-time data transmission where speed is more a priority.

While TCP is slower than UDP, it transfers data more reliably.

### How it works
1. The handshake process is initiated between the client and server to agree on how to communicate securely.
2. The client send a message to the server, listing supported encryption methods and protocols.
3. The server responds with its chosen encryption method and provide its SSL/TLS certificate.
4. The client will verify the validity of the certificate and ensure that it was issued by a trusted Certificate Authority (CA).
5. The Client and server exchange cryptographic keys using algorithms such as RSA, creating a shared session key for encryption.
6. The client and server can now securely exchange data over the encrypted channel.

*Handshake is the means of establishing the connection between client and server.*

## Transport Layer Security (TLS)
TLS is a cyptographic protocol used to provide secure communications over a computer network. It is typically used by HTTPS to secure web traffic and allows client and server applications to communicate securely over the Internet.

TLS prevents attackers from stealing sensitive data, verifies server's identity using handshakes, and ensures that transmitted data has not been tampered with. 

## Secure Socket Layer (SSL)
SSL is a standard technology to establish encrypted data transfer between a server and a client (typically a web browser). SSL is used to prevent attackers from stealing sensitive information.

## What is the difference between SSL and TLS?

SSL is older with some security vunerabilities. TLS is the upgraded version of SSL with the security vunerabilities addressed.

### Further reading(s)

[What is an SSL certificate?](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/)

## OSI model

The Open Systems Interconnection (OSI) model describes 7 layers that computer systems use to communicate over a network.

### Layer 7: Application

The application layer is an abstraction layer that allows the user to directly communicate with the network through applications. The application contains communication protocols to allow data exchange. It is also responsible for presenting data in a format that is readable to the user and applications.

Some of protocols used in the application layer include:
- HTTP/HTTPS
- SMTP/IMAP/POP3
- FTP (File Transfer Protocol)
- DNS (Domain Name System)
- Telnet/SSH

The application layer uses the functionalities of the presentation and session layer to provide seamless communication between the user and the network.

### Layer 6: Presentation

The presentation layer is responsible for translating data into a format suitable for software applications or network transmission. This layer handles tasks such as encryption and decryption, data compression, and data conversion, including encoding formats like ASCII and Unicode. (for example, encoding formats like ASCII and Unicode).

### Layer 5: Session

The session layer manages the communication session between devices and ensures that the session is started, maintained, and ended properly. It also fetches data from the transport layer and send data to the presentation layer.

The session layer supports two types of communication:
- Half-duplex: Data flows in one direction at a time.
- Full-duplex: Data flows in both directions simultaneously.

Some of protocols used in the application layer include:
- NetBIOS (Network Basic Input Output System)
- RPC (Remote Procedure Call Protocol)
- PAP (Password Authentication Protocol)


### Layer 4: Transport

The transport layer is responsible for ensuring that data is reliably and efficiently transmitted between devices across a network.

The key protocols used in this layer are TCP and UDP.

### Layer 5: Network

The network layer is responsible for moving data packets (chunks of data) between different networks. It decides which physical path the data packets will take. The network layer uses network addresses (typically Internet Protocol or IP addresses) to route packets.

Some of the protocols used in network layer include:

- IPv4/IPv6
- IPSec ( Internet Protocol Security)
- IGMP (Internet Group Management Protocol)
- DDP (Datagram Delivery Protocol)
- RIP (Routing Information Protocol)

### Layer 6: Data Link

The data link layer is an second layer and it is responsible for the transfers of datagram between nodes or physical links in a network. It basically hides all the underlying handware complexies or physical layer from the layers above it. Examples of data link protocols are Ethernet, the IEEE 802.11 WiFi protocols, ATM and Frame Relay.

Real-word examples includes the following:

- **Ethernet:**
When your computer sends data over an Ethernet cable, the Data Link layer that data into frames and adds the Media Access Control (MAC) addresses of the sender and receiver. It ensures the data reaches the right device on the local network without errors.
- **Wi-Fi**
In a Wi-Fi network, the Data Link layer controls how different devices share the wireless signal, ensuring only one device transmits at a time to avoid collisions.

*MAC addresses indentifies devices on the same network.* 

Some protocols used in this layer include:
- Ethernet
- IEEE 802.11 WiFi protocols
- ATM (Asynchronous Transfer Mode)
- Frame Relay

### Layer 7: Physical

The physical layer (raw bits) is commonly associated with physical connection between devices such as fiber optic cables, ethernet cables, wireless transmissions, and hubs and repeaters.

### Further reading(s)

- [OSI model](https://en.wikipedia.org/wiki/OSI_model)


## Differences between HTTP and HTTPS

HTTP operates on port 80, where as HTTPS operates on port 443. While HTTP transfers data as plain text, HTTPS transfers data as encrypted text. HTTPS requires a valid SSL certificate issued by a certificate authority (CA). 

## RESTful API

A RESTful API is an application program interface (API) that uses HTTP requests to retrieve and update data via methods. REST stands for Representational state transfer and is a software architectural style for designing network applications.

## gRPC

gRPC is a high performance Remote Procedure Call (RPC) implemented on top of HTTP/2. It allows communication betweens services in and across data centers.

### Further reading(s)

- [Remote procedural call](https://en.wikipedia.org/wiki/Remote_procedure_call)
- [Introduction to gRPC video](https://youtu.be/njC24ts24Pg)

## GraphQL

GraphQL is a query langiage for APIs and a runtime for fulfilling those queries with your existing data. GraphQL allows you to request exactly the data you need and nothing more.


## ETag header

The ETag response header is an identifier for a specific version of a resource. This helps caches to be more efficient and saves bandwidth as the web server does not need to send a full response if the content is unchanged.

### How it works?

Client makes a request to the server

```http
GET /images/logo.png HTTP/1.1
Host: example.com
```

Server sends response with ETag include

```http
HTTP/1.1 200 OK
Host: example.com
ETag: 123456efg
Content-Type: image/png
Content-Length: 1024
```

Client can make conditional request to the server by passing the ETag in the `If-None-Match` header 

```http
GET /images/logo.png HTTP/1.1
Host: example.com
If-None-Match: 123456efg
```

If the resource has not been modified, the server with return status code **304 Not Modified**, indicating that the client can use the cached resource.

## Difference between Latency, Throughput, and Bandwidth

Latency is the time it takes for content transfer from the client to the server and back. Latency is synonymous wth *delay*.

Throughput is the amount of data that can be processed for a given time (for example, the number of http requests a web server can handle per second).

Bandwidth is the maximum data volume of a network. Simply put, it indicates how much data in network can possible travel within a given period of time.

## Race condition

A race condition is an undesirable situation where an attempt is made to perform two or more operations (such as network requests) simultaneously. This typically occurs in multi-threaded or asynchronous environments, where tasks execute concurrently on shared resources.

For example, if two or more services attempt to update the same record in the database simultaneously, one update may overwrite another, leading to data loss or inconsistency.

Another real world example is two people try to withdraw money from the same bank account at the same time. 

### Further reading(s)

[Race condition](https://www.imperva.com/learn/application-security/race-condition/) 

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

## What is a deadlock?

In a computer program, a deadlock can occur when two or more processes are waiting for each other to release resources.

## What does Idempotency mean?

An HTTP method is considered idempotent if it produces the same response regardless of how many identical requests are made.

All safe methods such as `GET` and `HEAD` are idemptonent. `PUT` and `DELETE` are idempotent because, after the first request that modifies or removes the resource, all subsequent requests will result in the same response without further changing the resource.       

`POST` is not idemptonent.

## What is Head-of-Line blocking?

Head-of-Line blocking is an undesirable situation in HTTP/1.1 and HTTP/2 over TCP, where a lost packet in the stream forces the entire stream to wait until the packet is retransmitted and received.