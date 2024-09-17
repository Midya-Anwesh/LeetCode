# Write your MySQL query statement below
SELECT (CASE WHEN id < (SELECT COUNT(id) FROM Seat) THEN id+1
        WHEN id >= (SELECT COUNT(id) FROM Seat) THEN id
        END) AS id, student FROM Seat
        WHERE id % 2

UNION
SELECT id-1 AS id, student FROM Seat
WHERE id%2=0

ORDER BY id