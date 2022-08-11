--  script that creates a table cities
--  with 2 cols: id and name
CREATE DATABASE IF NOT EXISTS htbn_0d_usa;
CREATE TABLE IF NOT EXISTS htbn_0d_usa.cities 
(
    id INT UNIQUE AUTO INCREMENT NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES htbn_0d_usa.states(id)
);