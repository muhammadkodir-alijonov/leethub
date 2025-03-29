/* Write your PL/SQL query statement below */
select t.name, t.population, t.area from World t where t.area >=3000000 or t.population >= 25000000;