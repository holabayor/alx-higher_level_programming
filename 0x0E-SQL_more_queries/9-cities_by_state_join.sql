--  script that list all the cities of
--  that can be found in the database using JOIN
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id
ORDER BY 1;