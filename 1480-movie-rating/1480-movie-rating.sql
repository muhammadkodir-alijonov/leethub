SELECT results FROM (
  SELECT u.name AS results
  FROM Users u
  JOIN (
      SELECT user_id, COUNT(*) AS rating_count
      FROM MovieRating
      GROUP BY user_id
  ) r ON u.user_id = r.user_id
  ORDER BY r.rating_count DESC, u.name ASC
)
WHERE ROWNUM = 1

UNION ALL

SELECT results FROM (
  SELECT m.title AS results
  FROM Movies m
  JOIN (
      SELECT movie_id, AVG(rating) AS avg_rating
      FROM MovieRating
      WHERE TO_CHAR(created_at, 'YYYY-MM') = '2020-02'
      GROUP BY movie_id
  ) r ON m.movie_id = r.movie_id
  ORDER BY r.avg_rating DESC, m.title ASC
)
WHERE ROWNUM = 1;
