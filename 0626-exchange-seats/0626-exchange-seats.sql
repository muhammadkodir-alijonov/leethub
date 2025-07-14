# Write your MySQL query statement below
SELECT (CASE
        WHEN id % 2 = 1 AND (SELECT COUNT(*) FROM Seat) <> id THEN
            id + 1
        WHEN id % 2 = 1 AND (SELECT COUNT(*) FROM Seat) = id THEN
            id
        ELSE
            id - 1
        END) AS id, student
FROM Seat
ORDER BY id ASC;