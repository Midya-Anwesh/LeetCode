# Write your MySQL query statement below
SELECT person_name FROM (
    SELECT Q1.turn, (
        SELECT SUM(weight) FROM Queue Q2
        WHERE Q2.turn <= Q1.turn
    ) AS total_weight FROM Queue Q1
    ORDER BY Q1.turn
) Q3
JOIN Queue Q4
ON Q3.turn = Q4.turn
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1
