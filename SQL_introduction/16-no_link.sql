-- Task: Affich tout les champs de la table second_table avec condition

-- Affiche les champs
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
