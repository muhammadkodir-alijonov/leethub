/* Write your PL/SQL query statement below */
select t.project_id project_id, round(avg(r.experience_years),2) average_years  from Project t, Employee r where t.employee_id = r.employee_id
group by t.project_id