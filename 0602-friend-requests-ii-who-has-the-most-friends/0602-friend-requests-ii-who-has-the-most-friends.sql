/* Write your PL/SQL query statement below */

-- only one most friends result is returned from the query
-- request id like user id who sent request to other one
-- accepter id is who accepted the request id

WITH friend_counts AS (
    SELECT id, COUNT(*) as num
    FROM (
        SELECT requester_id as id FROM RequestAccepted
        UNION ALL
        SELECT accepter_id as id FROM RequestAccepted
    ) combined_ids
    GROUP BY id
    order by num desc
)
SELECT id, num
FROM friend_counts
WHERE rownum = 1;