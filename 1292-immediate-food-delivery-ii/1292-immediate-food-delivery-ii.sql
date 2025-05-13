/* Write your PL/SQL query statement below */
with Firstorders as
 (select *
    from Delivery d
   where Order_Date = (select min(Order_Date)
                         from Delivery
                        where Customer_Id = d.Customer_Id))

select Round((count(case
                       when t.Order_Date = t.Customer_Pref_Delivery_Date then
                        1
                     end) / count(t.Order_Date)) * 100,
              2) Immediate_Percentage
  from Firstorders t

