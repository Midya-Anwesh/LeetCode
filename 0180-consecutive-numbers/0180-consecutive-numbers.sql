# Write your MySQL query statement below
SELECT DISTINCT(l3.num) AS ConsecutiveNums FROM
(
(SELECT l2.id, l1.num FROM Logs l1
JOIN Logs l2
ON l1.id = l2.id-1 AND l1.num=l2.num) l3
JOIN Logs l4
ON l3.id = l4.id-1 AND l3.num = l4.num
)