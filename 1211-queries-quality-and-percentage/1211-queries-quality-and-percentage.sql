# Write your MySQL query statement below
SELECT derived1.query_name, quality, ROUND(IFNULL((derived2.bad_ratings/derived1.total_query)*100, 0), 2) AS poor_query_percentage FROM

        (SELECT query_name, ROUND(SUM(rating/position)/COUNT(query_name), 2) AS quality, COUNT(query_name) AS total_query FROM Queries
        WHERE query_name IS NOT NULL
        GROUP BY query_name) derived1
    LEFT JOIN
        (SELECT query_name, COUNT(rating) AS bad_ratings FROM Queries
        WHERE rating < 3 AND query_name IS NOT NULL
        GROUP BY query_name
        ) derived2

    ON derived1.query_name = derived2.query_name;