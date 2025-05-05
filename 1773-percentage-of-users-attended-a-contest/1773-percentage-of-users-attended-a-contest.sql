/* Write your PL/SQL query statement below */
select r.Contest_Id,
       Round(count(distinct r.User_Id) * 100.0 / (select count(*)
                                                    from Users),
             2) as Percentage
  from Register r
 group by r.Contest_Id
 order by Percentage desc, r.Contest_Id asc;
