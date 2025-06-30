# Hive and Impala

## General information:
- Hive and Impala uses SQL queries
- Impala uses Hive metadata
- Impala is faster than Hive (in most cases) - used for analytical queries
- Tables are by default in HDFS
- Beeline = a tool for connecting to Hive
- We have the main database security by Kerberos system
- We have physically 4 servers in 8. floor – one of them is running Cloudera

## Hive
- Hive is a computing infrastructure similar to the Data Warehouse that provides query and aggregation services for big data stored on a distributed file system such as HDFS
- Hive uses **HiveQL query language** = **SQL-based** (ANSI-92 standard) query language
- SQL query written in **HiveQL** is transformed into a **MapReduce job** and submitted to **JobTracker** for execution

<img src="https://images.datacamp.com/image/upload/v1646397248/image7_ef8a6b.png" alt="Hive overview" width="400"/>

## Impala
- The Impala framework is an **interactive SQL query engine** that allows direct access to data stored in HDFS (or Apache HBase or AWS S3)
- Impala **relies on** other technologies and components from Hive such as its SQL syntax (**HiveSQL**), the **OBCD** (Open DataBase Connectivity driver), and **Query UI**.