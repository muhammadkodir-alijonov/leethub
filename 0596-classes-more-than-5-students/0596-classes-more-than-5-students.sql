/* Write your PL/SQL query statement below */
select t.Class class
  from Courses t
 group by t.Class
having count(t.Class) >= 5
