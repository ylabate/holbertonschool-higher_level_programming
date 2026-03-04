select cities.id, cities.name, states.name
from cities
inner join states on cities.state_id = states.id
order by state_id;