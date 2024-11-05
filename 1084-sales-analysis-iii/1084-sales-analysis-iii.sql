# Write your MySQL query statement below
SELECT Sales.product_id, product_name FROM Sales
JOIN Product
ON Product.product_id = Sales.product_id
GROUP BY product_id
HAVING (MIN(sale_date) BETWEEN "2019-01-01" AND "2019-03-31" ) AND (MAX(sale_date) BETWEEN "2019-01-01" AND "2019-03-31")
