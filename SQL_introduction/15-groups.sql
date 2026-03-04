-- Lists the number of records with the same score in the table second_table
-- Display: score and number of records for this score
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score;
