-- Create states table in htbn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS htbn_0e_0_usa;
USE htbn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(256) NOT NULL,
  PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("Carlifornia"), ("Arizona"),
  ("Texas"), ("New York"), ("Nevada");