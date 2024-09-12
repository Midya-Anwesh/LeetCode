# Write your MySQL query statement below
SELECT DISTINCT(p1.product_id) AS product_id, IFNULL(derived3.price, 10) AS price FROM Products p1
LEFT JOIN
(
    SELECT derived1.product_id, derived1.new_price AS price FROM Products derived1
    JOIN (
        SELECT product_id, MAX(change_date) AS change_date FROM Products
        WHERE change_date <= "2019-08-16"
        GROUP BY product_id
        ORDER BY product_id, DATEDIFF(change_date, "2019-08-16")
    ) derived2 ON derived1.product_id = derived2.product_id AND derived1.change_date = derived2.change_date
) derived3
ON p1.product_id = derived3.product_id