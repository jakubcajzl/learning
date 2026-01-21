# SQL tips and tricks

- Rounding numbers that have a very small deviation from a given precision, using addition of a very small decimal number.
  - Example: rounding 17.249999001 to 17.250000 using a 6-decimal rounding:
  ``` SQL
  cast(round(column_01 + 0.000001, 6) as decimal(20,6)) as column_01
  ```
  - This is important for example when comparing numbers from different sources - the numbers are compared precisely, therefore even 0.0000001 is a difference that can trigger a difference flag.

- Rolling dates:
``` SQL
select task_id, start_date, end_date
from tasks
where (end_date - start_date) > INTERVAL 5 DAY
```


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

