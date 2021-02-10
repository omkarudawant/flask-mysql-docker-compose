USE user_management;
CREATE TABLE user (name CHAR(255) PRIMARY KEY NOT NULL,email VARCHAR(255),password CHAR(10),mobile INT(13),profile_picture LONGBLOB NOT NULL,address VARCHAR(255));
create table address(name CHAR(255) PRIMARY KEY NOT NULL,flat_number INT,addr1 VARCHAR(255),addr2 VARCHAR(255),city VARCHAR(255),state VARCHAR(255),pin INT
);