/* Write your PL/SQL query statement below */
select t.name as name, r.bonus as bonus from Employee t
left join Bonus r on r.empId =t.empId
where r.bonus < 1000 or r.bonus is null;