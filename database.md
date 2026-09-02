# Database

- [Database engine](#database-engine)
- [Index](#index)
- [What is a NoSql database?](#what-is-a-nosql-database)
- [When should you use NoSQL or a relational database?](#when-should-you-use-nosql-or-a-relational-database)
- [ACID  (atomicity, consistency, isolation, durability)](#acid-(atomicity,-consistency,-isolation,-durability))
  - [Further reading(s)](#further-reading(s))
- [SARGable (Search ARGument ABLE) queries](#sargable-(search-argument-able)-queries)
- [Optimizing database queries](#optimizing-database-queries)
  - [Further reference](#further-reference)
- [Sharding](#sharding)
  - [Example](#example)
  - [Further reading(s)](#further-reading(s))
- [When should you use sharding and replication?](#when-should-you-use-sharding-and-replication)
- [Database normalization](#database-normalization)

## Database engine

## Index

## What is a NoSql database?

NoSQL is a type of database that stores unstructured and semi-structured data in various formats, such as key-value pairs, documents, wide-column stores, or graphs.

Examples of NoSql databases include:
- **MongoDB:** A document-based NoSQL database.
- **CouchDB:** Another document-based NoSQL database that uses JSON for storing data.
- **Redis:** A key-value store known for its in-memory data processing.
- **etcd:** A distributed key-value store commonly used in distributed systems for configuration management and service discovery.

## When should you use NoSQL or a relational database?

A relational database is ideal for the following:
- Structured data, where relationships need to be clearly defined.
- The need to perform complex queries, such as joins across multiple tables.
- Data integrity and validation is a priority (e.g., compliance with ACID principles: Atomicity, Consistency, Isolation, Durability).

A NoSQL database is ideal for the following:
- Unstructured or semi-structured data, such as JSON or hierarchical data.
- Applications requiring high write performance or eventual consistency, such as real-time analytics, caching, or logging.
- Scenarios requiring horizontal scaling to handle massive amounts of data or traffic.

## ACID  (atomicity, consistency, isolation, durability)

ACID represents the four properties that define a database transaction, ensuring data integrity and validity even in the presence of errors, system crashes, or power outages.

- **Atomicity:** Each CRUD statement in a transaction is treated as a single unit; if any statement in the transaction fails to execute, the whole transaction fails, and the database remains unchanged.
- **Consistency:** Transactions are predictable and guarantee that changes transition the database from one valid state to another while maintaining defined rules and constraints. The database transation can only change the affected data in permitted ways. 
- **Isolation:** Concurrent transactions occur in isolation and do not interfere with each other, ensuring the integrity of each transaction.
- **Durability:** Changes successfully executed by transactions are persisted and remain permanent, even in the event of a system failure.

### Further reading(s)

https://en.wikipedia.org/wiki/ACID

## SARGable (Search ARGument ABLE) queries

A query is said to be SARGable if the database engine can leverage indexes for faster execution. 

## Optimizing database queries

- Select only the specific columns you need; avoid using SELECT *.
- Use `LIMIT` to preview the data efficiently.
- Indexing `JOIN` columns can improve performance and speed up the execution process.
- In the `WHERE` clause, use **SARGable** (Search Argument Able) queries to leverage Indexes effectively:
    - Avoid using functions, e.g., `WHERE YEAR(order_date) >= 2009`.
    - Use direct comparisons, e.g., `WHERE order_date >= '2020-09-30'`.
- Create a computed column or a function-based index if supported by the database engine.
- When using wildcards in the WHERE clause, place them at the end of the phrase (LIKE 'abc%') to avoid wide searches.
- Schedule large queries to run during off-peak hours to minimize system load.

Create Indexes on fields frequently used in queries. Indexes allow the database to retrieve data faster and speeds up execution 
performance, expecially in the `WHERE` clause, `JOIN` conditions, `GROUP BY` clause, `ORDER BY` clause, and frequent lookups (such as unique identifiers).

### Further reference

https://www.youtube.com/watch?v=BHwzDmr6d7s

## Sharding

Sharding is a design pattern for horizontally partitioning data across separate database server instances, known as shards, to enhance scalability and performance.

### Example

[Scaling Up SQLite: A Comprehensive Guide to Sharding with Python](https://code.likeagirl.io/scaling-up-sqlite-a-comprehensive-guide-to-sharding-with-python-acf34ee0d634)

### Further reading(s)
- [Shard (database architecture)](https://en.wikipedia.org/wiki/Shard_(database_architecture))
- [Sharding](https://www.mongodb.com/docs/manual/sharding/#:~:text=Sharding%20is%20a%20method%20for,capacity%20of%20a%20single%20server.)
- [Database Sharding – System Design](https://www.geeksforgeeks.org/database-sharding-a-system-design-concept)

## When should you use sharding and replication?

Sharding is ideal for handling large volumes of data while ensuring fast query performance, provided the queries are designed to target specific shards. However, sharding can introduce complexity, such as shard management and cross-shard queries.

On the other hand, replication is better suited for achieving high availability and enhancing the read performance of your database server. Replication does not necessarily improve write performance and can introduce latency for write operations, as changes need to be propagated to all replicas.

## Database normalization

Database normalization is the process of organizing your data to reduce redundancy and improve data integrity.

For example, a customer table for an ecommerce website is created with a field for customer addresses. Since a customer can have multiple billing and shipping addresses, we will introduce redundancy to the table, resulting in update anomalies. The solution would be to create a separate table for customer addresses.