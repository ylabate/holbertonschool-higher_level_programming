-- Lists all records of the table second_table without a name value
-- Display: score and name, ordered by score DESC
SELECT score, name FROM second_table WHERE name != '' ORDER BY score DESC;
