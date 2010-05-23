-- phpMyAdmin SQL Dump
-- version 3.3.2deb1
-- http://www.phpmyadmin.net
--
-- Host: 192.168.2.27
-- Generation Time: May 21, 2010 at 07:07 PM
-- Server version: 5.1.41
-- PHP Version: 5.3.2-1ubuntu4.2

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `feed_runner`
--

-- --------------------------------------------------------

--
-- Table structure for table `feed_catalog`
--

CREATE TABLE IF NOT EXISTS `feed_catalog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `feed_catalog`
--


-- --------------------------------------------------------

--
-- Table structure for table `feed_catalog_source`
--

CREATE TABLE IF NOT EXISTS `feed_catalog_source` (
  `source_id` int(11) NOT NULL,
  `catalog_id` int(11) NOT NULL,
  PRIMARY KEY (`source_id`,`catalog_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `feed_catalog_source`
--


-- --------------------------------------------------------

--
-- Table structure for table `feed_source`
--

CREATE TABLE IF NOT EXISTS `feed_source` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(20) NOT NULL,
  `url` char(255) NOT NULL,
  `add_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `update_time` (`update_time`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `feed_source`
--


-- --------------------------------------------------------

--
-- Table structure for table `feed_source_cnt`
--

CREATE TABLE IF NOT EXISTS `feed_source_cnt` (
  `id` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  `cnt` int(11) NOT NULL,
  UNIQUE KEY `id` (`id`,`update_time`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `feed_source_cnt`
--


-- --------------------------------------------------------

--
-- Table structure for table `manager`
--

CREATE TABLE IF NOT EXISTS `manager` (
  `userid` int(11) NOT NULL,
  `role` int(11) NOT NULL,
  `atime` int(11) NOT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `manager`
--


-- --------------------------------------------------------

--
-- Table structure for table `manager_role`
--

CREATE TABLE IF NOT EXISTS `manager_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role` char(50) NOT NULL,
  `privileges` char(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `manager_role`
--


-- --------------------------------------------------------

--
-- Table structure for table `session`
--

CREATE TABLE IF NOT EXISTS `session` (
  `namespace` char(33) NOT NULL,
  `data` text NOT NULL,
  `accessed` datetime NOT NULL,
  `created` datetime NOT NULL,
  PRIMARY KEY (`namespace`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `session`
--

INSERT INTO `session` (`namespace`, `data`, `accessed`, `created`) VALUES
('37144dfaa68df941aaba9bcd98828628', '€}qUsessionq}q(U_accessed_timeqGAÒúó.ŽŸU_creation_timeqGAÒúòà¹–ÝUtimeqU\r1273744570.22qus.', '2010-05-13 17:56:10', '2010-05-13 17:50:58'),
('5c440d5fe78dd163350363a007e50782', '€}qUsessionq}q(U_accessed_timeqGAÒúð¸4U_creation_timeqGAÒúð¶¾=OUtimeqU\r1273742048.09qus.', '2010-05-13 17:14:08', '2010-05-13 17:14:02'),
('6b7a14ecabca3eed76692b97770864d4', '€}qUsessionq}q(U_accessed_timeqGAÒúñuÐjÂU_creation_timeqGAÒúñh¬žˆUtimeqU\r1273742807.26qus.', '2010-05-13 17:26:47', '2010-05-13 17:25:54'),
('6d56e3c708e4d0d74ee90d1528430c3a', '€}qUsessionq}q(U_accessed_timeqGAÒú÷ˆvU_creation_timeqGAÒú÷‡ÜL#UtimeqU\r1273749024.24qus.', '2010-05-13 19:10:24', '2010-05-13 19:10:23'),
('b004cb8696cf5ba2aa420396eb803ff3', '€}qUsessionq}q(U_accessed_timeqGAÒúçh·R?U_creation_timeqGAÒúçhCqeUtimeqGAÒúçh·J0us.', '2010-05-13 14:35:14', '2010-05-13 14:35:13'),
('bb344882887748662fa182f243639947', '€}qUsessionq}q(U_accessed_timeqGAÒúòd˜žU_creation_timeqGAÒúòc²¿©UtimeqU\r1273743760.12qus.', '2010-05-13 17:42:40', '2010-05-13 17:42:38'),
('c54869892f2cf2f3e2aba39dd57d21a4', '€}qUsessionq}q(U_accessed_timeqGAÒúðvU_creation_timeqGAÒúðvUtimeqU\r1273741405.82qus.', '2010-05-13 17:03:25', '2010-05-13 17:03:25');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `id` char(40) NOT NULL,
  `mail` char(50) NOT NULL,
  `nick` char(50) NOT NULL,
  `password` char(32) NOT NULL,
  `registe_time` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mail` (`mail`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--


-- --------------------------------------------------------

--
-- Table structure for table `user_profile`
--

CREATE TABLE IF NOT EXISTS `user_profile` (
  `user_id` char(40) NOT NULL,
  `birthday` datetime NOT NULL,
  `carrer` int(11) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user_profile`
--


-- --------------------------------------------------------

--
-- Table structure for table `user_subscribe`
--

CREATE TABLE IF NOT EXISTS `user_subscribe` (
  `user_id` char(40) NOT NULL,
  `source_id` int(11) NOT NULL,
  `add_time` int(11) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user_subscribe`
--

