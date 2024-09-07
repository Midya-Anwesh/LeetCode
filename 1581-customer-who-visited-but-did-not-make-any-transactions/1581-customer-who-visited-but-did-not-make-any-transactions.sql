# Write your MySQL query statement below
SELECT Visits.customer_id, COUNT(Visits.customer_id) AS count_no_trans FROM Visits
WHERE Visits.visit_id IN (
    SELECT Visits.visit_id FROM Visits
    EXCEPT 
    SELECT Transactions.visit_id FROM Transactions
    )
GROUP BY customer_id;