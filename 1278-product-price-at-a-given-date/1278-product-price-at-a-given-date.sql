/* Write your PL/SQL query statement below */
with Latestprices as
 (select Product_Id,
         New_Price,
         Row_Number() Over(partition by Product_Id order by Change_Date desc) as Rn
    from Products
   where Change_Date <= '2019-08-16')

select Product_Id, New_Price as Price
  from Latestprices
 where Rn = 1
union
select p.Product_Id, 10 as Price
  from (select distinct Product_Id
          from Products) p
 where not exists (select 1
    from Products Pr
   where Pr.Product_Id = p.Product_Id
     and Pr.Change_Date <= '2019-08-16')
