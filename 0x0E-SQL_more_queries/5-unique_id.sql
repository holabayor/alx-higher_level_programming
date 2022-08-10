--  script that creates a table unique_id
--  with 2 cols: id and name
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));