# Write your MySQL query statement below
SELECT derived1.month, derived1.country, trans_count, IFNULL(approved_count, 0) AS approved_count, 
trans_total_amount, IFNULL(approved_total_amount, 0) AS approved_total_amount
FROM

    (
        SELECT id, DATE_FORMAT(trans_date, '%Y-%m') AS month, country, COUNT(*) AS trans_count, 
        SUM(amount) AS trans_total_amount FROM Transactions
        GROUP BY country, month
    ) derived1

    LEFT JOIN

    (
        SELECT id, country,DATE_FORMAT(trans_date, '%Y-%m') AS month, SUM(amount) AS approved_total_amount,
        COUNT(*) AS approved_count FROM Transactions
        WHERE state="approved"
        GROUP BY country, month
    ) derived2

    ON derived1.country <=> derived2.country AND derived1.month = derived2.month;