create database anil32;
use anil32;

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL
);
select * from employees;

INSERT INTO employees (name, salary) VALUES
('John Doe', 50000.00),
('Jane Smith', 60000.00),
('Michael Johnson', 75000.00),
('Emily Brown', 55000.00),
('David Lee', 70000.00);

select * from employees
where salary > 50000;
-- order by salary desc
-- limit 0,3;alter
select * from employees where salary =(
select max(salary) as secondhighest_salary from employees 
where salary < (
select max(salary) from employees));

select * from employees where salary=(
select max(salary) from employees);

SELECT id, name,salary
FROM employees
ORDER BY salary DESC
LIMIT 0,2;
SELECT id, name, salary
FROM (
    SELECT id, name, salary,
           @rank := @rank + 1 AS rank
    FROM employees
    CROSS JOIN (SELECT @rank := 0) AS r
    ORDER BY salary DESC
) AS ranked_employees
WHERE rank = 5;


SELECT id, name, salary
FROM employees
ORDER BY salary DESC
LIMIT 2, 1;

INSERT INTO employees (name, salary) VALUES
('John Doe', 50000.00),
('Jane Smith', 60000.00),
('Michael Johnson', 55000.00),
('Emily Davis', 62000.00),
('Robert Brown', 58000.00),
('Jessica Wilson', 53000.00),
('David Martinez', 57000.00),
('Jennifer Taylor', 61000.00),
('Christopher Anderson', 54000.00),
('Mary Thomas', 59000.00);


select distinct count(salary) from employees;

select * from employees
where name like "Jennifer taylor";


