# Network

### Question
Explain HTTP.

### Answer
HTTP stands for Hypertext Transfor Protocol. It is a top-level application protocol that exchanges information between a client (usually a browser) and a local or remote web server. 

---

### Question
What are RESTful APIs and how are they used?

### Answer

A RESTful API is an application program interface (API) that uses HTTP requests to retrieve and update data via methods.

REST stands for Representational state transfer and is a software architectural style for designing network applications.

---
### Question
What is the ETag header and how is it used?

### Answer

The ETag response header is an identifier for a specific version of a resource. This helps caches to be more efficient and saves bandwidth as the wbe server does not need to send a full response if the content is unchanged.

---

### Question
Explain Latency.

### Answer
Latency is the response time of the content transfer from the client to the server and back.

---
## Question
What is a race condition?

### Answer

A race condition is an undesirable situation an attempt is made to perform two or more operations (network requests) at the same time.

---

### Question
What is CORS?

### Answer

CORS (Cross-origin Resource Sharing) is a mechanism that uses additional HTTP headers to give a web application with a different origin access to a specific resource.

"preflighted" requests first send an HTTP request by the `OPTIONS` method to the resource on the other domain, to determine if the actual request is safe to send and to determine the options and/or requirements associated with a resource.

---
### Question
What does 10x HTTP response status code mean?

### Answer

10x HTTP response codes are used for informational responses.

---
### Question
What does 20x HTTP response status code mean?

### Answer

Responses were successful.

**Common:**
- `200` - Request succeeded.
- `201` - Resource was created.
- `206` - Partial content

---

### Question
What does 30x HTTP response status code mean?

### Answer

30x status codes are reserved for redirects.

**Common:**
- `302` - URI of the request resource has been changed temporarily.
- `307` - client is redirected to another URI to get the requested resource.

---

### Question
What does 40x HTTP response status code mean?
### Answer

40x status codes are reserved for client error responses.

**Common:**
- `400` - Bad request; request body was malformed.
- `401` - Unauthorized or unauthenticated.
- `403` - Forbidden; client does not access rights to the requested resource.
- `404` - Not found
- `409` - Conflict; request conflicts with the current state of the server

---

### Question
What does 50x HTTP response status code mean?

### Answer
50x indicated server error.

**Common:**
- `500` - Internal server error
- `501` - Not implemented
- `502` - Bad gateway
- `503` - Service unavailable
- `504` - Gateway timeout