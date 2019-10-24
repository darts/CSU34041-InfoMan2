Create table, gives new table name and defines columns. Column has: name, type, size, optional integrity contraints. Column defined by: name, data type, NULL value flag. 
Qualified name tables: used to ensure table name is unique, concatenating table name and name of user who created table separating with a dot.
Tables created using CREATE TABLE command.
Domain created using CREATE DOMAIN statement.
DEFAULT value is automatically inserted when no value is specified by INSERT in column. 
The tables in a database determine its structure.
The definition of a database table also includes the relationships among the tables in a database and includes restrictions on the data that can be entered into the database
A table will always include the Primary Key constraint
key constraints:
Uniqueness - This constraint forces the data in some column or combination of columns to be unique for every row in a table.
Primary Key - This constraint enforces the same uniqueness constraint but also designates a column or combination of columns as the key for the table.
Foreign Key - This constraint forces the value of a column or combination of columns to match the value of a primary key in some other table.
Specifying a foreign key we must also specify the table(s) in which that foreign key can be found.
Check restricts contents of table in SQL2. Uses in, like, between.
Assertions constraint of whole database content. SQL2 CREATE ASSERTION.
Domain definition, data type column in CREATE TABLE. Domain CREATE DOMAIN.
Primary Key and Foreign Key in CREATE TABLE, combination of attributes.
Change format of table using ALTER TABLE. To increase the maximum width of a CHAR or NUMBER field, use the ALTER TABLE statement with a MODIFY clause: ALTER TABLE S MODIFY S#(6);
DROP TABLE remove no longer useful. DROP TABLE Airport;


100%