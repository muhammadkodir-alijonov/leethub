# Write your MySQL query statement below
select 
    p1.id 
from 
    weather p1, weather p2 
where 
    p2.recorddate = DATE_SUB(p1.recorddate, INTERVAL 1 Day) and p1.temperature > p2.temperature; 