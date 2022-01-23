---
title: An introduction to web service scaling
date: 2022-01-22 02:42:18
tags:
  - system design
categories:
  - system design
---

Designing a system that could serve millions of requests will always be a big challenge. Fortunately, there are multiple solutions to this problem. Depending on how large your system could be, you could utilize these solutions or combine them for a better result.

<!--more-->

> Disclaimer: I learned this knowledge from the book "[System Design Interview: An Insider's Guide](https://www.amazon.ca/System-Design-Interview-insiders-Second/dp/B08CMF2CQF)" by Alex Xu.
>
> This post covers a tiny part of the book. Please read the book for more information.

# Some basic concepts

## What to scale?

A web service is a composite of multiple components. In the most straightforward system, they are:
* Database
* Server
* Client

When we talk about scaling up the web service, we focus on database and server only. We can do nothing from the client side since we cannot force the client to use a specific device to access the web service.

Depending on the nature of your system and/or where the bottleneck is, you could choose which component to scale up to serve more requests.

For example, if your system stores a vast amount of data and accesses them frequently, you may want to scale up the database. However, if your system is heavy on the calculation, then you may want to scale up the server. Of course, you can scale up both components. It is always the price/performance problem.

## Scaling directions

There are 2 ways to scale a system:
* Scale-up: Adding more processing power (CPU, RAM, Storage)
* Scale-out: Adding more servers

You cannot add an unlimited amount of CPU power, RAM, or storage. Adding more server to a system also add new problems like data consistency, choosing the server, concurrency access, etc. They are challenging, but fear not, there are solutions.

# Geting scaled

## Database scaling

A database has 4 basic operations: CREATE-READ-UPDATE-DELETE. For each operation, there are specific ways to scale.

### Database Replication

For example, when you need to read a lot but write sometimes, you can use Database Replication, with one master database and multiple slaves.

![database replication](../out/source/uml/2022/0122/database_replication.png)

### Database sharding

Sharding, or partioning, is another approach to database scaling. You still use multiple database, but different from replication, each database hold a portion of the data. A sharding strategy could be use to determine which data belong to which database.

> For example, you can store all record with odd id to a database, and even id to another.

However, this will introduce some new problems:
* What if all database is used up to it limit, and you need to add a new datbase?
* What if data of a query is allocated to multiple database?
* What if you need to remove a shard, and copy it data to all other operational shard?

> There are other clever ways to scaling the database, suitable for very specific systems. The key is to split and conquer.