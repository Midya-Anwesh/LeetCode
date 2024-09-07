# Write your MySQL query statement below
SELECT name FROM
    (SELECT manager.name, COUNT(manager.id) AS direct_reports FROM Employee manager
    JOIN Employee employee ON (employee.managerId IS NOT NULL) AND (manager.id = employee.managerId)
    GROUP BY manager.id) manager_table
WHERE direct_reports >= 5;