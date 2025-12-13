# Write your MySQL query statement below

SELECT Sales.product_id, Sales.year AS first_year,
Sales.quantity, Sales.price FROM Sales
JOIN (
    SELECT product_id, MIN(year) AS year FROM Sales
    GROUP BY product_id
) derived1

ON Sales.product_id = derived1.product_id AND Sales.year = derived1.year