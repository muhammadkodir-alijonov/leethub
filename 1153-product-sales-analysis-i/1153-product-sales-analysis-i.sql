/* Write your PL/SQL query statement below */
select s.product_name as product_name, t.year as year, t.price as price from Sales t 
left join Product s on t.product_id = s.product_id