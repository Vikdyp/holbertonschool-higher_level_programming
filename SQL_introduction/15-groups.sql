-- Task: Affiche combien de fois chaque score est present

-- Compte le nombre de fois qu'un score est present
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
