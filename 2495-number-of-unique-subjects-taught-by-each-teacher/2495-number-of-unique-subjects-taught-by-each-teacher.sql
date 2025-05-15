/* Write your PL/SQL query statement below */
select t.teacher_id, count(distinct t.subject_id) cnt from Teacher t  
group by t.teacher_id