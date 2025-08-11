# SQL tips and tricks

- Rounding correctly the numbers that have very small deviation from a given precision - e.g. rounding 17.249999999 to 17.25 using a 3-decimal rounding:
  ``` SQL
  cast( round(no_ad_hoc_volume + 0.000001, 3) as decimal(20,3) ) as column_01
  ```
  - This is important for example when comparing numbers from different sources - the numbers are compared precisely, therefore even 0.0000001 is a difference that can trigger a difference flag.


# Power BI tips and tricks


# Python tips and tricks


