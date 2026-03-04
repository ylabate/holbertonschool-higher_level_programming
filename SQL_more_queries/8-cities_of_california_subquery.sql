select cities.id, state_id, cities.name
from cities
inner join states on cities.state_id = states.id
where states.name = 'California'
