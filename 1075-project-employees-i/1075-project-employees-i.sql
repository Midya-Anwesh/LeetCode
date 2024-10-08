# Write your MySQL query statement below
SELECT project_id, ROUND(SUM(Employee.experience_years)/COUNT(Employee.employee_id), 2) AS average_years FROM Project
LEFT JOIN Employee
ON Project.employee_id = Employee.employee_id
GROUP BY Project.project_id;