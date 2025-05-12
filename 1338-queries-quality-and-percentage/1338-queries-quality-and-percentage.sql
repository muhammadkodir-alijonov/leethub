/* Write your PL/SQL query statement below */
select t.Query_Name,
       Round(avg(t.Rating / t.Position), 2) as Quality,
       Round(100.0 * sum(case
                            when t.Rating < 3 then
                             1
                            else
                             0
                          end) / count(*),
              2) as Poor_Query_Percentage
  from Queries t
 group by t.Query_Name;