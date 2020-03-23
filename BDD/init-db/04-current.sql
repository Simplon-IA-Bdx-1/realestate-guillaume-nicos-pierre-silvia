-- ************************************** `current_model`

CREATE TABLE `current_model`
(
 `id`         enum('1') NOT NULL ,
 `model_name` varchar(255) NOT NULL ,

PRIMARY KEY (`id`),
KEY `fkIdx_125` (`model_name`),
CONSTRAINT `FK_125` FOREIGN KEY `fkIdx_125` (`model_name`) REFERENCES `models` (`model_name`)
);
