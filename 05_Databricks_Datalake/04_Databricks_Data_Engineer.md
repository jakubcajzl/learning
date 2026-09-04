# Databricks Data Engineer (Associate + Professional)

## 01 Data Ingestion with Lakeflow Connect

### Data Engineering in Databricks

Agenda:
1. Describe the purpose and benefits of LakeFlow Connect for scalable data ingestion into Databricks
2. Identify the different types of connectors, including Standard and Managed connectors
3. Explain various data ingestion techniques such as batch, incremental batch, and streaming
4. Select the appropriate ingestion method based on data and use case requirements
5. Review the key benefits of UC tables and the Medallion Architecture for data management and analytics

**LakeFlow** provides a unified platform for data ingestion, transformation, and orchestration:
- **LakeFlow Connect****** — Efficient ingestion connectors for enterprise applications, databases, cloud storage, message buses, and local files
- **Apache Spark™ Declarative Pipelines** — A framework for building batch and streaming data pipelines using SQL and Python
- **LakeFlow Jobs** — Workflow automation that orchestrates data processing workloads and coordinates multiple tasks within complex workflows

#### Ingestion Methods

- Batch:
  - All data is re-ingested every time the pipeline runs
  - Traditional batch ingestion processes all records each time it runs
  - The SQL statement: CREATE TABLE AS SELECT
  - The Python method: spark.read.load()
- Incremental Batch: 
- Streaming Ingestion: 

