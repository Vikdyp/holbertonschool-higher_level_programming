-- Task: Liste toute les entrer de la table second_table avec un score >= 10

-- Affiche le score et le nom dans l'ordre
SELECT score, name FROM second_table WHERE score >= 10
ORDER BY score DESC;
