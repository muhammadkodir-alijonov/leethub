/* Write your PL/SQL query statement below */
select s.unique_id as unique_id, t.name as name from Employees t 
left join EmployeeUNI s on t.id = s.id