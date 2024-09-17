# Write your MySQL query statement below
SELECT * FROM (
    SELECT name AS results FROM Users WHERE user_id IN  (
        SELECT user_id FROM MovieRating
        GROUP BY user_id
        HAVING COUNT(user_id) = (
            SELECT COUNT(movie_id) AS rating_count FROM MovieRating
            GROUP BY user_id
            ORDER BY rating_count DESC
            LIMIT 1
        )
    )
    ORDER BY results
    LIMIT 1
) user_name

UNION ALL

SELECT * FROM (
    SELECT title AS results FROM Movies WHERE movie_id IN (
        SELECT movie_id FROM MovieRating
        WHERE created_at LIKE "2020-02%"
        GROUP BY movie_id
        HAVING AVG(rating) = (
            SELECT AVG(rating) AS avg_rating FROM MovieRating
            WHERE created_at LIKE "2020-02%"
            GROUP BY movie_id
            ORDER BY avg_rating DESC
            LIMIT 1
        )
    ) 
    ORDER BY results
    LIMIT 1
) movie_name