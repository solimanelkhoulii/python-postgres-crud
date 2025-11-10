-- SQL script to create the 'students' table and insert initial data

-- 1. Drop table if it exists to allow for clean re-runs
DROP TABLE IF EXISTS students CASCADE;

-- 2. Create the 'students' table with specified schema and constraints
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

-- 3. Insert Initial Data
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

-- Display the inserted data
SELECT * FROM students;