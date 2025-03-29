/* Write your PL/SQL query statement below */
select t.customer_id as customer_id, count(t.visit_id) as count_no_trans from Visits t
left join Transactions s on t.visit_id = s.visit_id
where s.transaction_id is null
group by t.customer_id;