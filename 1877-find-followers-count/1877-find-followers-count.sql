/* Write your PL/SQL query statement below */
select t.User_Id User_Id, count(t.Follower_Id) Followers_Count
  from Followers t
 group by t.User_Id
 order by 1

