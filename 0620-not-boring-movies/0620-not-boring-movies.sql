# Write your MySQL query statement below
select t.id id, t.movie movie, t.description description, t.rating rating from Cinema t 
where t.description <> 'boring' and t.id%2=1 order by t.id desc