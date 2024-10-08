# Write your MySQL query statement below
SELECT (CASE WHEN id%2 AND id < (SELECT COUNT(id) FROM Seat) THEN id+1
        WHEN id%2 AND id >= (SELECT COUNT(id) FROM Seat) THEN id 
        WHEN id%2=0 THEN id-1
        END)
        AS id, student FROM Seat
ORDER BY id;