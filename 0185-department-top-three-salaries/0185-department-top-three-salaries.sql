# Write your MySQL query statement below
SELECT Department, Employee, Salary FROM (
    SELECT Department.name AS "Department", e1.name AS "Employee", e1.salary AS "Salary", DENSE_RANK() OVER (
        PARTITION BY departmentId ORDER BY salary DESC
    ) AS salary_rank FROM Employee e1
    JOIN Department 
    ON Department.id = e1.departmentId
) derived1 WHERE salary_rank <= 3