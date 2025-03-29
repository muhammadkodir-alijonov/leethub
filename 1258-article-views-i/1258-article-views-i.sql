/* Write your PL/SQL query statement below */
select distinct t.author_id as id from Views t where t.viewer_id = t.author_id order by t.author_id asc;