# Fast API with MySQL example
This example show how to connect fastAPI to a MySQL database

## Activate a virtual enviroment
virtualenv env
. env/bin/activate

# Install requirements

pip install -r requirements.txt

## Create a databse in MySQL
```mysql
CREATE DATABASE restapi;
USE restapi;
CREATE TABLE user_info(
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(50) NOT NULL,
password VARCHAR(500) NOT NULL,
fullname VARCHAR(50) NOT NULL
);
