/* Write your PL/SQL query statement below */
with rank_sal_temp as
 (select d.name Department,
         e.name Employee,
         e.salary Salary,
         DENSE_RANK() over (PARTITION BY d.id ORDER BY e.salary desc) as rank_sal
    from Employee e
    join Department d
      on e.departmentId = d.id);
--
select t.Department, t.Employee, t.Salary
  from rank_sal_temp t
 where t.rank_sal <= 3;