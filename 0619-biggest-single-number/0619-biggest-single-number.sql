select max(Num) as Num
  from (select Num
          from Mynumbers
         group by Num
        having count(*) = 1)  Singles;
