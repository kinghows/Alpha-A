/*
SQLyog Ultimate v12.5.1 (64 bit)
MySQL - 5.7.17-enterprise-commercial-advanced-log : Database - quant
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
/*Table structure for table `alphaa` */

DROP TABLE IF EXISTS `alphaa`;

CREATE TABLE `alphaa` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` varchar(10) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `detail` varchar(3000) DEFAULT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB AUTO_INCREMENT=461 DEFAULT CHARSET=utf8;

/*Table structure for table `boom_pool` */

DROP TABLE IF EXISTS `boom_pool`;

CREATE TABLE `boom_pool` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` int(4) NOT NULL,
  `stock_name` varchar(20) NOT NULL,
  `reason` varchar(500) NOT NULL,
  `price` float NOT NULL,
  `change_rate` varchar(10) NOT NULL,
  `turnover_ratio` varchar(10) NOT NULL,
  `circulation_value` varchar(10) NOT NULL,
  `total_value` varchar(10) NOT NULL,
  `first_raise_time` varchar(10) NOT NULL,
  `last_raise_time` varchar(10) NOT NULL,
  `last_boom_time` varchar(10) NOT NULL,
  `open_count` int(3) NOT NULL,
  `continue_board_count` int(3) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_name` (`stock_name`),
  KEY `idx_time` (`time`)
) ENGINE=InnoDB AUTO_INCREMENT=53677 DEFAULT CHARSET=utf8;

/*Table structure for table `boom_pool_his` */

DROP TABLE IF EXISTS `boom_pool_his`;

CREATE TABLE `boom_pool_his` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `stock_name` varchar(100) NOT NULL,
  `reason` varchar(500) NOT NULL,
  `price` float NOT NULL,
  `change_rate` varchar(10) NOT NULL,
  `turnover_ratio` varchar(10) NOT NULL,
  `circulation_value` varchar(10) NOT NULL,
  `total_value` varchar(10) NOT NULL,
  `first_raise_time` varchar(10) NOT NULL,
  `last_raise_time` varchar(10) NOT NULL,
  `last_boom_time` varchar(10) NOT NULL,
  `open_count` int(3) NOT NULL,
  `continue_board_count` int(3) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_date` (`date`),
  KEY `idx_name` (`stock_name`)
) ENGINE=InnoDB AUTO_INCREMENT=10599 DEFAULT CHARSET=utf8;

/*Table structure for table `cnew_pool` */

DROP TABLE IF EXISTS `cnew_pool`;

CREATE TABLE `cnew_pool` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` int(4) NOT NULL,
  `stock_name` varchar(20) NOT NULL,
  `price` float NOT NULL,
  `change_rate` varchar(10) NOT NULL,
  `turnover_ratio` varchar(10) NOT NULL,
  `circulation_value` varchar(10) NOT NULL,
  `total_value` varchar(10) NOT NULL,
  `open_board_day` int(2) NOT NULL,
  `before_open_count` int(2) NOT NULL,
  `accumulated_pcp` varchar(10) NOT NULL,
  `time_on_market` varchar(10) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_name` (`stock_name`),
  KEY `idx_time` (`time`)
) ENGINE=InnoDB AUTO_INCREMENT=72320 DEFAULT CHARSET=utf8;

/*Table structure for table `cnew_pool_his` */

DROP TABLE IF EXISTS `cnew_pool_his`;

CREATE TABLE `cnew_pool_his` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `stock_name` varchar(20) NOT NULL,
  `price` float NOT NULL,
  `change_rate` varchar(10) NOT NULL,
  `turnover_ratio` varchar(10) NOT NULL,
  `circulation_value` varchar(10) NOT NULL,
  `total_value` varchar(10) NOT NULL,
  `open_board_day` int(2) NOT NULL,
  `before_open_count` int(2) NOT NULL,
  `accumulated_pcp` varchar(10) NOT NULL,
  `time_on_market` varchar(10) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_date` (`date`),
  KEY `idx_name` (`stock_name`)
) ENGINE=InnoDB AUTO_INCREMENT=29950 DEFAULT CHARSET=utf8;

/*Table structure for table `down_pool` */

DROP TABLE IF EXISTS `down_pool`;

CREATE TABLE `down_pool` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` int(4) NOT NULL,
  `stock_name` varchar(20) NOT NULL,
  `price` float NOT NULL,
  `change_rate` varchar(10) NOT NULL,
  `blockade_ratio` varchar(10) NOT NULL,
  `turnover_ratio` varchar(10) NOT NULL,
  `circulation_value` varchar(10) NOT NULL,
  `total_value` varchar(10) NOT NULL,
  `first_board_time` varchar(10) NOT NULL,
  `last_board_time` varchar(10) NOT NULL,
  `open_count` int(3) NOT NULL,
  `continue_board_count` int(3) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_name` (`stock_name`),
  KEY `idx_time` (`time`)
) ENGINE=InnoDB AUTO_INCREMENT=82538 DEFAULT CHARSET=utf8;

/*Table structure for table `down_pool_his` */

DROP TABLE IF EXISTS `down_pool_his`;

CREATE TABLE `down_pool_his` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `stock_name` varchar(20) NOT NULL,
  `price` float NOT NULL,
  `change_rate` varchar(10) NOT NULL,
  `blockade_ratio` varchar(10) NOT NULL,
  `turnover_ratio` varchar(10) NOT NULL,
  `circulation_value` varchar(10) NOT NULL,
  `total_value` varchar(10) NOT NULL,
  `first_board_time` varchar(10) NOT NULL,
  `last_board_time` varchar(10) NOT NULL,
  `open_count` int(3) NOT NULL,
  `continue_board_count` int(3) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_date` (`date`),
  KEY `idx_name` (`stock_name`)
) ENGINE=InnoDB AUTO_INCREMENT=12928 DEFAULT CHARSET=utf8;

/*Table structure for table `fast_pool` */

DROP TABLE IF EXISTS `fast_pool`;

CREATE TABLE `fast_pool` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` int(4) NOT NULL,
  `stock_name` varchar(20) NOT NULL,
  `last_px` float NOT NULL,
  `pcp` float NOT NULL,
  `pcr` float NOT NULL,
  `theme` varchar(50) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_name` (`stock_name`),
  KEY `idx_time` (`time`)
) ENGINE=InnoDB AUTO_INCREMENT=215386 DEFAULT CHARSET=utf8;

/*Table structure for table `fast_pool_his` */

DROP TABLE IF EXISTS `fast_pool_his`;

CREATE TABLE `fast_pool_his` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` int(4) NOT NULL,
  `stock_name` varchar(20) NOT NULL,
  `last_px` float NOT NULL,
  `pcp` float NOT NULL,
  `pcr` float NOT NULL,
  `theme` varchar(50) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_name` (`stock_name`)
) ENGINE=InnoDB AUTO_INCREMENT=60044 DEFAULT CHARSET=utf8;

/*Table structure for table `hit_pool` */

DROP TABLE IF EXISTS `hit_pool`;

CREATE TABLE `hit_pool` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` int(4) NOT NULL,
  `stock_name` varchar(20) NOT NULL,
  `reason` varchar(500) NOT NULL,
  `price` float NOT NULL,
  `change_rate` varchar(10) NOT NULL,
  `blockade_ratio` varchar(10) NOT NULL,
  `turnover_ratio` varchar(10) NOT NULL,
  `circulation_value` varchar(10) NOT NULL,
  `total_value` varchar(10) NOT NULL,
  `first_raise_time` varchar(10) NOT NULL,
  `last_raise_time` varchar(10) NOT NULL,
  `open_count` int(3) NOT NULL,
  `continue_board_count` int(3) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_name` (`stock_name`),
  KEY `idx_time` (`time`)
) ENGINE=InnoDB AUTO_INCREMENT=113016 DEFAULT CHARSET=utf8;

/*Table structure for table `hit_pool_his` */

DROP TABLE IF EXISTS `hit_pool_his`;

CREATE TABLE `hit_pool_his` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `stock_name` varchar(20) NOT NULL,
  `reason` varchar(500) NOT NULL,
  `price` float NOT NULL,
  `change_rate` varchar(10) NOT NULL,
  `blockade_ratio` varchar(10) NOT NULL,
  `turnover_ratio` varchar(10) NOT NULL,
  `circulation_value` varchar(10) NOT NULL,
  `total_value` varchar(10) NOT NULL,
  `first_raise_time` varchar(10) NOT NULL,
  `last_raise_time` varchar(10) NOT NULL,
  `open_count` int(3) NOT NULL,
  `continue_board_count` int(3) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_date` (`date`),
  KEY `idx_name` (`stock_name`)
) ENGINE=InnoDB AUTO_INCREMENT=22401 DEFAULT CHARSET=utf8;

/*Table structure for table `hot_pool` */

DROP TABLE IF EXISTS `hot_pool`;

CREATE TABLE `hot_pool` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `theme` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `time` int(4) NOT NULL,
  `stock_name` varchar(20) NOT NULL,
  `price` float NOT NULL,
  `change_rate` varchar(10) NOT NULL,
  `turnover_ratio` varchar(10) NOT NULL,
  `circulation_value` varchar(10) NOT NULL,
  `total_value` varchar(10) NOT NULL,
  `pe` int(5) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_theme` (`theme`),
  KEY `idx_time` (`time`)
) ENGINE=InnoDB AUTO_INCREMENT=13607 DEFAULT CHARSET=utf8;

/*Table structure for table `hot_pool_his` */

DROP TABLE IF EXISTS `hot_pool_his`;

CREATE TABLE `hot_pool_his` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `theme` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `stock_name` varchar(20) NOT NULL,
  `price` float NOT NULL,
  `change_rate` varchar(10) NOT NULL,
  `turnover_ratio` varchar(10) NOT NULL,
  `circulation_value` varchar(10) NOT NULL,
  `total_value` varchar(10) NOT NULL,
  `pe` int(5) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_theme` (`theme`),
  KEY `idx_date` (`date`)
) ENGINE=InnoDB AUTO_INCREMENT=12299 DEFAULT CHARSET=utf8;

/*Table structure for table `hotspot` */

DROP TABLE IF EXISTS `hotspot`;

CREATE TABLE `hotspot` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `theme` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `time` varchar(10) DEFAULT NULL,
  `id` int(10) NOT NULL,
  `title` varchar(200) DEFAULT NULL,
  `detail` varchar(800) DEFAULT NULL,
  `stock_group` varchar(50) DEFAULT NULL,
  `createdatinsec` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_theme` (`theme`),
  KEY `idx_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12820 DEFAULT CHARSET=utf8;

/*Table structure for table `hotspot_his` */

DROP TABLE IF EXISTS `hotspot_his`;

CREATE TABLE `hotspot_his` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `theme` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `time` varchar(10) DEFAULT NULL,
  `id` int(10) NOT NULL,
  `title` varchar(200) DEFAULT NULL,
  `detail` varchar(800) DEFAULT NULL,
  `stock_group` varchar(50) DEFAULT NULL,
  `createdatinsec` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_theme` (`theme`),
  KEY `idx_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=265700 DEFAULT CHARSET=utf8;

/*Table structure for table `market_heat` */

DROP TABLE IF EXISTS `market_heat`;

CREATE TABLE `market_heat` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` int(4) NOT NULL,
  `limit_up` int(4) NOT NULL,
  `limit_lose` int(4) NOT NULL,
  `lose_ratio` varchar(6) NOT NULL,
  `heat_ratio` varchar(6) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_time` (`time`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

/*Table structure for table `market_heat_his` */

DROP TABLE IF EXISTS `market_heat_his`;

CREATE TABLE `market_heat_his` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `limit_up` int(4) NOT NULL,
  `limit_lose` int(4) NOT NULL,
  `lose_ratio` varchar(6) NOT NULL,
  `heat_ratio` varchar(6) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_date` (`date`)
) ENGINE=InnoDB AUTO_INCREMENT=479 DEFAULT CHARSET=utf8;

/*Table structure for table `new_pool` */

DROP TABLE IF EXISTS `new_pool`;

CREATE TABLE `new_pool` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` int(4) NOT NULL,
  `stock_name` varchar(20) NOT NULL,
  `price` float NOT NULL,
  `change_rate` varchar(10) NOT NULL,
  `turnover_ratio` varchar(10) NOT NULL,
  `circulation_value` varchar(10) NOT NULL,
  `total_value` varchar(10) NOT NULL,
  `first_open_time` varchar(10) NOT NULL,
  `before_open_count` int(2) NOT NULL,
  `accumulated_pcp` varchar(10) NOT NULL,
  `time_on_market` varchar(10) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_name` (`stock_name`),
  KEY `idx_time` (`time`)
) ENGINE=InnoDB AUTO_INCREMENT=11505 DEFAULT CHARSET=utf8;

/*Table structure for table `new_pool_his` */

DROP TABLE IF EXISTS `new_pool_his`;

CREATE TABLE `new_pool_his` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `stock_name` varchar(20) NOT NULL,
  `price` float NOT NULL,
  `change_rate` varchar(10) NOT NULL,
  `turnover_ratio` varchar(10) NOT NULL,
  `circulation_value` varchar(10) NOT NULL,
  `total_value` varchar(10) NOT NULL,
  `first_open_time` varchar(10) NOT NULL,
  `before_open_count` int(2) NOT NULL,
  `accumulated_pcp` varchar(10) NOT NULL,
  `time_on_market` varchar(10) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_date` (`date`),
  KEY `idx_name` (`stock_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4491 DEFAULT CHARSET=utf8;

/*Table structure for table `nyse` */

DROP TABLE IF EXISTS `nyse`;

CREATE TABLE `nyse` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` int(4) NOT NULL,
  `rose` int(5) NOT NULL,
  `fell` int(5) NOT NULL,
  `flat` int(5) DEFAULT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_time` (`time`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

/*Table structure for table `nyse_his` */

DROP TABLE IF EXISTS `nyse_his`;

CREATE TABLE `nyse_his` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `rose` int(5) NOT NULL,
  `fell` int(5) NOT NULL,
  `flat` int(5) DEFAULT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_date` (`date`)
) ENGINE=InnoDB AUTO_INCREMENT=471 DEFAULT CHARSET=utf8;

/*Table structure for table `pre_hit_pool` */

DROP TABLE IF EXISTS `pre_hit_pool`;

CREATE TABLE `pre_hit_pool` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` int(4) NOT NULL,
  `stock_name` varchar(20) NOT NULL,
  `reason` varchar(500) NOT NULL,
  `price` float NOT NULL,
  `change_rate` varchar(10) NOT NULL,
  `turnover_ratio` varchar(10) NOT NULL,
  `circulation_value` varchar(10) NOT NULL,
  `total_value` varchar(10) NOT NULL,
  `first_raise_time` varchar(10) NOT NULL,
  `last_raise_time` varchar(10) NOT NULL,
  `open_count` int(3) NOT NULL,
  `continue_board_count` int(3) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_name` (`stock_name`),
  KEY `idx_time` (`time`)
) ENGINE=InnoDB AUTO_INCREMENT=165915 DEFAULT CHARSET=utf8;

/*Table structure for table `pre_hit_pool_his` */

DROP TABLE IF EXISTS `pre_hit_pool_his`;

CREATE TABLE `pre_hit_pool_his` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `stock_name` varchar(20) NOT NULL,
  `reason` varchar(500) NOT NULL,
  `price` float NOT NULL,
  `change_rate` varchar(10) NOT NULL,
  `turnover_ratio` varchar(10) NOT NULL,
  `circulation_value` varchar(10) NOT NULL,
  `total_value` varchar(10) NOT NULL,
  `first_raise_time` varchar(10) NOT NULL,
  `last_raise_time` varchar(10) NOT NULL,
  `open_count` int(3) NOT NULL,
  `continue_board_count` int(3) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_date` (`date`),
  KEY `idx_name` (`stock_name`)
) ENGINE=InnoDB AUTO_INCREMENT=16745 DEFAULT CHARSET=utf8;

/*Table structure for table `stockindex` */

DROP TABLE IF EXISTS `stockindex`;

CREATE TABLE `stockindex` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `indexs` varchar(20) NOT NULL,
  `ivalue` varchar(10) NOT NULL,
  `ichange` varchar(10) NOT NULL,
  `iratio` varchar(10) NOT NULL,
  `time` int(4) NOT NULL,
  `codes` varchar(2) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_time` (`time`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;

/*Table structure for table `stockindex_his` */

DROP TABLE IF EXISTS `stockindex_his`;

CREATE TABLE `stockindex_his` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `indexs` varchar(20) NOT NULL,
  `ivalue` varchar(10) NOT NULL,
  `ichange` varchar(10) NOT NULL,
  `iratio` varchar(10) NOT NULL,
  `codes` varchar(2) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_date` (`date`)
) ENGINE=InnoDB AUTO_INCREMENT=1493 DEFAULT CHARSET=utf8;

/*Table structure for table `strong_pool` */

DROP TABLE IF EXISTS `strong_pool`;

CREATE TABLE `strong_pool` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` int(4) NOT NULL,
  `stock_name` varchar(20) NOT NULL,
  `reason` varchar(100) NOT NULL,
  `price` float NOT NULL,
  `change_rate` varchar(10) NOT NULL,
  `turnover_ratio` varchar(10) NOT NULL,
  `circulation_value` varchar(10) NOT NULL,
  `total_value` varchar(10) NOT NULL,
  `continue_board_count` int(2) NOT NULL,
  `board_days` varchar(10) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_name` (`stock_name`),
  KEY `idx_time` (`time`)
) ENGINE=InnoDB AUTO_INCREMENT=131397 DEFAULT CHARSET=utf8;

/*Table structure for table `strong_pool_his` */

DROP TABLE IF EXISTS `strong_pool_his`;

CREATE TABLE `strong_pool_his` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `stock_name` varchar(20) NOT NULL,
  `reason` varchar(100) NOT NULL,
  `price` float NOT NULL,
  `change_rate` varchar(10) NOT NULL,
  `turnover_ratio` varchar(10) NOT NULL,
  `circulation_value` varchar(10) NOT NULL,
  `total_value` varchar(10) NOT NULL,
  `continue_board_count` int(2) NOT NULL,
  `board_days` varchar(10) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_date` (`date`),
  KEY `idx_name` (`stock_name`)
) ENGINE=InnoDB AUTO_INCREMENT=17729 DEFAULT CHARSET=utf8;

/*Table structure for table `theme` */

DROP TABLE IF EXISTS `theme`;

CREATE TABLE `theme` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `title` varchar(10) NOT NULL,
  `theme` varchar(50) NOT NULL,
  `rate` varchar(10) NOT NULL,
  `time` int(4) NOT NULL,
  `zd` varchar(1) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_theme` (`theme`),
  KEY `idx_time` (`time`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8;

/*Table structure for table `theme_his` */

DROP TABLE IF EXISTS `theme_his`;

CREATE TABLE `theme_his` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `title` varchar(10) NOT NULL,
  `theme` varchar(50) NOT NULL,
  `rate` varchar(10) NOT NULL,
  `zd` varchar(1) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_theme` (`theme`),
  KEY `idx_date` (`date`)
) ENGINE=InnoDB AUTO_INCREMENT=18377 DEFAULT CHARSET=utf8;

/*Table structure for table `theme_pool` */

DROP TABLE IF EXISTS `theme_pool`;

CREATE TABLE `theme_pool` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `theme` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `time` int(4) NOT NULL,
  `stock_name` varchar(20) NOT NULL,
  `price` float NOT NULL,
  `change_rate` varchar(10) NOT NULL,
  `turnover_ratio` varchar(10) NOT NULL,
  `circulation_value` varchar(10) NOT NULL,
  `total_value` varchar(10) NOT NULL,
  `pe` int(5) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_theme` (`theme`),
  KEY `idx_time` (`time`)
) ENGINE=InnoDB AUTO_INCREMENT=147 DEFAULT CHARSET=utf8;

/*Table structure for table `theme_pool_his` */

DROP TABLE IF EXISTS `theme_pool_his`;

CREATE TABLE `theme_pool_his` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `theme` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `stock_name` varchar(20) NOT NULL,
  `price` float NOT NULL,
  `change_rate` varchar(10) NOT NULL,
  `turnover_ratio` varchar(10) NOT NULL,
  `circulation_value` varchar(10) NOT NULL,
  `total_value` varchar(10) NOT NULL,
  `pe` int(5) NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `idx_theme` (`theme`),
  KEY `idx_date` (`date`)
) ENGINE=InnoDB AUTO_INCREMENT=12516 DEFAULT CHARSET=utf8;

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `tid` int(10) NOT NULL AUTO_INCREMENT,
  `phone` varchar(11) NOT NULL,
  `email` varchar(30) DEFAULT NULL,
  `pwd` varchar(50) NOT NULL,
  `exp_date` date NOT NULL DEFAULT '2020-01-01',
  `logintoken` varchar(20) DEFAULT NULL,
  `sessiontoken` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`tid`),
  UNIQUE KEY `ui_phone` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
