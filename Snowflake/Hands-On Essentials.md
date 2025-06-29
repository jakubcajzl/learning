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
``` sql

## Lesson 4 (Tables, Data Types, and Loading Data)

## Lesson 5 (Worksheets & Warehouses)

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
