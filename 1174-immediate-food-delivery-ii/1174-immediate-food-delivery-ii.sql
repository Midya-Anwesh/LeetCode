# Write your MySQL query statement below
    SELECT ROUND(COUNT(derived2.customer_id)*100/(SELECT COUNT(DISTINCT(customer_id)) FROM Delivery), 2)
    AS immediate_percentage FROM
    (
        SELECT MIN(order_date) AS order_date, customer_id FROM Delivery
        GROUP BY customer_id
    ) derived1
    JOIN Delivery derived2
    ON derived1.order_date = derived2.order_date AND derived1.customer_id = derived2.customer_id

    WHERE DATEDIFF(derived2.order_date, derived2.customer_pref_delivery_date) = 0;