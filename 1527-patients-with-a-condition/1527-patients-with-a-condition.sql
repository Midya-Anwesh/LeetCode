# Write your MySQL query statement below
SELECT * FROM Patients
WHERE REGEXP_LIKE(conditions, "^DIAB1.*") OR REGEXP_LIKE(conditions, "[:space:]DIAB1+")