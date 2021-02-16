CREATE DATABASE students_manager;
use students_manager;

CREATE TABLE students(id int unsigned not null auto_increment, name varchar(100) not null, mark double not null, primary key (id));