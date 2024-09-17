# Write your MySQL query statement below
DELETE FROM Person WHERE NOT id IN (
    SELECT id FROM (
    SELECT MIN(p2.id) AS id FROM (
        SELECT email FROM Person
        GROUP BY email
        HAVING COUNT(email)>1
    ) p1
    JOIN Person p2
    ON p1.email = p2.email
    GROUP BY p1.email

    UNION

    SELECT MIN(id) AS id FROM Person
    GROUP BY email
    HAVING COUNT(email) = 1) t1
);