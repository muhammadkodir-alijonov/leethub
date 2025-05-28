select e.Employee_Id,
       e.Name,
       count(r.Employee_Id) as Reports_Count,
       Round(avg(r.Age)) as Average_Age
  from Employees e
  join Employees r
    on e.Employee_Id = r.Reports_To
 group by e.Employee_Id, e.Name
 order by e.Employee_Id;
