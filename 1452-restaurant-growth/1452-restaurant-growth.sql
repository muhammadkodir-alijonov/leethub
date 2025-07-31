-- calculate.
-- curr_day + 6 days.
-- avg(average_amount).
-- round(..,2).
-- order by asc visited_on.

-- first just simple calculation of problem like subquery.
--second we have to iterate outcoming response of subquery.
-- Step 1: First aggregate daily totals (since multiple customers per day)
WITH daily_totals AS (
    SELECT 
        visited_on,
        SUM(amount) as daily_amount
    FROM Customer 
    GROUP BY visited_on
),

-- Step 2: Calculate 7-day moving window using window functions
moving_averages AS (
    SELECT 
        visited_on,
        SUM(daily_amount) OVER (
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) as amount,
        AVG(daily_amount) OVER (
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) as average_amount,
        ROW_NUMBER() OVER (ORDER BY visited_on) as row_num
    FROM daily_totals
)

-- Step 3: Only return results where we have 7 days of data
SELECT 
    to_char(visited_on,'YYYY-MM-DD') visited_on,
    amount,
    ROUND(average_amount, 2) as average_amount
FROM moving_averages 
WHERE row_num >= 7
ORDER BY visited_on;