-- script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, states.name FROM cities, states WHERE states.id = state_id
ORDER BY cities.id ASC;
