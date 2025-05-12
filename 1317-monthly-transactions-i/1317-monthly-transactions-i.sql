/* Write your PL/SQL query statement below */
select to_char(t.Trans_Date, 'YYYY-MM') as month,
       t.Country,
       count(*) as Trans_Count,
       count(case
                when t.State = 'approved' then
                 1
              end) as Approved_Count,
       sum(t.Amount) as Trans_Total_Amount,
       sum(case
              when t.State = 'approved' then
               t.Amount
              else
               0
            end) as Approved_Total_Amount
  from Transactions t
 group by to_char(t.Trans_Date, 'YYYY-MM'), t.Country
 order by month, t.Country;
