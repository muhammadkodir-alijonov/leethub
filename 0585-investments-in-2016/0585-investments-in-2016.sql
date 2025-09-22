/* Write your PL/SQL query statement below */
-- 1. summ all inestmant in 2016 for all pid         
-- 2. where: value 2015 one or more
-- 3. not located same city and other placeholder(let and lon)
-- 4. res should be round 2 decemal
select round(sum(q.tiv_2016), 2) as tiv_2016
  from Insurance q
 where q.tiv_2015 in (select t.tiv_2015
                        from Insurance t
                       group by t.tiv_2015
                      having count(t.tiv_2015) > 1)
   and (q.lon, q.lat) in (select r.lon, r.lat
                            from Insurance r
                           group by r.lat, r.lon
                          having count(r.lat) = 1)
