# Write your MySQL query statement below
SELECT contest_id, ROUND((participant/user_count)*100, 2) AS percentage FROM
        (SELECT contest_id, COUNT(user_id) AS participant FROM Register
        GROUP BY contest_id) contest
    LEFT JOIN
        (SELECT COUNT(user_id) AS user_count FROM Users) user
    ON 1
ORDER BY percentage DESC, contest_id ASC;