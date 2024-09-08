SELECT derived1.user_id, ROUND(IFNULL(confirmed_count/total_count, 0), 2) AS confirmation_rate FROM

    (SELECT Signups.user_id, IFNULL(COUNT(Confirmations.user_id), 0) AS total_count FROM Signups
    LEFT JOIN Confirmations
    ON Signups.user_id = Confirmations.user_id
    GROUP BY Signups.user_id) derived1

    LEFT JOIN

    (SELECT user_id, IFNULL(COUNT(user_id), 0) AS confirmed_count FROM Confirmations
    WHERE action = "confirmed"
    GROUP BY user_id
    ) derived2

    ON derived1.user_id = derived2.user_id
    
;