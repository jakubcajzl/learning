# Badge 1: Data Warehousing Workshop

## Lesson 2 (Identity and Access)
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
- Each USER has a DEFAULT ROLE role assigned, e.g. ACCOUNTADMIN - this can be changed - also, when you log out and log back in, your role will revert to the default
- Ownership of items can be transfered - e.g. ownership of Database can be done in (left side) Data -> Databases and right upper corner three dots -> Transfer ownership
- **Data** is **stored** in **databases** and any **processing** of data is done by a **warehouse**
  - Processing units called warehouses are under Admin tab

## Lesson 3 (Data Containers)
- Hierarchy: Databases -> Schemas -> Tables
- To show info about **databases** run: _show databases;_
- To show info about **schemas** run: _show schemas;_ (current selected database) or _show schemas in account;_ (all schemas for current role)

## Lesson 4 (Tables, Data Types, and Loading Data)
- When creating a database, two concepts should be used - Data modeling and Normalization - example:

<img width="800" alt="Screenshot (86)" src="https://github.com/user-attachments/assets/ffde8f2f-686b-40d4-9594-8a06bc8557fb" />

``` SQL
create or replace table ROOT_DEPTH (
   ROOT_DEPTH_ID number(1), 
   ROOT_DEPTH_CODE text(1), 
   ROOT_DEPTH_NAME text(7), 
   UNIT_OF_MEASURE text(2),
   RANGE_MIN number(2),
   RANGE_MAX number(2)
   );
```

- Renaming a table:
``` sql
alter table garden_plants.veggies.root_size
rename to garden_plants.veggies.root_depth;
```

- Moving a table:
``` sql
alter table garden_plants.veggies.root_size
rename to garden_plants.fruits.root_depth;
```

- Vieving a definition of a table:
![DWW_052](https://github.com/user-attachments/assets/d01a112d-4570-4ccd-b2c4-f08d63382f47)

- Inserting new values into a table - example:
``` sql
insert into root_depth values (1, 'S', 'Shallow', 'cm', 30, 45);

insert into root_depth values
    (1, 'S', 'Shallow', 'cm', 30, 45),
    (2, 'M', 'Medium', 'cm', 45, 60),
    (3, 'D', 'Deep', 'cm', 60, 90)
    ;
```

- Changing values in a table:
``` sql
update root_depth
    set root_depth_id = 2
    where root_depth_code = 'M'
    ;
```

- Deleting a row of a table:
``` sql
delete from root_depth where root_depth_id = 9;
```

- Deleting all the rows from a table:
``` sql
truncate table root_depth;
```

## Lesson 5 (Worksheets & Warehouses)
- Data mart = a subset of a data warehouse, focused on a specific business area (e.g. Sales Data Mart, Finance Data Mart, Customer Service Data Mart, etc.)
- 3NF (Third Normal Form) = a normal form used in relational database design to reduce data redundancy and ensure data integrity. It's part of the normalization process, which organizes data into related tables to avoid anomalies in insert, update, or delete operations.
  - A table is in 3NF if:
    1. It is in 2NF (i.e., no partial dependency on a composite key)
    2. No transitive dependencies — i.e., non-key columns depend only on the primary key, not on other non-key columns
  - Example:
    - **Not in 3NF:** ``` Employee (EmployeeID, Name, DepartmentID, DepartmentName) ```
      - Here, DepartmentName depends on DepartmentID, which is not a primary key — this is a transitive dependency
    - **In 3NF:** ``` Employee (EmployeeID, Name, DepartmentID) ```, ``` Department (DepartmentID, DepartmentName) ```
      - Now, everything depends only on its own table's primary key — no transitive dependencies.
- Dimensional Modelling and Star Schemas:

<img width="800" alt="Screenshot (86)" src="https://res.cloudinary.com/endjin/image/upload/f_auto/q_80/assets/images/blog/2023/11/schema-spectrum-de-noralised-star-schema-normalised.png" />

- **Scaling In** and **Scaling Out** means _automatically_ adding and reducing number of computing clusters = Multi-Cluster **Elastic** Data Warehousing
- **Scaling Up** and **Scaling Down** means _manually_ changing the size of the cluster (e.g. from XS to M)
- A cluster just means a "group" of servers
- In Snowflake all computing **warehouses** (XS, M, L, ...) have **1 cluster**, but a cluster have different number of servers for each warehouse type
- How to control costs? Set up a **Resource Monitor**:
![DWW_059](https://github.com/user-attachments/assets/16c07e6f-2d4b-41fc-8d57-8d930cef8194)



## Lesson 6 (Meet DORA!)

## Lesson 7 (The Load Data Wizard)

## Lesson 8 (Notebooks and Forms)

## Lesson 9 (Staging Data)

## Lesson 10:( Data Storage Structures)

## Lesson 11:( Intro to Semi-Structured Data)

## Lesson 12:( Nested Semi-Structured Data)


## SQL
- Naming a column can be done literally using double quotes, e.g.:
``` sql
select 'hello' as "Greeting";
```

- Run always executes all the code (from a previous semicolon) up to a (next) semicolon
