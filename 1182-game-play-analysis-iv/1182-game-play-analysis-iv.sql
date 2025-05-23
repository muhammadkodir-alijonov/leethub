   SELECT ROUND(COUNT(a2.player_id) / COUNT(a.player_id), 2) AS fraction
     FROM activity a
LEFT JOIN activity a2
       ON a2.player_id = a.player_id
      AND a2.event_date = a.event_date + 1
    WHERE (a.player_id, a.event_date) IN (SELECT player_id, MIN(event_date)
                                            FROM activity
                                        GROUP BY player_id)