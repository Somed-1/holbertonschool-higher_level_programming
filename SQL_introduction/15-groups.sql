-- Number by score
SELECT score, COUNT(id) as number FROM second_table
GROUP BY score
ORDER BY score DESC;
