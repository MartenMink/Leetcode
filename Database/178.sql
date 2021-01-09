-- 178. Rank Scores

SELECT s1.Score, (SELECT count(DISTINCT s2.Score) + 1 FROM Scores s2 where s1.Score<s2.Score) as Rank
FROM Scores s1
ORDER BY s1.Score DESC
;