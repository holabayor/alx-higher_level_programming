--  script that creates the user user_0d_2
--  user_0d_2 should have ALL priviledges
CREATE DATABASE IF NOT EXISTS htbn_0d_1;
CREATE USER IF NOT EXISTS user_0d_1 IDENTIFIED BY 'user_0d_pwd';
GRANT ALL ON *.* TO user_0d_1;