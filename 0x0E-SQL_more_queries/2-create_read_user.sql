--  script that creates the database htbn_0d_2 and the user user_0d_2
--  user_0d_2 should have only SELECT priviledges
CREATE DATABASE IF NOT EXISTS htbn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON htbn_0d_2 TO user_0d_2