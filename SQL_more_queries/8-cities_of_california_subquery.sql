-- Lists all cities of California in the database hbtn_0d_usa
-- Display: cities.id, state_id, cities.name ordered by cities.id
SELECT cities.id, state_id, cities.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
WHERE states.name = 'California'
