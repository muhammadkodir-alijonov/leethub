/* Write your PL/SQL query statement below */
select to_char(t.activity_date,'yyyy-mm-dd') day, count(distinct t.user_id) active_users from Activity t
where t.activity_date between '2019-06-28' and '2019-07-27'
group by t.activity_date