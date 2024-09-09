# Write your MySQL query statement below
SELECT manager.id AS employee_id, manager.name,
employee.reports_count, employee.average_age FROM (

    (
        SELECT employee_id AS id, name FROM Employees
    ) manager
    JOIN 
    (
        SELECT reports_to AS manager_id, COUNT(DISTINCT(employee_id)) AS reports_count,
        ROUND(SUM(age)/COUNT(DISTINCT(employee_id))) AS average_age FROM Employees
        WHERE reports_to IS NOT NULL
        GROUP BY reports_to
    ) employee
    ON manager.id = employee.manager_id

)
ORDER BY employee_id