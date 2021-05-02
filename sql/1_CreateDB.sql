-- http://coding-karma.com/2017/08/12/creating-login-registration-using-nodejs-mysql/
create database taller2;
show databases;
use taller2;

CREATE USER 'user_taller2'@'localhost' IDENTIFIED BY 'taller2.';
GRANT ALL PRIVILEGES ON taller2.* TO 'user_taller2'@'localhost';
FLUSH PRIVILEGES;

