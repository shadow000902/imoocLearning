# -*- coding: utf-8 -*-

use imooc;
CREATE TABLE user(
  userid INT(11) NOT NULL AUTO_INCREMENT,
  username VARCHAR(100) DEFAULT NULL,
  PRIMARY KEY (userid)
) charset=utf8;