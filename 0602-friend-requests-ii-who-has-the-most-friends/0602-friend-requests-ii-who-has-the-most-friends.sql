/* Write your PL/SQL query statement below */

-- only one most friends result is returned from the query
-- request id like user id who sent request to other one
-- accepter id is who accepted the request id

SELECT id, num
FROM (
    SELECT id, COUNT(*) as num
    FROM (
        SELECT requester_id as id FROM RequestAccepted
        UNION ALL
        SELECT accepter_id as id FROM RequestAccepted
    ) combined_ids
    GROUP BY id
) friend_counts
WHERE num = (
    SELECT MAX(num)
    FROM (
        SELECT COUNT(*) as num
        FROM (
            SELECT requester_id as id FROM RequestAccepted
            UNION ALL
            SELECT accepter_id as id FROM RequestAccepted
        ) combined_ids
        GROUP BY id
    ) max_friend_counts
);