# Big Data

## Types of Big data

- **Human-generated data**:
  - Social media posts
  - Emails
  - Spreadsheets
  - Prezentations
  - Audio and Video files
- **Machine-generated data**:
  - Sensors (vehicles, appliances, industry)
  - Security cameras
  - Satellites
  - Medical devices
  - Smart devices (smatphones, fitness trackers, etc.)
- **Organization-generated data**:
  - Purchase records = **Transactional data** (Customer ID, Item No., Datetime, Quantity, Price, etc.) - Sales Transactions, Purchase Orders, Financial Transactions, Customer Interactions (customer service interactions, returns, and feedback), Logistics and Supply Chain Transactions


## What does it mean "Big" data?

- Usually **defined** by **3 V's**:
  - **`Volume`:** the **amount** of **data** generated that needs to be processed and stored
  - **`Variety`:** different **types** of **data** that are generated
  - **`Velocity`:** the **amount** of data generated **per unit of time**, i.e. the **speed** at which the data is generated
  - Other 2 V's are: 
    - **`Veracity`:** **trustworthiness, accuracy, and quality** of the **data** (clean, reliable, consistent and representative data)
    - **`Value`:** potential business or economic benefit from the data, i.e. the **value of the data** for the business in order to extract meaningful and actionable insights from data


## Data types of Big data

- **`Structured`:** conforms to a **schema** or **format**; clearly organized in rows and columns with keys and indexes
- **`Semi-structured`:** has **some level** of **organization**, e.g. HTML code, where data on the internet page (text, images, tables, etc.) are structured into the code
- **`Unstructured`:** does **not fit** any **schema** or **format**. Today almost **90%** of all data are **unstructured**. Example: purchases recorded by **images** that need to be transformed and loaded into structured database. 


## Batch and Streaming data

**Batch data:**
- Data that we have in **storage** that 
- **Processed** at **once**, i.e. in a **batch**
- Used for **periodic reporting**

**Streaming data:**
- Data that are being **continuously produced** by one or more **sources**
- Must be **processed incrementally** (example: heartbeat monitor)
- Used for **real-time reporting** (e.g. fraud detection in card transactions)

- **Lakehouse** allows both **Batch** and **Streaming** **data**


## Data storage systems

- **Data Warehouses:**
  - Pros:
    - **Reliable**
    - **Structured** data
    - **Easy** to **query**
  - Cons:
    - **Hard** to **scale** up or down (Scalability)
    - **Don't** work with **unstructured** data
    - **Vendor lock-in** (usually licensed database systems)
    - **Expensive** for **big data** (to build, license and maintain)

- **Data Lakes:**
  - Pros:
    - **Structured** and **Unstructured** data
    - Easier to **scale**
    - **Cheap** (usually as a **cloud** storage)
    - Separated costs - **storage** and **computing**
  - Cons:
    - Sometimes too **complex**
    - **Slow** query **speeds**

- **Data Lakehouses:**
  - Best of both worlds: `Data Lakehouse = Data Warehouse + Data Lake`
  - **Single source** of **truth** for data
  - **Schema enforcement** and **governance**
  - **Scalable**
  - **Collaborative**


## Working with Big data

**Big data** are primarily used for these **fields**:

- **Data Science:**
  - Field that combines **Math**, **Statistics**, **Computer Science** and **Business**
  - Gives **insights** into **business data** and more
  - Data Science is **extracting knowledge and insights** from **structured** and **unstructured** data using **scientific methods**
  - Usually has these stages:
    - Data Collection and Preparation
    - Data Analysis
    - Modeling
    - Optimization and Decision Making
    - Deployment into production and Monitoring
- **Artificial Intelligence (AI):**
  - Subgroup of Data Science
  - **Tasks** that would typically require **human intelligence**
  - Arching term for many subgroups like Machine learning and Neural networks
- **Machine Learning (ML):**
  - Subgroup of AI
  - Uses algorithms to **learn** from data and make **predictions** or **decisions**
  - Variety of techniques: regression, classification, clustering, reinforcement learning, etc.
  - Divided into **Supervised** and **Unsupervised learning**
- **Deep Learning (DL):**
  - Subgroup of ML (Machine Learning)
  - Uses deep **neural networks** - composed of multiple layers of interconnected nodes (**neurons**)
  - Can automatically **learn features** and **representations** from data
  - Tasks: **image and speech recognition**, **natural language processing** (NLP), etc.
  - Uses typically **large datasets** to **train**


## Data Science Workflow

**Cyclical process** of identifying **business problems** and delivering **business solutions**:

1. **Identifying business needs:**
     - First is usually **set of questions** about the **business needs** (product prices, customer churn, etc.)
2. **Ingesting data:**
     - Organization **load the data** - e.g. **real-time data** about transaction or **batch data** from database or CSV, etc.
3. **Preparing data:**
     - **Data cleaning and filtering** for the next step which is Modelling
4. **Analyzing data:**
     - Finding **insights** in the data
     - Usually Data science techniques involving **Statistics**
5. **Creating models**
     - Usually **ML or DL models**
6. **Sharing results:**
     - Sharing the **results of the analysis** with the **shareholders** or stakeholders or company managers
     - Usually in the form of **BI dashboards** (Power BI, Python, Tableau, etc.)


## Roles of Data Science Team

- **Platform Administrators:**
  - Reponsible for **managing** and supporting **data infrastructure**
- **Data Engineers:**
  - Develop, construct, test and maintain **data pipelines**
  - Usually need programming languages like Python, Scala or bash terminal commands
  - For big data they usually use **Spark platform**: the core implementation language of Spark is **Scala**, which is a language that runs on the Java Virtual Machine (**JVM**) and therefore enables interoperability with **Java**, however Spark provides APIs in several languages to allow users to write applications in these languages (**Python**, **SQL**, **R**)
- **Data Analysts:**
  - Extract **insights** from data prepared by Data Engineers
  - Data analysts usually use: **SQL**, **Visualization** (Power BI, Tableau, etc.)
- **Data Scientists:**
  - Create models for prediction of various outcomes (e.g. risks, churns, etc.)
  - Data scientists usually use: **SQL**, **Python**, R, **Machine-learning libraries**, **Notebooks** (Jupyter, Databricks, etc.), **ML experiments** logging and tracking (e.g. ML Flow)


## Business Decision-Making

In order to make good business decisions we need to:
- **Understand our customers better:**
  - Who are our customers?
  - What they like?
  - How they use our products?
- **Improve our products:**
  - Do we need to make changes to our products?
  - What types of changes we should make?
  - What do people like the most about our products?
- **Protect our business:**
  - Are we investing money in correct things?
  - Will the risks we take make us money?
- **Stay ahead of the competition:**
  - Who are our biggest competitiors?
  - How to implement latest trends in industry?


## ACID transactions

- **ACID transactions** are a **set of properties** that ensure database transactions are **processed reliably**
- The acronym **ACID** stands for **Atomicity**, **Consistency**, **Isolation**, and **Durability**
- These properties are crucial for maintaining the **integrity of data** in a **database**, especially in systems where **multiple transactions** occur **concurrently**

### ACID Properties

**1. Atomicity**

- **Definition:** Atomicity ensures that each transaction is all-or-nothing. If any part of the transaction fails, the entire transaction fails, and the database state is left unchanged.
- **Example:** In a bank transfer, both the debit from one account and the credit to another account must occur together. If one operation fails, neither should be completed.

**2. Consistency**

- **Definition:** Consistency ensures that a transaction brings the database from one valid state to another, maintaining database rules such as constraints, cascades, and triggers.
- **Example:** If a transaction violates a database constraint (like a foreign key constraint), the transaction will be rolled back, ensuring that only valid data is written to the database.

**3. Isolation**

- **Definition:** Isolation ensures that concurrently executing transactions do not interfere with each other. The intermediate state of a transaction is invisible to other transactions until it is completed.
- **Example:** If two transactions are trying to update the same data, isolation mechanisms (like locking) prevent one transaction from seeing the intermediate changes made by the other.

**4. Durability**

- **Definition:** Durability ensures that once a transaction is committed, it remains so, even in the event of a system failure. This means that committed data will not be lost.
- **Example:** After a banking transaction is committed, even if there is a power failure, the transaction will not be lost, and the data will be safely stored.

### Importance of ACID Transactions

- **Reliability:** Ensures that transactions are completed accurately and reliably, which is critical for applications where data integrity and consistency are paramount.

- **Data Integrity:** Prevents data corruption and maintains the correctness of the database state.

- **Concurrency Control:** Manages the concurrent execution of transactions to ensure data accuracy and consistency.

- **Recovery:** Provides mechanisms for recovery in case of failures, ensuring that the database can be restored to a consistent state.

#### Example Use Cases

- **Banking Systems:** Ensuring accurate and reliable transactions between accounts.

- **E-commerce Platforms:** Maintaining consistency and integrity during order processing and inventory management.

- **Reservation Systems:** Handling concurrent bookings and updates without conflicts.