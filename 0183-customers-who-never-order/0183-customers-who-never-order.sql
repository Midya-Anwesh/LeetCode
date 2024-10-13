# Write your MySQL query statement below
SELECT name AS "Customers" FROM Customers 
WHERE id IN (
    SELECT id FROM Customers
    EXCEPT
    SELECT CustomerId FROM Orders
)