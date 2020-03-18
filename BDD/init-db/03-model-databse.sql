-- ****************** SqlDBM: MySQL ******************;
-- ***************************************************;


-- ************************************** `models`

CREATE TABLE `models`
(
 `model_name` varchar(255) NOT NULL ,
 `r2`         float NULL ,
 `rmse`       float NULL ,
 `msle`       float NULL ,
 `rmsle`      float NULL ,
 `mape`       float NULL ,

PRIMARY KEY (`model_name`)
);





