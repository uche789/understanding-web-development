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

TBP

## Fault tolerance

TBP

## Load balancing

TBP

### Example with nginx