/* Write your PL/SQL query statement below */
select Employee_Id, Department_Id
  from (select Employee_Id,
               Department_Id,
               Primary_Flag,
               Row_Number() Over(partition by Employee_Id order by Primary_Flag desc) Rn
          from Employee)
 where Rn = 1