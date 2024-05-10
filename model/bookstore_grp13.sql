-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 06, 2024 at 05:20 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bookstore_grp13`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `mngstore` varchar(50) NOT NULL,
  `adminID` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`mngstore`, `adminID`, `username`, `password`) VALUES
('', '1', 'admin', 'admin'),
('qweq', 'eqwwq', 'ewq', 'eqweqw'),
('test1', '1111', 'admin1', '1111'),
('test2', '2222', 'admin2', '2222'),
('test3', '3333', 'admin3', '3333'),
('test4', '4444', 'admin4', '4444'),
('test5', '5555', 'admin5', '5555'),
('test9', '12', 'dasdssasad', 'dasdsa');

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `mngstore` varchar(50) NOT NULL,
  `bookID` int(11) NOT NULL,
  `mngbkstore` varchar(50) NOT NULL,
  `bookTitle` varchar(50) NOT NULL,
  `bookquantityAvailability` int(11) NOT NULL,
  `bookpriceDetails` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`mngstore`, `bookID`, `mngbkstore`, `bookTitle`, `bookquantityAvailability`, `bookpriceDetails`) VALUES
('test1', 2, 'test1', 'testdev', 100, 111),
('test3', 3, '33', 'testdev3', 3, 333),
('test5', 5, '55', 'testdev5', 5, 555),
('test5', 7, 'dsada', 'dsadsad', 123, 2112);

-- --------------------------------------------------------

--
-- Table structure for table `reservationdetails`
--

CREATE TABLE `reservationdetails` (
  `createDate` longtext NOT NULL,
  `reservationdetailsID` int(11) NOT NULL,
  `expiryDate` date NOT NULL,
  `numofItems` int(11) NOT NULL,
  `totalAmount` int(11) NOT NULL,
  `studentID` int(11) NOT NULL,
  `items` longtext NOT NULL,
  `status` varchar(50) NOT NULL DEFAULT 'pending'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reservationdetails`
--

INSERT INTO `reservationdetails` (`createDate`, `reservationdetailsID`, `expiryDate`, `numofItems`, `totalAmount`, `studentID`, `items`, `status`) VALUES
('Mon Apr 29 2024 11:01:50 GMT+0800 (China Standard Time)', 36, '0000-00-00', 7, 4342, 3, '\"[{\\\"id\\\":5,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (Polo)\\\",\\\"price\\\":444,\\\"stock\\\":1,\\\"size\\\":\\\"XL\\\",\\\"image\\\":\\\"\\\"},{\\\"id\\\":6,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (PE)\\\",\\\"price\\\":555,\\\"stock\\\":1,\\\"size\\\":\\\"XXL\\\",\\\"image\\\":\\\"\\\"},{\\\"id\\\":1,\\\"category\\\":\\\"book\\\",\\\"name\\\":\\\"pharm\\\",\\\"price\\\":121,\\\"stock\\\":1,\\\"image\\\":\\\"\\\"},{\\\"id\\\":2,\\\"category\\\":\\\"book\\\",\\\"name\\\":\\\"testdev\\\",\\\"price\\\":111,\\\"stock\\\":1,\\\"image\\\":\\\"\\\"},{\\\"id\\\":7,\\\"category\\\":\\\"book\\\",\\\"name\\\":\\\"dsadsad\\\",\\\"price\\\":2112,\\\"stock\\\":1,\\\"image\\\":\\\"\\\"},{\\\"id\\\":5,\\\"category\\\":\\\"book\\\",\\\"name\\\":\\\"testdev5\\\",\\\"price\\\":555,\\\"stock\\\":1,\\\"image\\\":\\\"\\\"},{\\\"id\\\":4,\\\"category\\\":\\\"book\\\",\\\"name\\\":\\\"testdev4\\\",\\\"price\\\":444,\\\"stock\\\":1,\\\"image\\\":\\\"\\\"}]\"', 'completed'),
('Mon Apr 29 2024 11:04:47 GMT+0800 (China Standard Time)', 37, '0000-00-00', 7, 1897, 2, '\"[{\\\"id\\\":5,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (Polo)\\\",\\\"price\\\":444,\\\"stock\\\":1,\\\"size\\\":\\\"XL\\\",\\\"image\\\":\\\"\\\"},{\\\"id\\\":6,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (PE)\\\",\\\"price\\\":555,\\\"stock\\\":1,\\\"size\\\":\\\"XXL\\\",\\\"image\\\":\\\"\\\"},{\\\"id\\\":1,\\\"category\\\":\\\"book\\\",\\\"name\\\":\\\"pharm\\\",\\\"price\\\":121,\\\"stock\\\":1,\\\"image\\\":\\\"\\\"},{\\\"id\\\":2,\\\"category\\\":\\\"book\\\",\\\"name\\\":\\\"testdev\\\",\\\"price\\\":111,\\\"stock\\\":1,\\\"image\\\":\\\"\\\"},{\\\"id\\\":4,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (PE)\\\",\\\"price\\\":333,\\\"stock\\\":1,\\\"size\\\":\\\"L\\\",\\\"image\\\":\\\"\\\"},{\\\"id\\\":3,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (uniform)\\\",\\\"price\\\":222,\\\"stock\\\":1,\\\"size\\\":\\\"S\\\",\\\"image\\\":\\\"\\\"},{\\\"id\\\":2,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (uniform)\\\",\\\"price\\\":111,\\\"stock\\\":1,\\\"size\\\":\\\"M\\\",\\\"image\\\":\\\"\\\"}]\"', 'completed'),
('Mon Apr 29 2024 11:16:43 GMT+0800 (China Standard Time)', 38, '0000-00-00', 3, 666, 2, '\"[{\\\"id\\\":2,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (uniform)\\\",\\\"price\\\":111,\\\"stock\\\":1,\\\"size\\\":\\\"M\\\",\\\"image\\\":\\\"\\\"},{\\\"id\\\":3,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (uniform)\\\",\\\"price\\\":222,\\\"stock\\\":1,\\\"size\\\":\\\"S\\\",\\\"image\\\":\\\"\\\"},{\\\"id\\\":4,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (PE)\\\",\\\"price\\\":333,\\\"stock\\\":1,\\\"size\\\":\\\"L\\\",\\\"image\\\":\\\"\\\"}]\"', 'completed'),
('Mon Apr 29 2024 11:17:38 GMT+0800 (China Standard Time)', 39, '0000-00-00', 1, 222, 2, '\"[{\\\"id\\\":3,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (uniform)\\\",\\\"price\\\":222,\\\"stock\\\":1,\\\"size\\\":\\\"S\\\",\\\"image\\\":\\\"\\\"}]\"', 'completed'),
('Mon Apr 29 2024 11:17:45 GMT+0800 (China Standard Time)', 40, '0000-00-00', 3, 1110, 2, '\"[{\\\"id\\\":5,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (Polo)\\\",\\\"price\\\":444,\\\"stock\\\":1,\\\"size\\\":\\\"XL\\\",\\\"image\\\":\\\"\\\"},{\\\"id\\\":6,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (PE)\\\",\\\"price\\\":555,\\\"stock\\\":1,\\\"size\\\":\\\"XXL\\\",\\\"image\\\":\\\"\\\"},{\\\"id\\\":2,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (uniform)\\\",\\\"price\\\":111,\\\"stock\\\":1,\\\"size\\\":\\\"M\\\",\\\"image\\\":\\\"\\\"}]\"', 'completed'),
('Mon Apr 29 2024 11:19:24 GMT+0800 (China Standard Time)', 41, '0000-00-00', 3, 12654, 2, '\"[{\\\"id\\\":1,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (PE)\\\",\\\"price\\\":12321,\\\"stock\\\":1,\\\"size\\\":\\\"M\\\",\\\"image\\\":\\\"\\\"},{\\\"id\\\":2,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (uniform)\\\",\\\"price\\\":111,\\\"stock\\\":1,\\\"size\\\":\\\"M\\\",\\\"image\\\":\\\"\\\"},{\\\"id\\\":3,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (uniform)\\\",\\\"price\\\":222,\\\"stock\\\":1,\\\"size\\\":\\\"S\\\",\\\"image\\\":\\\"\\\"}]\"', 'declined'),
('Mon Apr 29 2024 11:19:57 GMT+0800 (China Standard Time)', 42, '0000-00-00', 2, 24642, 2, '\"[{\\\"id\\\":1,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (PE)\\\",\\\"price\\\":12321,\\\"stock\\\":1,\\\"size\\\":\\\"M\\\",\\\"image\\\":\\\"\\\"},{\\\"id\\\":1,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (PE)\\\",\\\"price\\\":12321,\\\"stock\\\":1,\\\"size\\\":\\\"XXXL\\\",\\\"image\\\":\\\"\\\"}]\"', 'declined'),
('Mon Apr 29 2024 11:39:51 GMT+0800 (China Standard Time)', 43, '0000-00-00', 4, 1554, 1, '\"[{\\\"id\\\":3,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (uniform)\\\",\\\"price\\\":222,\\\"stock\\\":1,\\\"size\\\":\\\"S\\\",\\\"image\\\":\\\"\\\"},{\\\"id\\\":5,\\\"category\\\":\\\"book\\\",\\\"name\\\":\\\"testdev5\\\",\\\"price\\\":555,\\\"stock\\\":1,\\\"image\\\":\\\"\\\"},{\\\"id\\\":4,\\\"category\\\":\\\"book\\\",\\\"name\\\":\\\"testdev4\\\",\\\"price\\\":444,\\\"stock\\\":1,\\\"image\\\":\\\"\\\"},{\\\"id\\\":3,\\\"category\\\":\\\"book\\\",\\\"name\\\":\\\"testdev3\\\",\\\"price\\\":333,\\\"stock\\\":1,\\\"image\\\":\\\"\\\"}]\"', 'declined'),
('Mon Apr 29 2024 11:46:58 GMT+0800 (China Standard Time)', 44, '0000-00-00', 4, 999, 1, '\"[{\\\"id\\\":2,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (uniform)\\\",\\\"price\\\":111,\\\"stock\\\":1,\\\"size\\\":\\\"M\\\",\\\"image\\\":\\\"\\\"},{\\\"id\\\":3,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (uniform)\\\",\\\"price\\\":222,\\\"stock\\\":1,\\\"size\\\":\\\"S\\\",\\\"image\\\":\\\"\\\"},{\\\"id\\\":4,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (PE)\\\",\\\"price\\\":333,\\\"stock\\\":1,\\\"size\\\":\\\"L\\\",\\\"image\\\":\\\"\\\"},{\\\"id\\\":4,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"School Uniform (PE)\\\",\\\"price\\\":333,\\\"stock\\\":1,\\\"size\\\":\\\"XXXL\\\",\\\"image\\\":\\\"\\\"}]\"', 'completed'),
('Mon Apr 29 2024 11:47:55 GMT+0800 (China Standard Time)', 45, '0000-00-00', 3, 3111, 1, '\"[{\\\"id\\\":4,\\\"category\\\":\\\"book\\\",\\\"name\\\":\\\"testdev4\\\",\\\"price\\\":444,\\\"stock\\\":1,\\\"image\\\":\\\"\\\"},{\\\"id\\\":5,\\\"category\\\":\\\"book\\\",\\\"name\\\":\\\"testdev5\\\",\\\"price\\\":555,\\\"stock\\\":1,\\\"image\\\":\\\"\\\"},{\\\"id\\\":7,\\\"category\\\":\\\"book\\\",\\\"name\\\":\\\"dsadsad\\\",\\\"price\\\":2112,\\\"stock\\\":1,\\\"image\\\":\\\"\\\"}]\"', 'completed'),
('Wed May 01 2024 20:39:29 GMT+0800 (Philippine Standard Time)', 46, '0000-00-00', 1, 333, 2, '\"[{\\\"id\\\":3,\\\"category\\\":\\\"book\\\",\\\"name\\\":\\\"testdev3\\\",\\\"price\\\":333,\\\"stock\\\":1,\\\"image\\\":\\\"\\\",\\\"mngstore\\\":\\\"test3\\\"}]\"', 'completed'),
('Wed May 01 2024 20:42:27 GMT+0800 (Philippine Standard Time)', 47, '0000-00-00', 3, 999, 2, '\"[{\\\"id\\\":2,\\\"category\\\":\\\"book\\\",\\\"name\\\":\\\"testdev\\\",\\\"price\\\":111,\\\"stock\\\":1,\\\"image\\\":\\\"\\\",\\\"mngstore\\\":\\\"test1\\\"},{\\\"id\\\":3,\\\"category\\\":\\\"book\\\",\\\"name\\\":\\\"testdev3\\\",\\\"price\\\":333,\\\"stock\\\":1,\\\"image\\\":\\\"\\\",\\\"mngstore\\\":\\\"test3\\\"},{\\\"id\\\":5,\\\"category\\\":\\\"book\\\",\\\"name\\\":\\\"testdev5\\\",\\\"price\\\":555,\\\"stock\\\":1,\\\"image\\\":\\\"\\\",\\\"mngstore\\\":\\\"test5\\\"}]\"', 'completed'),
('Wed May 01 2024 21:05:17 GMT+0800 (Philippine Standard Time)', 48, '0000-00-00', 2, 333, 2, '\"[{\\\"id\\\":2,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"uniform\\\",\\\"price\\\":111,\\\"stock\\\":1,\\\"size\\\":\\\"M\\\",\\\"image\\\":\\\"\\\",\\\"mngstore\\\":\\\"test1\\\"},{\\\"id\\\":3,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"uniform\\\",\\\"price\\\":222,\\\"stock\\\":1,\\\"size\\\":\\\"S\\\",\\\"image\\\":\\\"\\\",\\\"mngstore\\\":\\\"test2\\\"}]\"', 'completed'),
('Wed May 01 2024 21:22:34 GMT+0800 (Philippine Standard Time)', 49, '0000-00-00', 2, 555, 2, '\"[{\\\"id\\\":3,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"uniform\\\",\\\"price\\\":222,\\\"stock\\\":1,\\\"size\\\":\\\"S\\\",\\\"image\\\":\\\"\\\",\\\"mngstore\\\":\\\"test2\\\"},{\\\"id\\\":4,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"PE Senior High\\\",\\\"price\\\":333,\\\"stock\\\":1,\\\"size\\\":\\\"L\\\",\\\"image\\\":\\\"\\\",\\\"mngstore\\\":\\\"test3\\\"}]\"', 'completed'),
('Wed May 01 2024 23:09:12 GMT+0800 (Philippine Standard Time)', 50, '0000-00-00', 3, 611, 4, '\"[{\\\"id\\\":2,\\\"category\\\":\\\"book\\\",\\\"name\\\":\\\"testdev\\\",\\\"price\\\":111,\\\"stock\\\":1,\\\"image\\\":\\\"\\\",\\\"mngstore\\\":\\\"test1\\\"},{\\\"id\\\":2,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"College Uniform\\\",\\\"price\\\":250,\\\"stock\\\":1,\\\"size\\\":\\\"M\\\",\\\"image\\\":\\\"\\\",\\\"mngstore\\\":\\\"test1\\\"},{\\\"id\\\":2,\\\"category\\\":\\\"uniform\\\",\\\"name\\\":\\\"College Uniform\\\",\\\"price\\\":250,\\\"stock\\\":1,\\\"size\\\":\\\"XXXL\\\",\\\"image\\\":\\\"\\\",\\\"mngstore\\\":\\\"test1\\\"}]\"', 'completed');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `studentID` int(11) NOT NULL,
  `firstName` varchar(100) NOT NULL,
  `lastName` varchar(100) NOT NULL,
  `uicEmail` varchar(250) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`studentID`, `firstName`, `lastName`, `uicEmail`, `password`) VALUES
(1, 'Raldin', 'Casidar', 'raldin.disomimba13@gmail.com', 'dindin23'),
(2, 'Juan', 'Luna', 'marasigan@gmail.com', 'dindin23'),
(3, 'Sheen', 'Lee', 'sheenlee@gmail.com', 'dindin23'),
(4, 'Lemwel', 'Bayson', 'Lem@uic.edu.ph', '123213212');

-- --------------------------------------------------------

--
-- Table structure for table `uniform`
--

CREATE TABLE `uniform` (
  `mngstore` varchar(50) NOT NULL,
  `uniformID` int(11) NOT NULL,
  `type` varchar(30) NOT NULL,
  `size` varchar(30) NOT NULL,
  `uniformQuantityAvailability` int(11) NOT NULL,
  `uniformPriceDetails` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `uniform`
--

INSERT INTO `uniform` (`mngstore`, `uniformID`, `type`, `size`, `uniformQuantityAvailability`, `uniformPriceDetails`) VALUES
('test1', 2, 'College Uniform', 'M', 100, 250),
('test2', 3, 'uniform', 'S', 22, 222),
('test3', 4, 'PE Senior High', 'L', 3, 333),
('test4', 5, 'Polo', 'XL', 4, 444),
('test5', 6, 'PE', 'XXL', 5, 555),
('test', 13, 'PE22', 'XL', 100, 50);

-- --------------------------------------------------------

--
-- Table structure for table `uniformdetails`
--

CREATE TABLE `uniformdetails` (
  `uniformreservationID` int(11) NOT NULL,
  `reservationdetailsID` int(11) NOT NULL,
  `uniformID` int(11) NOT NULL,
  `uniformQuantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `uniformdetails`
--

INSERT INTO `uniformdetails` (`uniformreservationID`, `reservationdetailsID`, `uniformID`, `uniformQuantity`) VALUES
(1, 3, 1, 11),
(2, 4, 1, 22),
(4, 1, 5, 44),
(5, 2, 1, 55);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`mngstore`);

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`bookID`),
  ADD KEY `mngstore` (`mngstore`);

--
-- Indexes for table `reservationdetails`
--
ALTER TABLE `reservationdetails`
  ADD PRIMARY KEY (`reservationdetailsID`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`studentID`);

--
-- Indexes for table `uniform`
--
ALTER TABLE `uniform`
  ADD PRIMARY KEY (`uniformID`),
  ADD KEY `mngstore` (`mngstore`);

--
-- Indexes for table `uniformdetails`
--
ALTER TABLE `uniformdetails`
  ADD PRIMARY KEY (`uniformreservationID`),
  ADD KEY `uniformID` (`uniformID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `book`
--
ALTER TABLE `book`
  MODIFY `bookID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `reservationdetails`
--
ALTER TABLE `reservationdetails`
  MODIFY `reservationdetailsID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `studentID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `uniform`
--
ALTER TABLE `uniform`
  MODIFY `uniformID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `uniformdetails`
--
ALTER TABLE `uniformdetails`
  MODIFY `uniformreservationID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
