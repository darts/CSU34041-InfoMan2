"Create a table called cs_course_modules with the fields module_name (variable char of length 50), module_id (variable char of length 10), etc (Number), and lecture_hours (Number). All fields must not be null and the module_id must be the primary key."  
**CREATE TABLE cs_course_modules (module_name varchar(50) NOT NULL, module_id varchar(10) NOT NULL PRIMARY KEY, etc int NOT NULL, lecture_hours int NOT NULL);**  


"Alter the cs_course_modules table adding an extra field: semester_taught, which is of type variable char of length 15 and not null."  
**ALTER TABLE cs_course_modules ADD semester_taught VARCHAR(15) NOT NULL;**  


"Drop the cs_course_modules table"  
**DROP TABLE cs_course_modules;**