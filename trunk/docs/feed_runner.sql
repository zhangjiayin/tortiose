-- phpMyAdmin SQL Dump
-- version 3.3.2deb1
-- http://www.phpmyadmin.net
--
-- Host: 192.168.2.27
-- Generation Time: May 09, 2010 at 11:02 AM
-- Server version: 5.1.41
-- PHP Version: 5.3.2-1ubuntu4.1

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
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feed_source_cnt`
--


-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `id` char(40) NOT NULL,
  `mail` char(50) NOT NULL,
  `nick` char(50) NOT NULL,
  `password` char(32) NOT NULL,
  `registe_time` int(11) NOT NULL
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
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_subscribe`
--

