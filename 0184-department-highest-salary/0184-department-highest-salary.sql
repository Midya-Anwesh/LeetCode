# Write your MySQL query statement below
SELECT Department, Employee, Salary FROM (
    SELECT Department.name AS "Department", Employee.name AS "Employee", salary AS "Salary",
    DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS custom_rank
    FROM Employee
    JOIN Department
    ON Department.id = Employee.departmentId
) derived WHERE derived.custom_rank = 1