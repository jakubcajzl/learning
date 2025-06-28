# Badge 1: Data Warehousing Workshop

## Lesson 2 (Identity and Access):
- Databases are used to group datasets (tables) together
- A second-level organizational grouping, within a database, is called a schema
- Snowflake automatically creates 2 schemas:
  - The INFORMATION_SCHEMA schema holds a collection of views and cannot be deleted (dropped), renamed, or moved
  - The PUBLIC schema is created empty and can be dropped, renamed, or moved at any time
- Identity = Who you are
  - Proving identity = Authentication
  - Usually proven by a combination of Username and Password
- Access = What you are allowed to see or do
  - Proving access = Authorization
  - Usually proven by RBAC role-assignment = Role-Based Access Control (RBAC)
  - RBAC role-assignment = e.g. ACCOUNTADMIN, SYSADMIN, PUBLIC, ...
    - All users have PUBLIC role
    - ACCOUNTADMIN role has all database priviliges
      - ACCOUNTADMIN owns SECURITYADMIN (that owns USERADMIN) and SYSADMIN. This hierarchy is allowed by _RBAC inheritance_.
      - SYSADMIN is developers role for creating (therefore, most used one), while SECURITYADMIN and USERADMIN are for gatekeeping and enforcement, respectively.
      - There is also ORGADMIN role for creating new Snowflake accounts and can edit high-level configuration setttings
  - Discretionary Access Control (DAC) = another Snowflake access model which tells that the creator of database also owns it
- In Snowflake ROLES *own* items and are *awarded* rights and priviliges
