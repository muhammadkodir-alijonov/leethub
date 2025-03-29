/* Write your PL/SQL query statement below */
SELECT 
    today.id
FROM 
    weather today
LEFT JOIN 
    weather yesterday
    ON today.recorddate - 1 = yesterday.recorddate
WHERE 
    today.temperature > yesterday.temperature;