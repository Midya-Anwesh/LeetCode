# Write your MySQL query statement below
SELECT day_id AS Id FROM(
SELECT present.id AS day_id, present.temperature AS present_temp, past.temperature AS past_temp FROM Weather present
LEFT JOIN Weather past ON past.recordDate = DATE_SUB(present.recordDate, INTERVAL 1 DAY)) temp_table
WHERE ( (NOT(present_temp IS NULL)) AND (NOT(past_temp IS NULL)) AND (present_temp > past_temp));