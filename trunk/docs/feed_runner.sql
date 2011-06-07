-- phpMyAdmin SQL Dump
-- version 3.3.2deb1
-- http://www.phpmyadmin.net
--
-- Host: 192.168.2.27
-- Generation Time: May 25, 2010 at 07:51 PM
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
-- Table structure for table `feed_source`
--

CREATE TABLE IF NOT EXISTS `feed_source` (
  `id` char(32) NOT NULL,
  `name` char(20) NOT NULL,
  `url` char(255) NOT NULL,
  `add_time` int(11) NOT NULL,
  `update_time` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `update_time` (`update_time`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `feed_source`
--

INSERT INTO `feed_source` (`id`, `name`, `url`, `add_time`, `update_time`) VALUES
('042f873163e69609e624ebf55c0a792c', '', 'http://api.jquery.com/empty/feed/', 1274770726, 1274770726),
('77df04d8c0aef04e9b778d5e258ea478', '', 'http://api.jquery.com/empty/feed/1', 1274771415, 1274771415),
('39d13674a4e475a8f65ec55f97398f4b', '', 'http://api.jquery.com/empty/', 1274771584, 1274771584),
('5506ee24c89e43b39b37e1225e2ca27f', '', 'http://api.jquery.com/empty/2', 1274771625, 1274771625),
('abd26334db51ede7b10dc6a7920680ee', '', 'http://api.jquery.com/empty/1', 1274771646, 1274771646),
('925838ded0b9be1fa0342ae7b3a83143', '', 'http://code.jquery.com/jquery-1.4.2.min.js', 1274774510, 1274774510),
('4c3174f4d2b9b51cbeaa26a005e52bd4', '', 'http://blog.00rz.com/feed', 1274774517, 1274774517),
('cfb85bb93a02fbf67aee8c1e2bf09eb8', '', 'http://api.jquery.com/empty-selector/', 1274780251, 1274780251),
('1d9d724606b88b72c758e198baeb9b3b', '', 'http://pylonshq.com/docs/en/0.9.7/helpers/', 1274781485, 1274781485),
('cc06b29112938c81713d0d390e6793f2', '', 'http://baike.baidu.com/view/2745769.htm?fr=ala0_1', 1274781515, 1274781515),
('239da3b3749ea007355e236352332bd1', '', 'http://proxy.00rz.com/zhangjiayin', 1274781563, 1274781563),
('306ed7b1081e3ba0cce8863f95404f66', '', 'http://pylonshq.com/docs/en/0.9.7/helpers/1', 1274783274, 1274783274),
('aa0e6dbe458e2d9b13256efe073ac3bc', '', 'http://pylonshq.com/docs/en/0.9.7/helpers/12', 1274783275, 1274783275),
('a4a8c325ed126b5d33f612c6a37e2e4f', '', 'http://pylonshq.com/docs/en/0.9.7/helpers/123', 1274783276, 1274783276),
('418821949e2b0f989f7677329dd635d7', '', 'http://pylonshq.com/docs/en/0.9.7/helpers/1234', 1274783277, 1274783277),
('59a77ce783b57e2908f46f1527427d34', '', 'http://pylonshq.com/docs/en/0.9.7/helpers/12346', 1274783279, 1274783279),
('ba732cceb1feee4da5ee23bf7e7f7337', '', 'http://pylonshq.com/docs/en/0.9.7/helpers/123466', 1274783281, 1274783281),
('b69e5e6bd88f87bc5739ebabf19402ee', '', 'http://pylonshq.com/docs/en/0.9.7/helpers/1234667', 1274783282, 1274783282),
('d6b82d3d60091d53726d79bb71bf9c40', '', 'http://pylonshq.com/docs/en/0.9.7/helpers/12346678', 1274783284, 1274783284),
('4df742340e34710cbd073ad05c4fbb91', '', 'http://pylonshq.com/docs/en/0.9.7/helpers/123466789', 1274783289, 1274783289),
('3a7c53951e8521a68468becaf1f3b644', '', 'http://pylonshq.com/docs/en/0.9.7/helpers/12346678910', 1274783294, 1274783294),
('14df9e4bc61033de94f567a086ca4aab', '', 'http://bel-epa.com/pylonsdocs/thirdparty/webhelpers/paginate.html', 1274788280, 1274788280);

-- --------------------------------------------------------

--
-- Table structure for table `feed_source_cnt`
--

CREATE TABLE IF NOT EXISTS `feed_source_cnt` (
  `id` char(32) NOT NULL,
  `update_time` int(11) NOT NULL,
  `cnt` int(11) NOT NULL,
  UNIQUE KEY `id` (`id`,`update_time`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `feed_source_cnt`
--


-- --------------------------------------------------------

--
-- Table structure for table `feed_source_item`
--

CREATE TABLE IF NOT EXISTS `feed_source_item` (
  `id` char(32) NOT NULL,
  `source_id` char(32) NOT NULL,
  `item` text NOT NULL,
  `add_time` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `feed_source_item`
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
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

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
-- Table structure for table `sessions`
--

CREATE TABLE IF NOT EXISTS `sessions` (
  `namespace` char(33) NOT NULL,
  `accessed` datetime NOT NULL,
  `created` datetime NOT NULL,
  `data` blob NOT NULL,
  PRIMARY KEY (`namespace`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `sessions`
--

INSERT INTO `sessions` (`namespace`, `accessed`, `created`, `data`) VALUES
('01d5375d8aff4108bd591990c2f6a46a', '2010-05-25 19:14:06', '2010-05-25 19:14:03', 0x80027d7101550773657373696f6e71027d710328550e5f61636365737365645f74696d6571044741d2feec3f9f6556550c617574685f757365725f69647105552439613932386235662d313137622d343235662d626136632d3561366365633365666235337106550e5f6372656174696f6e5f74696d6571074741d2feec3edcb3145509617574685f75736572710863746f72746f6973652e6d6f64656c0a55736572426173650a71092981710a7d710b2855125f73615f696e7374616e63655f7374617465710c6373716c616c6368656d792e6f726d2e73746174650a496e7374616e636553746174650a710d2981710e7d710f285508696e7374616e63657110680a55036b6579711168096806858671127562550d72656769737465725f74696d6571138a045b1ffa4b5505656d61696c711455177a68616e676a696179696e393940676d61696c2e636f6d711555046e69636b71165506e4bdb3e99fb37117550b72656769737465725f697071188a04c0a8021c550870617373776f7264711955206531306164633339343962613539616262653536653035376632306638383365711a55026964711b6806756275732e),
('3ee62abee5450b8519f077288e39773d', '2010-05-25 19:27:53', '2010-05-25 19:22:32', 0x80027d7101550773657373696f6e71027d710328550e5f61636365737365645f74696d6571044741d2feed0e708738550c617574685f757365725f69647105552439613932386235662d313137622d343235662d626136632d3561366365633365666235337106550e5f6372656174696f6e5f74696d6571074741d2feecbe156fef5509617574685f75736572710863746f72746f6973652e6d6f64656c0a55736572426173650a71092981710a7d710b2855125f73615f696e7374616e63655f7374617465710c6373716c616c6368656d792e6f726d2e73746174650a496e7374616e636553746174650a710d2981710e7d710f285508696e7374616e63657110680a55036b6579711168096806858671127562550d72656769737465725f74696d6571138a045b1ffa4b5505656d61696c711455177a68616e676a696179696e393940676d61696c2e636f6d711555046e69636b71165506e4bdb3e99fb37117550b72656769737465725f697071188a04c0a8021c550870617373776f7264711955206531306164633339343962613539616262653536653035376632306638383365711a55026964711b6806756275732e),
('62e9b0469d896acbb85ace7e03c0fcc3', '2010-05-25 19:14:35', '2010-05-25 19:14:17', 0x80027d7101550773657373696f6e71027d710328550e5f61636365737365645f74696d6571044741d2feec46f35476550c617574685f757365725f69647105552462623236313339332d653637632d343465652d616137382d3563323138666635393439357106550e5f6372656174696f6e5f74696d6571074741d2feec4266bdf15509617574685f75736572710863746f72746f6973652e6d6f64656c0a55736572426173650a71092981710a7d710b2855125f73615f696e7374616e63655f7374617465710c6373716c616c6368656d792e6f726d2e73746174650a496e7374616e636553746174650a710d2981710e7d710f285508696e7374616e63657110680a55036b6579711168096806858671127562550d72656769737465725f74696d6571138a04c052fa4b5505656d61696c711455117368756973687569407175616e2e636f6d711555046e69636b711655063132333435367117550b72656769737465725f697071188a04c0a8021c550870617373776f7264711955206531306164633339343962613539616262653536653035376632306638383365711a55026964711b6806756275732e),
('918e5423dc2ca5ff88f08467a4133804', '2010-05-25 19:21:40', '2010-05-25 19:15:22', 0x80027d7101550773657373696f6e71027d710328550c617574685f757365725f69647104552439613932386235662d313137622d343235662d626136632d3561366365633365666235337105550e5f61636365737365645f74696d6571064741d2feecb10da919550e5f6372656174696f6e5f74696d6571074741d2feec52975bd15509617574685f75736572710863746f72746f6973652e6d6f64656c0a55736572426173650a71092981710a7d710b2855125f73615f696e7374616e63655f7374617465710c6373716c616c6368656d792e6f726d2e73746174650a496e7374616e636553746174650a710d2981710e7d710f285508696e7374616e63657110680a55036b6579711168096805858671127562550d72656769737465725f74696d6571138a045b1ffa4b5505656d61696c711455177a68616e676a696179696e393940676d61696c2e636f6d711555046e69636b71165506e4bdb3e99fb37117550b72656769737465725f697071188a04c0a8021c550870617373776f7264711955206531306164633339343962613539616262653536653035376632306638383365711a55026964711b6805756275732e),
('b531bff0d242480eef303b7f99b13a19', '2010-05-25 19:51:59', '2010-05-25 19:44:05', 0x80027d7101550773657373696f6e71027d710328550e5f61636365737365645f74696d6571044741d2feee77d69164550c617574685f757365725f69647105552439613932386235662d313137622d343235662d626136632d3561366365633365666235337106550e5f6372656174696f6e5f74696d6571074741d2feee017606795509617574685f75736572710863746f72746f6973652e6d6f64656c0a55736572426173650a71092981710a7d710b2855125f73615f696e7374616e63655f7374617465710c6373716c616c6368656d792e6f726d2e73746174650a496e7374616e636553746174650a710d2981710e7d710f285508696e7374616e63657110680a55036b6579711168096806858671127562550d72656769737465725f74696d6571138a045b1ffa4b5505656d61696c711455177a68616e676a696179696e393940676d61696c2e636f6d711555046e69636b71165506e4bdb3e99fb37117550b72656769737465725f697071188a04c0a8021c550870617373776f7264711955206531306164633339343962613539616262653536653035376632306638383365711a55026964711b6806756275732e);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `id` char(40) NOT NULL,
  `email` char(50) NOT NULL,
  `nick` char(50) NOT NULL,
  `password` char(32) NOT NULL,
  `register_time` int(11) NOT NULL,
  `register_ip` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mail` (`email`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `email`, `nick`, `password`, `register_time`, `register_ip`) VALUES
('9a928b5f-117b-425f-ba6c-5a6cec3efb53', 'zhangjiayin99@gmail.com', 'ä½³éŸ³', 'e10adc3949ba59abbe56e057f20f883e', 1274683227, 469936320),
('b4e27fcc-f6b6-4dc3-b01a-684ce6572392', 'zhangjiayin99.1@gmail.com', 'sadfa', 'e10adc3949ba59abbe56e057f20f883e', 1274688979, 469936320),
('bb261393-e67c-44ee-aa78-5c218ff59495', 'shuishui@quan.com', '123456', 'e10adc3949ba59abbe56e057f20f883e', 1274696384, 469936320),
('a6902415-fb69-4cf1-9996-7fbe67152f71', 'zhang.jiayin@gmail.com', '123456', 'e10adc3949ba59abbe56e057f20f883e', 1274786192, 469936320);

-- --------------------------------------------------------

--
-- Table structure for table `user_profile`
--

CREATE TABLE IF NOT EXISTS `user_profile` (
  `id` char(40) NOT NULL,
  `birthday` datetime NOT NULL,
  `carrer` text NOT NULL,
  `google_account` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user_profile`
--

INSERT INTO `user_profile` (`id`, `birthday`, `carrer`, `google_account`) VALUES
('9a928b5f-117b-425f-ba6c-5a6cec3efb53', '0000-00-00 00:00:00', '', '{"password": "123456", "email": "zhangjiayin@gmail.com"}'),
('b4e27fcc-f6b6-4dc3-b01a-684ce6572392', '0000-00-00 00:00:00', '', '{"password": "123456", "email": "zhangjiayin@gmail.com"}'),
('bb261393-e67c-44ee-aa78-5c218ff59495', '0000-00-00 00:00:00', '', '{"password": "123456", "email": "shuishui@quan.com"}');

-- --------------------------------------------------------

--
-- Table structure for table `user_subscribe`
--

CREATE TABLE IF NOT EXISTS `user_subscribe` (
  `id` char(40) CHARACTER SET utf8 NOT NULL,
  `source_id` char(40) CHARACTER SET utf8 NOT NULL,
  `add_time` int(11) NOT NULL,
  UNIQUE KEY `uid` (`id`,`source_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_subscribe`
--

INSERT INTO `user_subscribe` (`id`, `source_id`, `add_time`) VALUES
('9a928b5f-117b-425f-ba6c-5a6cec3efb52', '925838ded0b9be1fa0342ae7b3a83143', 1274780183),
('9a928b5f-117b-425f-ba6c-5a6cec3efb53', 'cfb85bb93a02fbf67aee8c1e2bf09eb8', 1274780251),
('9a928b5f-117b-425f-ba6c-5a6cec3efb53', '1d9d724606b88b72c758e198baeb9b3b', 1274781485),
('9a928b5f-117b-425f-ba6c-5a6cec3efb53', 'cc06b29112938c81713d0d390e6793f2', 1274781515),
('9a928b5f-117b-425f-ba6c-5a6cec3efb53', '239da3b3749ea007355e236352332bd1', 1274781563),
('9a928b5f-117b-425f-ba6c-5a6cec3efb53', '306ed7b1081e3ba0cce8863f95404f66', 1274783274),
('9a928b5f-117b-425f-ba6c-5a6cec3efb53', 'aa0e6dbe458e2d9b13256efe073ac3bc', 1274783275),
('9a928b5f-117b-425f-ba6c-5a6cec3efb53', 'a4a8c325ed126b5d33f612c6a37e2e4f', 1274783276),
('9a928b5f-117b-425f-ba6c-5a6cec3efb53', '418821949e2b0f989f7677329dd635d7', 1274783277),
('9a928b5f-117b-425f-ba6c-5a6cec3efb53', '59a77ce783b57e2908f46f1527427d34', 1274783279),
('9a928b5f-117b-425f-ba6c-5a6cec3efb53', 'ba732cceb1feee4da5ee23bf7e7f7337', 1274783281),
('9a928b5f-117b-425f-ba6c-5a6cec3efb53', 'b69e5e6bd88f87bc5739ebabf19402ee', 1274783282),
('9a928b5f-117b-425f-ba6c-5a6cec3efb53', 'd6b82d3d60091d53726d79bb71bf9c40', 1274783284),
('9a928b5f-117b-425f-ba6c-5a6cec3efb53', '4df742340e34710cbd073ad05c4fbb91', 1274783289),
('9a928b5f-117b-425f-ba6c-5a6cec3efb53', '3a7c53951e8521a68468becaf1f3b644', 1274783294),
('9a928b5f-117b-425f-ba6c-5a6cec3efb53', '14df9e4bc61033de94f567a086ca4aab', 1274788280);
