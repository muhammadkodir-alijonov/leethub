/* Write your PL/SQL query statement below */
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
