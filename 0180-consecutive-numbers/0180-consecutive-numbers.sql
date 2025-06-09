select distinct Num "Consecutivenums"
  from (select Num,
               Lag(Num, 1) Over(order by Id) as Prev_Num,
               Lead(Num, 1) Over(order by Id) as Next_Num
          from Logs)
 where Num = Prev_Num
   and Num = Next_Num;
