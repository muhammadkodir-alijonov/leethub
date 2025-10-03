/* Write your PL/SQL query statement below */
/* Write your PL/SQL query statement below */
select user_id as user_id, UPPER(SUBSTR(name, 1, 1)) || LOWER(SUBSTR(name, 2)) as name
  from Users
 order by 1;
