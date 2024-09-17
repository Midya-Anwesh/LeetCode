# Write your MySQL query statement below
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016 FROM Insurance
WHERE pid IN (
    SELECT pid FROM Insurance
    WHERE tiv_2015 IN (
        SELECT tiv_2015 FROM Insurance i1
        GROUP BY tiv_2015
        HAVING COUNT(pid) > 1
    )

    EXCEPT

    SELECT i1.pid FROM Insurance i1
    JOIN Insurance i2
    ON i1.lat = i2.lat AND i1.lon = i2.lon
    AND i1.pid <> i2.pid
)