-- Lists all cities of California in the database hbtn_0d_usa
-- Display: cities.id, state_id, cities.name ordered by cities.id
SELECT cities.id, state_id, cities.name
FROM cities
WHERE cities.state_id = (
	SELECT states.id
	FROM states
	WHERE states.name = 'California'
	)
ORDER BY cities.id ASC