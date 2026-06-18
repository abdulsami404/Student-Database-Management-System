create database student_db;
use student_db;
select * from students;
select * from courses;
select * from teachers;

truncate students;

select * from students where age < 17;

select count(name) from students where course = 'neuroscience';

select course,count(name) from students group by course;

select course,count(name) as c from students group by course having c<2;
alter table students add column attendance int;

drop table students;
drop table courses;
drop table enrollment;
drop table grades;
