DROP TABLE IF EXISTS students, teachers, subjects;

CREATE TABLE students(
    id serial PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    subject INT
);

CREATE TABLE teachers(
    id serial PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    subject INT
);

CREATE TABLE subjects(
    id serial PRIMARY KEY,
    subject VARCHAR(50)
);


\COPY students FROM '/Users/robert/Documents/Software Engineer/week3/flask_postgres_school/data/student.csv' DELIMITER ',' CSV HEADER;
\COPY teachers FROM '/Users/robert/Documents/Software Engineer/week3/flask_postgres_school/data/teachers.csv' DELIMITER ',' CSV HEADER;
\COPY subjects FROM '/Users/robert/Documents/Software Engineer/week3/flask_postgres_school/data/subjects.csv' DELIMITER ',' CSV HEADER;