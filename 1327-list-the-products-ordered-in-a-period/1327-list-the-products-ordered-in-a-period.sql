# Write your MySQL query statement below
SELECT Products.product_name, derived.unit FROM Products
JOIN (
    SELECT product_id, SUM(unit) AS unit FROM Orders
    WHERE order_date LIKE "2020-02-%"
    GROUP BY product_id
    HAVING unit >= 100
) derived
ON derived.product_id = Products.product_id