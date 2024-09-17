# Write your MySQL query statement below
SELECT *, ROUND(amount/7, 2) AS average_amount FROM (
    SELECT DISTINCT(visited_on) AS visited_on, (
        SELECT SUM(amount) FROM Customer c1
        WHERE c1.visited_on <= c2.visited_on AND DATEDIFF(c2.visited_on, c1.visited_on) <= 6
    ) AS amount FROM Customer c2
    WHERE visited_on >= (SELECT MIN(visited_on) FROM Customer)+6
) AS derived1