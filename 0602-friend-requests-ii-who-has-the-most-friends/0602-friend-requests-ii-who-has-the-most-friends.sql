# Write your MySQL query statement below
SELECT id, IFNULL(request_count, 0)+IFNULL(accept_count, 0) AS num FROM (
    SELECT * FROM (
        SELECT DISTINCT(requester_id) AS id FROM RequestAccepted
        UNION
        SELECT DISTINCT(accepter_id) AS id FROM RequestAccepted
    ) derived1
    LEFT JOIN (
        SELECT accepter_id, IFNULL(COUNT(requester_id), 0) AS request_count FROM RequestAccepted
        GROUP BY accepter_id
    ) derived2
    ON derived1.id = derived2.accepter_id
    LEFT JOIN (
        SELECT requester_id, IFNULL(COUNT(accepter_id), 0) AS accept_count FROM RequestAccepted
        GROUP BY requester_id
    ) derived3
    ON derived1.id = derived3.requester_id
) derived4
ORDER BY num DESC
LIMIT 1