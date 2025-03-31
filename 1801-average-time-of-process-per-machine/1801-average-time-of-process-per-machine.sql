/* Write your PL/SQL query statement below */
with process_times as (
    select 
        machine_id,
        process_id,
        MAX(case when activity_type = 'end' then timestamp end) - 
        MAX(case when activity_type = 'start' then timestamp end) as process_time
    from Activity
    group by machine_id, process_id
)

select machine_id, ROUND(AVG(process_time),3) as processing_time
from process_times 
group by machine_id;