# Write your MySQL query statement below
SELECT * FROM (
    SELECT derived1.request_at AS "Day", IFNULL(ROUND(total_cancelled_requests/total_unbanned_requests, 2), 0) AS "Cancellation Rate" FROM (
        (
            SELECT COUNT(*) AS total_unbanned_requests, request_at FROM Trips
            WHERE NOT client_id IN (
                SELECT users_id FROM Users
                WHERE banned = "Yes"
            )
            AND NOT driver_id IN (
                SELECT users_id FROM Users
                WHERE banned = "Yes"
            )
            GROUP BY request_at
            ORDER BY request_at
        ) derived1

        LEFT JOIN 

        (
            SELECT COUNT(*) AS total_cancelled_requests, status, request_at FROM Trips t2
            WHERE NOT client_id IN (
                SELECT users_id FROM Users
                WHERE banned = "Yes"
            ) AND status LIKE "cancelled%" AND NOT driver_id IN (
                SELECT users_id FROM Users
                WHERE banned = "Yes"
            )
            GROUP BY request_at
            ORDER BY request_at
        ) derived2

        ON derived1.request_at = derived2.request_at
    )
) d4 WHERE Day IN (
    "2013-10-01", "2013-10-02", "2013-10-03"
)