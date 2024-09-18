# Write your MySQL query statement below
SELECT * FROM Users
WHERE mail REGEXP "^[a-z]{1}([a-z]|\\.|_|-|[0-9])*@leetcode\\.com$"