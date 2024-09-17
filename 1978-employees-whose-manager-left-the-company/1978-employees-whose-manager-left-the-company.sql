# Write your MySQL query statement below
SELECT employee_id FROM (
    SELECT t1.employee_id, t1.salary, t2.employee_id AS manager_id FROM Employees t1
    LEFT JOIN Employees t2
    ON t1.manager_id = t2.employee_id
    WHERE t1.manager_id IS NOT NULL
)t3
WHERE salary < 30000 AND manager_id IS NULL
ORDER BY employee_id;