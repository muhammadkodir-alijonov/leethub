/* Write your PL/SQL query statement below */
select t.x  x,
       t.y  y,
       t.z  z,
       case when(t.x + t.y > t.z and t.x + t.z > t.y and t.z + t.y > t.x) then 'Yes' else 'No' end Triangle
  from Triangle t;
