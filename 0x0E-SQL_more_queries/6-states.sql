--  script that creates a table states
--  with 2 cols: id and name
CREATE DATABASE IF NOT EXISTS htbn_0d_usa;
CREATE TABLE IF NOT EXISTS htbn_0d_usa.states 
(
    id INT UNIQUE AUTO INCREMENT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);