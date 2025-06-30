# Apache **Spark SQL API**

The **Spark SQL API** allows to perform various **operations** using **SQL syntax**, making it easy to **query structured data**. Here are some more examples demonstrating different functionalities of **Spark SQL**:

## Initial Setup
First, let's set up the Spark session and create a DataFrame from a sample dataset:

```python
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("SparkSQLExamples").getOrCreate()

# Sample data
data = [("Alice", 29), ("Bob", 35), ("Catherine", 45), ("David", 25), ("Eva", 32)]
columns = ["Name", "Age"]

# Create DataFrame
df = spark.createDataFrame(data, schema=columns)

# Register the DataFrame as a SQL temporary view
df.createOrReplaceTempView("people")
```

## Basic SQL Queries

1. **Simple Select Query**:
   ```python
   result = spark.sql("SELECT * FROM people")
   result.show()
   ```

2. **Filter Data**:
   ```python
   result = spark.sql("SELECT Name, Age FROM people WHERE Age > 30")
   result.show()
   ```

3. **Aggregation**:
   ```python
   result = spark.sql("SELECT AVG(Age) as Avg_Age FROM people")
   result.show()
   ```

4. **Group By**:
   ```python
   result = spark.sql("SELECT Age, COUNT(*) as Count FROM people GROUP BY Age")
   result.show()
   ```

## Advanced SQL Queries

5. **Join Operations**:
   Let's create another DataFrame for demonstration:
   ```python
   data2 = [("Alice", "HR"), ("Bob", "Engineering"), ("Catherine", "Finance"), ("Eva", "Marketing")]
   columns2 = ["Name", "Department"]
   df2 = spark.createDataFrame(data2, schema=columns2)
   df2.createOrReplaceTempView("employees")

   result = spark.sql("""
       SELECT p.Name, p.Age, e.Department
       FROM people p
       JOIN employees e
       ON p.Name = e.Name
   """)

   result.show()
   ```

6. **Window Functions**:
   ```python
   result = spark.sql("""
       SELECT Name, Age, 
              ROW_NUMBER() OVER (ORDER BY Age DESC) as Row_Num
       FROM people
   """)

   result.show()
   ```

7. **Subqueries**:
   ```python
   result = spark.sql("""
       SELECT Name, Age
       FROM people
       WHERE Age > (SELECT AVG(Age) FROM people)
   """)

   result.show()
   ```

8. **Case Statements**:
   ```python
   result = spark.sql("""
       SELECT Name, Age,
              CASE 
                  WHEN Age < 30 THEN 'Young'
                  WHEN Age BETWEEN 30 AND 40 THEN 'Middle-aged'
                  ELSE 'Old'
              END as Age_Group
       FROM people
   """)

   result.show()
   ```

## Creating and Using Databases and Tables

9. **Create Database**:
   ```python
   spark.sql("CREATE DATABASE IF NOT EXISTS test_db")
   ```

10. **Create Table**:
    ```python
    spark.sql("USE test_db")
    spark.sql("CREATE TABLE IF NOT EXISTS people_table (Name STRING, Age INT)")
    spark.sql("INSERT INTO people_table VALUES ('Alice', 29), ('Bob', 35)")
    
    result = spark.sql("SELECT * FROM people_table")
    result.show()
    ```

## Temporary Views and Global Temporary Views

11. **Temporary View**:
    ```python
    df.createOrReplaceTempView("temp_people")
    
    result = spark.sql("SELECT * FROM temp_people WHERE Age < 35")
    result.show()
    ```

12. **Global Temporary View**:
    ```python
    df.createOrReplaceGlobalTempView("global_people")
    
    result = spark.sql("SELECT * FROM global_temp.global_people WHERE Age < 35")
    result.show()
    ```

## Using SQL Functions

13. **Built-in Functions**:
    ```python
    from pyspark.sql.functions import col

    df = df.withColumn("Age_Squared", col("Age") ** 2)
    df.createOrReplaceTempView("people")

    result = spark.sql("SELECT Name, Age, Age_Squared FROM people")
    result.show()
    ```

14. **User-Defined Functions (UDFs)**:
    ```python
    from pyspark.sql.functions import udf
    from pyspark.sql.types import StringType

    def age_group(age):
        if age < 30:
            return "Young"
        elif 30 <= age <= 40:
            return "Middle-aged"
        else:
            return "Old"

    age_group_udf = udf(age_group, StringType())
    spark.udf.register("age_group", age_group_udf)

    result = spark.sql("SELECT Name, Age, age_group(Age) as Age_Group FROM people")
    result.show()
    ```
