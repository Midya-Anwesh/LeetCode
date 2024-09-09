# Write your MySQL query statement below
SELECT ROUND(COUNT(DISTINCT(derived2.player_id))/(SELECT COUNT(DISTINCT(player_id)) FROM Activity), 2) 
    AS fraction FROM
    (
        SELECT player_id, MIN(event_date) AS event_date FROM Activity
        GROUP BY player_id
        HAVING COUNT(event_date) > 1
    ) derived1

    JOIN Activity derived2
    ON derived1.player_id = derived2.player_id AND DATEDIFF(derived2.event_date, derived1.event_date) = 1
;