use taller2;

CREATE TABLE IF NOT EXISTS `users`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `user_id` varchar(255) NOT NULL UNIQUE,
    `email` varchar(255) NOT NULL UNIQUE,
    `password` varchar(255) NOT NULL, 
    PRIMARY KEY (`id`));

CREATE TABLE IF NOT EXISTS `business`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `business_id` varchar(100) DEFAULT NULL,
    `name` varchar(500) DEFAULT NULL,
    `address` varchar(500) DEFAULT NULL,
    `city` varchar(500) DEFAULT NULL,
    `state` varchar(500) DEFAULT NULL,
    `latitude` FLOAT(11,8) DEFAULT NULL,
    `longitude` FLOAT(11,8) DEFAULT NULL,
    `categories` varchar(500) DEFAULT NULL,
    PRIMARY KEY (`id`));

ALTER TABLE business CONVERT TO CHARACTER SET utf8;

CREATE TABLE IF NOT EXISTS `recomendations_business`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `user_id` varchar(100) NOT NULL,
    `business_id` varchar(100) DEFAULT NULL,
    `recomendation_score` decimal(2,1) DEFAULT NULL,
    PRIMARY KEY (`id` ));

ALTER TABLE recomendations_business CONVERT TO CHARACTER SET utf8;