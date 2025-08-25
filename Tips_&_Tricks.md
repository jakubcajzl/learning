# SQL tips and tricks

- Rounding numbers that have a very small deviation from a given precision, using addition of a very small decimal number.
  - Example: rounding 17.249999999 to 17.25 using a 3-decimal rounding:
  ``` SQL
  cast(round(column_01 + 0.000001, 3) as decimal(20,3)) as column_01
  ```
  - This is important for example when comparing numbers from different sources - the numbers are compared precisely, therefore even 0.0000001 is a difference that can trigger a difference flag.


# Power BI tips and tricks


# Python tips and tricks


# PySpark tips and tricks:

- Settings tips:
  - spark.shuffle.service.enabled = True
  - spark.sql.adaptive.enabled = True
  - spark.sql.adaptive.skewJoin.enabled = True
  - spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes = 64MB
  - spark.driver.memory = 4g
  - spark.executor.memory = 20g

