-- MySQL dump 10.13  Distrib 8.0.12, for macos10.13 (x86_64)
--
-- Host: localhost    Database: ID
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `BST`
--

DROP TABLE IF EXISTS `BST`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `BST` (
  `UID` varchar(30) NOT NULL,
  `BID` varchar(30) NOT NULL,
  `IDB` tinyint(1) DEFAULT NULL,
  `IQ` float DEFAULT NULL,
  `ID_Type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`BID`),
  KEY `fkbst` (`UID`),
  CONSTRAINT `fkbst` FOREIGN KEY (`UID`) REFERENCES `child` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BST`
--

LOCK TABLES `BST` WRITE;
/*!40000 ALTER TABLE `BST` DISABLE KEYS */;
INSERT INTO `BST` VALUES ('1bognhbFAvOjBqDeDFpPzL7RUj02','1bognhbFAvOjBqDeDFpPzL7RUj02',0,129.6,'NOT ID'),('1JejQH6R3DaM5WYY8QIZEq0LJMo1','1JejQH6R3DaM5WYY8QIZEq0LJMo1',0,150.4,'NOT ID'),('24iby93N2mhyKwJF4pdyKkHChku2','24iby93N2mhyKwJF4pdyKkHChku2',0,151.6,'NOT ID'),('25','25',1,66.8667,'Mild ID'),('26','26',1,50,'Mild ID'),('41PBOElAoCS5ZmYhbCLtkoeqeE03','41PBOElAoCS5ZmYhbCLtkoeqeE03',0,100,'NOT ID'),('5pUxKTHISCXBRR1A9yRqefnLnpy1','5pUxKTHISCXBRR1A9yRqefnLnpy1',1,67.1333,'Mild ID'),('7fb3YgTttRUO524HSoQW4xsFnRm1','7fb3YgTttRUO524HSoQW4xsFnRm1',0,101.029,'NOT ID'),('AsMtX5qSEkgduxATZvZzm2e2ca83','AsMtX5qSEkgduxATZvZzm2e2ca83',0,111.111,'NOT ID'),('B1sRQGiqGpciZiXdbCEkYjB0iXa2','B1sRQGiqGpciZiXdbCEkYjB0iXa2',1,89.9556,'Boderline ID'),('bEOSMcdGN9OQJyv8aTrD3Gvmvhb2','bEOSMcdGN9OQJyv8aTrD3Gvmvhb2',1,50.075,'Mild ID'),('EJGHXOkydOMMpEHhQDvdw6Vc5rH3','EJGHXOkydOMMpEHhQDvdw6Vc5rH3',1,45.4444,'Moderate ID'),('g6pTMQWqKMaom437eqIUGcSvJBA3','g6pTMQWqKMaom437eqIUGcSvJBA3',0,134.933,'NOT ID'),('gNRSHIvAGEPwNoOpbfPFcF3fwRm2','gNRSHIvAGEPwNoOpbfPFcF3fwRm2',0,151.2,'NOT ID'),('HKttyTxIhtSqXolAAJTMka5ZNf83','HKttyTxIhtSqXolAAJTMka5ZNf83',0,134.133,'NOT ID'),('J6vGWibfcKYRoM3vuoQEVX9xqp52','J6vGWibfcKYRoM3vuoQEVX9xqp52',1,75.3,'Boderline ID'),('JjZw94xcPZhXpTswOEMvBRifL5F3','JjZw94xcPZhXpTswOEMvBRifL5F3',0,101.067,'NOT ID'),('k4SOzA9qKCchvLcPvDYq7IIAD3n1','k4SOzA9qKCchvLcPvDYq7IIAD3n1',0,133.733,'NOT ID'),('PHxLUkJUqdZ1U3nn91SY3quulaJ3','PHxLUkJUqdZ1U3nn91SY3quulaJ3',0,111.111,'NOT ID'),('POQpZRGYJPagtcRSe9QmJcuF3lF2','POQpZRGYJPagtcRSe9QmJcuF3lF2',0,125,'NOT ID'),('PSct0i7U4AOO64UJ0kawdjdmj0x2','PSct0i7U4AOO64UJ0kawdjdmj0x2',1,66.8667,'Mild ID'),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1','wmP5aqWAA9ZeAenjTHfEbcPjVMy1',0,100.686,'NOT ID'),('xRUrJ9zZ5eOseQevk4GNxTCtZj03','xRUrJ9zZ5eOseQevk4GNxTCtZj03',0,100,'NOT ID'),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1','YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',1,78.3111,'Boderline ID'),('YhkwMGvtBVQ5NtZLk82kgm6nFFh1','YhkwMGvtBVQ5NtZLk82kgm6nFFh1',1,22.2222,'Severe ID'),('YWY7SzsQoObHzqjfmd6p5FqHcGe2','YWY7SzsQoObHzqjfmd6p5FqHcGe2',1,67.4667,'Mild ID'),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2','ZtKOYnNo39QhUtrpWXi9qBT8BHv2',1,89.6889,'Borderline ID');
/*!40000 ALTER TABLE `BST` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BST10`
--

DROP TABLE IF EXISTS `BST10`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `BST10` (
  `BID` varchar(30) DEFAULT NULL,
  `q1` int(11) DEFAULT NULL,
  `q2` int(11) DEFAULT NULL,
  `q3` int(11) DEFAULT NULL,
  `q4` int(11) DEFAULT NULL,
  `q5` int(11) DEFAULT NULL,
  KEY `b10` (`BID`),
  CONSTRAINT `b10` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BST10`
--

LOCK TABLES `BST10` WRITE;
/*!40000 ALTER TABLE `BST10` DISABLE KEYS */;
INSERT INTO `BST10` VALUES ('g6pTMQWqKMaom437eqIUGcSvJBA3',0,1,1,1,0),('gNRSHIvAGEPwNoOpbfPFcF3fwRm2',1,1,1,1,1),('k4SOzA9qKCchvLcPvDYq7IIAD3n1',1,1,0,1,0),('7fb3YgTttRUO524HSoQW4xsFnRm1',1,1,0,1,0),('1bognhbFAvOjBqDeDFpPzL7RUj02',1,1,1,1,0),('PHxLUkJUqdZ1U3nn91SY3quulaJ3',1,1,1,1,1),('JjZw94xcPZhXpTswOEMvBRifL5F3',1,0,1,1,1),('41PBOElAoCS5ZmYhbCLtkoeqeE03',1,1,1,1,0),('24iby93N2mhyKwJF4pdyKkHChku2',1,1,1,1,1),('1JejQH6R3DaM5WYY8QIZEq0LJMo1',1,1,1,1,1),('HKttyTxIhtSqXolAAJTMka5ZNf83',1,1,1,1,0),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1',0,1,0,0,0),('POQpZRGYJPagtcRSe9QmJcuF3lF2',1,1,1,1,1),('xRUrJ9zZ5eOseQevk4GNxTCtZj03',1,1,0,1,0),('B1sRQGiqGpciZiXdbCEkYjB0iXa2',1,1,1,1,1),('AsMtX5qSEkgduxATZvZzm2e2ca83',1,1,1,1,1),('YWY7SzsQoObHzqjfmd6p5FqHcGe2',0,1,0,0,0),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',1,1,0,0,0),('J6vGWibfcKYRoM3vuoQEVX9xqp52',0,1,1,0,0);
/*!40000 ALTER TABLE `BST10` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BST3`
--

DROP TABLE IF EXISTS `BST3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `BST3` (
  `BID` varchar(30) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  `q5` int(11) NOT NULL,
  KEY `fk3` (`BID`),
  CONSTRAINT `fk3` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BST3`
--

LOCK TABLES `BST3` WRITE;
/*!40000 ALTER TABLE `BST3` DISABLE KEYS */;
INSERT INTO `BST3` VALUES ('g6pTMQWqKMaom437eqIUGcSvJBA3',1,1,1,1,1),('gNRSHIvAGEPwNoOpbfPFcF3fwRm2',1,1,1,1,1),('k4SOzA9qKCchvLcPvDYq7IIAD3n1',1,1,1,1,1),('7fb3YgTttRUO524HSoQW4xsFnRm1',1,1,1,1,1),('1bognhbFAvOjBqDeDFpPzL7RUj02',1,1,1,1,1),('PHxLUkJUqdZ1U3nn91SY3quulaJ3',1,1,1,1,1),('JjZw94xcPZhXpTswOEMvBRifL5F3',1,1,1,1,1),('41PBOElAoCS5ZmYhbCLtkoeqeE03',1,1,1,1,1),('24iby93N2mhyKwJF4pdyKkHChku2',1,1,1,1,1),('1JejQH6R3DaM5WYY8QIZEq0LJMo1',1,1,1,1,1),('HKttyTxIhtSqXolAAJTMka5ZNf83',1,1,1,1,1),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1',1,1,1,1,1),('POQpZRGYJPagtcRSe9QmJcuF3lF2',1,1,1,1,1),('xRUrJ9zZ5eOseQevk4GNxTCtZj03',1,1,1,1,1),('B1sRQGiqGpciZiXdbCEkYjB0iXa2',1,1,1,1,1),('AsMtX5qSEkgduxATZvZzm2e2ca83',1,1,1,1,1),('EJGHXOkydOMMpEHhQDvdw6Vc5rH3',1,1,1,1,0),('YWY7SzsQoObHzqjfmd6p5FqHcGe2',1,1,1,0,0),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',1,1,1,1,1),('J6vGWibfcKYRoM3vuoQEVX9xqp52',1,1,0,1,0),('5pUxKTHISCXBRR1A9yRqefnLnpy1',1,1,1,1,0),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2',1,1,1,1,1),('bEOSMcdGN9OQJyv8aTrD3Gvmvhb2',1,0,0,1,0),('PSct0i7U4AOO64UJ0kawdjdmj0x2',0,0,1,1,1),('25',0,0,1,1,1);
/*!40000 ALTER TABLE `BST3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BST4`
--

DROP TABLE IF EXISTS `BST4`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `BST4` (
  `BID` varchar(30) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  KEY `fk4` (`BID`),
  CONSTRAINT `fk4` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BST4`
--

LOCK TABLES `BST4` WRITE;
/*!40000 ALTER TABLE `BST4` DISABLE KEYS */;
INSERT INTO `BST4` VALUES ('g6pTMQWqKMaom437eqIUGcSvJBA3',1,1,1,1),('gNRSHIvAGEPwNoOpbfPFcF3fwRm2',1,1,1,1),('k4SOzA9qKCchvLcPvDYq7IIAD3n1',1,1,1,1),('7fb3YgTttRUO524HSoQW4xsFnRm1',1,1,1,1),('1bognhbFAvOjBqDeDFpPzL7RUj02',1,1,1,1),('PHxLUkJUqdZ1U3nn91SY3quulaJ3',1,1,1,1),('JjZw94xcPZhXpTswOEMvBRifL5F3',1,1,1,1),('41PBOElAoCS5ZmYhbCLtkoeqeE03',1,1,1,1),('24iby93N2mhyKwJF4pdyKkHChku2',1,1,1,1),('1JejQH6R3DaM5WYY8QIZEq0LJMo1',1,1,1,1),('HKttyTxIhtSqXolAAJTMka5ZNf83',1,1,1,1),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1',1,1,1,1),('POQpZRGYJPagtcRSe9QmJcuF3lF2',1,1,1,1),('xRUrJ9zZ5eOseQevk4GNxTCtZj03',1,1,1,1),('B1sRQGiqGpciZiXdbCEkYjB0iXa2',1,1,1,1),('AsMtX5qSEkgduxATZvZzm2e2ca83',1,1,1,1),('EJGHXOkydOMMpEHhQDvdw6Vc5rH3',1,1,0,1),('YWY7SzsQoObHzqjfmd6p5FqHcGe2',1,1,1,1),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',1,1,1,1),('J6vGWibfcKYRoM3vuoQEVX9xqp52',1,1,1,1),('5pUxKTHISCXBRR1A9yRqefnLnpy1',0,1,1,1),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2',1,1,1,1),('bEOSMcdGN9OQJyv8aTrD3Gvmvhb2',0,0,0,1),('PSct0i7U4AOO64UJ0kawdjdmj0x2',0,0,1,1),('25',0,0,1,1);
/*!40000 ALTER TABLE `BST4` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BST5`
--

DROP TABLE IF EXISTS `BST5`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `BST5` (
  `BID` varchar(30) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  `q5` int(11) NOT NULL,
  KEY `fk5` (`BID`),
  CONSTRAINT `fk5` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BST5`
--

LOCK TABLES `BST5` WRITE;
/*!40000 ALTER TABLE `BST5` DISABLE KEYS */;
INSERT INTO `BST5` VALUES ('g6pTMQWqKMaom437eqIUGcSvJBA3',1,1,1,1,1),('gNRSHIvAGEPwNoOpbfPFcF3fwRm2',1,1,1,1,1),('k4SOzA9qKCchvLcPvDYq7IIAD3n1',1,1,1,0,1),('7fb3YgTttRUO524HSoQW4xsFnRm1',1,1,1,0,1),('1bognhbFAvOjBqDeDFpPzL7RUj02',1,1,1,1,1),('PHxLUkJUqdZ1U3nn91SY3quulaJ3',1,1,1,1,1),('JjZw94xcPZhXpTswOEMvBRifL5F3',1,1,1,1,1),('41PBOElAoCS5ZmYhbCLtkoeqeE03',1,1,1,1,1),('24iby93N2mhyKwJF4pdyKkHChku2',1,1,1,1,1),('1JejQH6R3DaM5WYY8QIZEq0LJMo1',1,1,1,0,1),('HKttyTxIhtSqXolAAJTMka5ZNf83',1,1,1,0,0),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1',1,1,0,1,1),('POQpZRGYJPagtcRSe9QmJcuF3lF2',1,1,1,1,1),('xRUrJ9zZ5eOseQevk4GNxTCtZj03',1,1,1,0,1),('B1sRQGiqGpciZiXdbCEkYjB0iXa2',1,1,1,0,1),('AsMtX5qSEkgduxATZvZzm2e2ca83',1,1,1,1,1),('EJGHXOkydOMMpEHhQDvdw6Vc5rH3',1,1,0,0,1),('YWY7SzsQoObHzqjfmd6p5FqHcGe2',1,1,0,0,1),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',1,1,0,0,1),('J6vGWibfcKYRoM3vuoQEVX9xqp52',1,0,0,0,1),('5pUxKTHISCXBRR1A9yRqefnLnpy1',1,1,0,1,1),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2',1,1,1,0,1),('bEOSMcdGN9OQJyv8aTrD3Gvmvhb2',0,1,0,0,1);
/*!40000 ALTER TABLE `BST5` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BST6`
--

DROP TABLE IF EXISTS `BST6`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `BST6` (
  `BID` varchar(30) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  `q5` int(11) NOT NULL,
  KEY `fk6` (`BID`),
  CONSTRAINT `fk6` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BST6`
--

LOCK TABLES `BST6` WRITE;
/*!40000 ALTER TABLE `BST6` DISABLE KEYS */;
INSERT INTO `BST6` VALUES ('g6pTMQWqKMaom437eqIUGcSvJBA3',1,1,1,1,1),('gNRSHIvAGEPwNoOpbfPFcF3fwRm2',1,1,1,1,1),('k4SOzA9qKCchvLcPvDYq7IIAD3n1',1,1,1,0,1),('7fb3YgTttRUO524HSoQW4xsFnRm1',1,1,1,0,1),('1bognhbFAvOjBqDeDFpPzL7RUj02',1,1,1,1,1),('PHxLUkJUqdZ1U3nn91SY3quulaJ3',1,1,1,1,1),('JjZw94xcPZhXpTswOEMvBRifL5F3',1,1,1,1,1),('41PBOElAoCS5ZmYhbCLtkoeqeE03',1,1,1,1,1),('24iby93N2mhyKwJF4pdyKkHChku2',1,1,1,1,1),('1JejQH6R3DaM5WYY8QIZEq0LJMo1',1,1,1,0,1),('HKttyTxIhtSqXolAAJTMka5ZNf83',1,1,1,0,1),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1',1,1,1,0,0),('POQpZRGYJPagtcRSe9QmJcuF3lF2',1,1,1,1,1),('xRUrJ9zZ5eOseQevk4GNxTCtZj03',0,1,1,0,1),('B1sRQGiqGpciZiXdbCEkYjB0iXa2',1,1,1,0,1),('AsMtX5qSEkgduxATZvZzm2e2ca83',1,1,1,1,1),('EJGHXOkydOMMpEHhQDvdw6Vc5rH3',1,1,1,0,0),('YWY7SzsQoObHzqjfmd6p5FqHcGe2',1,1,1,0,1),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',1,1,1,0,0),('J6vGWibfcKYRoM3vuoQEVX9xqp52',0,1,1,0,0),('5pUxKTHISCXBRR1A9yRqefnLnpy1',1,1,0,0,0),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2',1,1,1,0,1);
/*!40000 ALTER TABLE `BST6` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BST7`
--

DROP TABLE IF EXISTS `BST7`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `BST7` (
  `BID` varchar(30) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  `q5` int(11) NOT NULL,
  KEY `fk7` (`BID`),
  CONSTRAINT `fk7` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BST7`
--

LOCK TABLES `BST7` WRITE;
/*!40000 ALTER TABLE `BST7` DISABLE KEYS */;
INSERT INTO `BST7` VALUES ('g6pTMQWqKMaom437eqIUGcSvJBA3',1,1,1,0,1),('gNRSHIvAGEPwNoOpbfPFcF3fwRm2',1,0,1,1,1),('k4SOzA9qKCchvLcPvDYq7IIAD3n1',1,0,1,1,1),('7fb3YgTttRUO524HSoQW4xsFnRm1',1,1,1,0,1),('1bognhbFAvOjBqDeDFpPzL7RUj02',1,1,1,1,1),('PHxLUkJUqdZ1U3nn91SY3quulaJ3',1,1,1,1,1),('JjZw94xcPZhXpTswOEMvBRifL5F3',1,1,1,1,1),('41PBOElAoCS5ZmYhbCLtkoeqeE03',1,1,1,0,1),('24iby93N2mhyKwJF4pdyKkHChku2',1,1,1,1,1),('1JejQH6R3DaM5WYY8QIZEq0LJMo1',1,1,1,1,1),('HKttyTxIhtSqXolAAJTMka5ZNf83',1,0,1,0,1),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1',1,1,1,1,1),('POQpZRGYJPagtcRSe9QmJcuF3lF2',1,1,1,1,1),('xRUrJ9zZ5eOseQevk4GNxTCtZj03',0,1,1,0,1),('B1sRQGiqGpciZiXdbCEkYjB0iXa2',1,1,1,0,1),('AsMtX5qSEkgduxATZvZzm2e2ca83',1,1,1,1,1),('YWY7SzsQoObHzqjfmd6p5FqHcGe2',0,0,1,0,1),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',1,0,1,0,1),('J6vGWibfcKYRoM3vuoQEVX9xqp52',1,0,1,0,1),('5pUxKTHISCXBRR1A9yRqefnLnpy1',1,1,1,0,1),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2',1,1,1,0,1);
/*!40000 ALTER TABLE `BST7` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BST8`
--

DROP TABLE IF EXISTS `BST8`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `BST8` (
  `BID` varchar(30) DEFAULT NULL,
  `q1` int(11) DEFAULT NULL,
  `q2` int(11) DEFAULT NULL,
  `q3` int(11) DEFAULT NULL,
  `q4` int(11) DEFAULT NULL,
  `q5` int(11) DEFAULT NULL,
  KEY `b8` (`BID`),
  CONSTRAINT `b8` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BST8`
--

LOCK TABLES `BST8` WRITE;
/*!40000 ALTER TABLE `BST8` DISABLE KEYS */;
INSERT INTO `BST8` VALUES ('g6pTMQWqKMaom437eqIUGcSvJBA3',1,1,1,0,1),('gNRSHIvAGEPwNoOpbfPFcF3fwRm2',1,1,1,1,1),('k4SOzA9qKCchvLcPvDYq7IIAD3n1',1,1,1,0,1),('7fb3YgTttRUO524HSoQW4xsFnRm1',1,0,0,0,1),('1bognhbFAvOjBqDeDFpPzL7RUj02',1,1,1,1,1),('PHxLUkJUqdZ1U3nn91SY3quulaJ3',1,1,1,1,1),('JjZw94xcPZhXpTswOEMvBRifL5F3',1,1,1,1,1),('41PBOElAoCS5ZmYhbCLtkoeqeE03',1,1,1,1,1),('24iby93N2mhyKwJF4pdyKkHChku2',1,1,1,1,1),('1JejQH6R3DaM5WYY8QIZEq0LJMo1',1,1,1,1,1),('HKttyTxIhtSqXolAAJTMka5ZNf83',1,1,1,1,1),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1',1,0,1,0,0),('POQpZRGYJPagtcRSe9QmJcuF3lF2',1,1,1,1,1),('xRUrJ9zZ5eOseQevk4GNxTCtZj03',1,1,1,1,1),('B1sRQGiqGpciZiXdbCEkYjB0iXa2',1,1,1,1,1),('AsMtX5qSEkgduxATZvZzm2e2ca83',1,1,1,1,1),('YWY7SzsQoObHzqjfmd6p5FqHcGe2',1,0,1,0,0),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',1,0,1,1,0),('J6vGWibfcKYRoM3vuoQEVX9xqp52',1,0,0,1,0),('5pUxKTHISCXBRR1A9yRqefnLnpy1',1,0,0,0,0),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2',1,0,1,1,0);
/*!40000 ALTER TABLE `BST8` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BST9`
--

DROP TABLE IF EXISTS `BST9`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `BST9` (
  `BID` varchar(30) DEFAULT NULL,
  `q1` int(11) DEFAULT NULL,
  `q2` int(11) DEFAULT NULL,
  `q3` int(11) DEFAULT NULL,
  `q4` int(11) DEFAULT NULL,
  `q5` int(11) DEFAULT NULL,
  KEY `b9` (`BID`),
  CONSTRAINT `b9` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BST9`
--

LOCK TABLES `BST9` WRITE;
/*!40000 ALTER TABLE `BST9` DISABLE KEYS */;
INSERT INTO `BST9` VALUES ('g6pTMQWqKMaom437eqIUGcSvJBA3',0,0,1,1,1),('gNRSHIvAGEPwNoOpbfPFcF3fwRm2',0,1,1,1,1),('k4SOzA9qKCchvLcPvDYq7IIAD3n1',0,0,1,0,1),('7fb3YgTttRUO524HSoQW4xsFnRm1',0,0,0,0,1),('1bognhbFAvOjBqDeDFpPzL7RUj02',1,0,1,1,1),('PHxLUkJUqdZ1U3nn91SY3quulaJ3',1,1,1,1,1),('JjZw94xcPZhXpTswOEMvBRifL5F3',1,1,1,1,1),('41PBOElAoCS5ZmYhbCLtkoeqeE03',0,0,0,1,1),('24iby93N2mhyKwJF4pdyKkHChku2',1,0,1,1,1),('1JejQH6R3DaM5WYY8QIZEq0LJMo1',0,0,1,1,1),('HKttyTxIhtSqXolAAJTMka5ZNf83',0,0,1,1,1),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1',0,0,1,0,1),('POQpZRGYJPagtcRSe9QmJcuF3lF2',1,1,1,1,1),('xRUrJ9zZ5eOseQevk4GNxTCtZj03',0,0,1,0,1),('B1sRQGiqGpciZiXdbCEkYjB0iXa2',0,0,1,0,1),('AsMtX5qSEkgduxATZvZzm2e2ca83',1,1,1,1,1),('YWY7SzsQoObHzqjfmd6p5FqHcGe2',0,0,1,1,1),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',0,0,1,1,1),('J6vGWibfcKYRoM3vuoQEVX9xqp52',0,0,0,1,1),('5pUxKTHISCXBRR1A9yRqefnLnpy1',0,0,1,1,1),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2',0,0,1,1,1);
/*!40000 ALTER TABLE `BST9` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `c`
--

DROP TABLE IF EXISTS `c`;
/*!50001 DROP VIEW IF EXISTS `c`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `c` AS SELECT 
 1 AS `UID`,
 1 AS `Name`,
 1 AS `Age`,
 1 AS `ID`,
 1 AS `Gender`,
 1 AS `Score`,
 1 AS `IDR`,
 1 AS `Forward_Score`,
 1 AS `Backward_Score`,
 1 AS `Raw_score`,
 1 AS `IDD`,
 1 AS `Std_score`,
 1 AS `Per_score`,
 1 AS `BID`,
 1 AS `IDB`,
 1 AS `IQ`,
 1 AS `ID_Type`,
 1 AS `GID`,
 1 AS `Percentile`,
 1 AS `IDG`,
 1 AS `VID`,
 1 AS `IDV`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `Child`
--

DROP TABLE IF EXISTS `Child`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Child` (
  `UID` varchar(30) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Age` float NOT NULL,
  `ID` tinyint(1) DEFAULT NULL,
  `Gender` char(1) DEFAULT NULL,
  `DateOfTest` date DEFAULT NULL,
  `RID` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`UID`),
  KEY `refer` (`RID`),
  CONSTRAINT `refer` FOREIGN KEY (`RID`) REFERENCES `child` (`uid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Child`
--

LOCK TABLES `Child` WRITE;
/*!40000 ALTER TABLE `Child` DISABLE KEYS */;
INSERT INTO `Child` VALUES ('1bognhbFAvOjBqDeDFpPzL7RUj02','Swarnima _07',7,0,'F','2018-09-26','1bognhbFAvOjBqDeDFpPzL7RUj02'),('1JejQH6R3DaM5WYY8QIZEq0LJMo1','Anuj _6',6,0,'M','2018-09-26','1JejQH6R3DaM5WYY8QIZEq0LJMo1'),('24iby93N2mhyKwJF4pdyKkHChku2','Paridhi _6',6,0,'F','2018-09-26','24iby93N2mhyKwJF4pdyKkHChku2'),('25','Admin',6,1,'M','2018-10-29','PSct0i7U4AOO64UJ0kawdjdmj0x2'),('26','',6,1,'M','2018-10-29','PSct0i7U4AOO64UJ0kawdjdmj0x2'),('41PBOElAoCS5ZmYhbCLtkoeqeE03','Atharv _10',9,0,'M','2018-09-26','41PBOElAoCS5ZmYhbCLtkoeqeE03'),('5pUxKTHISCXBRR1A9yRqefnLnpy1','Dheeraj _11',9,1,'M','2018-09-24','5pUxKTHISCXBRR1A9yRqefnLnpy1'),('7fb3YgTttRUO524HSoQW4xsFnRm1','Gautam _07',7,0,'M','2018-09-26','7fb3YgTttRUO524HSoQW4xsFnRm1'),('AsMtX5qSEkgduxATZvZzm2e2ca83','Devarchita _9',9,0,'F','2018-09-26','AsMtX5qSEkgduxATZvZzm2e2ca83'),('B1sRQGiqGpciZiXdbCEkYjB0iXa2','Suhas _9',9,0,'M','2018-09-26','B1sRQGiqGpciZiXdbCEkYjB0iXa2'),('bEOSMcdGN9OQJyv8aTrD3Gvmvhb2','Gautam',8,1,'M','2018-10-26','bEOSMcdGN9OQJyv8aTrD3Gvmvhb2'),('EJGHXOkydOMMpEHhQDvdw6Vc5rH3','Lalith _10',9,1,'M','2018-09-24','EJGHXOkydOMMpEHhQDvdw6Vc5rH3'),('g6pTMQWqKMaom437eqIUGcSvJBA3','Tanav _06',6,0,'M','2018-09-26','g6pTMQWqKMaom437eqIUGcSvJBA3'),('gNRSHIvAGEPwNoOpbfPFcF3fwRm2','Akhilan1.0 _6',6,0,'M','2018-09-26','gNRSHIvAGEPwNoOpbfPFcF3fwRm2'),('HKttyTxIhtSqXolAAJTMka5ZNf83','Charu _6',6,0,'F','2018-09-26','HKttyTxIhtSqXolAAJTMka5ZNf83'),('J6vGWibfcKYRoM3vuoQEVX9xqp52','Dhanush _8',8,1,'M','2018-09-24','J6vGWibfcKYRoM3vuoQEVX9xqp52'),('JjZw94xcPZhXpTswOEMvBRifL5F3','Naren _09',9,0,'M','2018-09-26','JjZw94xcPZhXpTswOEMvBRifL5F3'),('k4SOzA9qKCchvLcPvDYq7IIAD3n1','Guna _06',6,0,'M','2018-09-26','k4SOzA9qKCchvLcPvDYq7IIAD3n1'),('PHxLUkJUqdZ1U3nn91SY3quulaJ3','yashas_9',9,0,'M','2018-09-26','PHxLUkJUqdZ1U3nn91SY3quulaJ3'),('POQpZRGYJPagtcRSe9QmJcuF3lF2','Anukalp _8',8,0,'M','2018-09-26','POQpZRGYJPagtcRSe9QmJcuF3lF2'),('PSct0i7U4AOO64UJ0kawdjdmj0x2','Admin',6,1,'M','2018-10-29','PSct0i7U4AOO64UJ0kawdjdmj0x2'),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1','Likith _7',7,0,'M','2018-09-26','wmP5aqWAA9ZeAenjTHfEbcPjVMy1'),('xRUrJ9zZ5eOseQevk4GNxTCtZj03','Anagha _8',8,0,'F','2018-09-26','xRUrJ9zZ5eOseQevk4GNxTCtZj03'),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1','Jeevan',9,1,'M','2018-09-24','YfkXOoRK6cZgKjKHxnw1cNZ8zCq1'),('YhkwMGvtBVQ5NtZLk82kgm6nFFh1','Janani _10',9,1,'F','2018-09-24','YhkwMGvtBVQ5NtZLk82kgm6nFFh1'),('YWY7SzsQoObHzqjfmd6p5FqHcGe2','Deekshit',9,1,'M','2018-09-24','YWY7SzsQoObHzqjfmd6p5FqHcGe2'),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2','Jaslene _12',9,1,'F','2018-09-24','ZtKOYnNo39QhUtrpWXi9qBT8BHv2');
/*!40000 ALTER TABLE `Child` ENABLE KEYS */;
UNLOCK TABLES;
--
-- WARNING: old server version. The following dump may be incomplete.
--
DELIMITER ;;
/*!50003 SET SESSION SQL_MODE="ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION" */;;
/*!50003 CREATE */ /*!50017 DEFINER=`root`@`localhost` */ /*!50003 TRIGGER `age_rect` BEFORE INSERT ON `Child` FOR EACH ROW BEGIN
           IF NEW.Age < 6 THEN
               SET NEW.Age = 6;
           ELSEIF NEW.Age > 9 THEN
               SET NEW.Age = 9;
           END IF;
       END */;;
DELIMITER ;

--
-- Table structure for table `DST`
--

DROP TABLE IF EXISTS `DST`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `DST` (
  `UID` varchar(30) NOT NULL,
  `Forward_Score` int(11) DEFAULT NULL,
  `Backward_Score` int(11) DEFAULT NULL,
  `Raw_score` int(11) DEFAULT NULL,
  `IDD` tinyint(1) DEFAULT NULL,
  `Std_score` float DEFAULT NULL,
  `Per_score` float DEFAULT NULL,
  KEY `fk2` (`UID`),
  CONSTRAINT `fk2` FOREIGN KEY (`UID`) REFERENCES `child` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DST`
--

LOCK TABLES `DST` WRITE;
/*!40000 ALTER TABLE `DST` DISABLE KEYS */;
INSERT INTO `DST` VALUES ('g6pTMQWqKMaom437eqIUGcSvJBA3',9,4,13,0,123,94),('gNRSHIvAGEPwNoOpbfPFcF3fwRm2',10,3,13,0,123,94),('k4SOzA9qKCchvLcPvDYq7IIAD3n1',10,2,12,0,117,87),('7fb3YgTttRUO524HSoQW4xsFnRm1',8,2,10,0,93,32),('1bognhbFAvOjBqDeDFpPzL7RUj02',12,4,16,0,129,97),('PHxLUkJUqdZ1U3nn91SY3quulaJ3',10,3,13,0,101,53),('JjZw94xcPZhXpTswOEMvBRifL5F3',11,5,16,0,116,86),('41PBOElAoCS5ZmYhbCLtkoeqeE03',11,4,15,0,111,77),('24iby93N2mhyKwJF4pdyKkHChku2',10,2,12,0,117,87),('1JejQH6R3DaM5WYY8QIZEq0LJMo1',11,3,14,0,128,97),('HKttyTxIhtSqXolAAJTMka5ZNf83',10,2,12,0,117,87),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1',4,0,4,1,57,0.2),('POQpZRGYJPagtcRSe9QmJcuF3lF2',10,4,14,0,110,75),('xRUrJ9zZ5eOseQevk4GNxTCtZj03',8,2,10,1,90,25),('B1sRQGiqGpciZiXdbCEkYjB0iXa2',12,2,14,0,106,66),('AsMtX5qSEkgduxATZvZzm2e2ca83',11,10,21,0,141,99.7),('EJGHXOkydOMMpEHhQDvdw6Vc5rH3',2,0,2,1,0,0),('YWY7SzsQoObHzqjfmd6p5FqHcGe2',4,0,4,1,56,0.2),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',5,0,5,1,61,0.5),('J6vGWibfcKYRoM3vuoQEVX9xqp52',4,0,4,1,60,0.4),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2',6,2,8,1,76,5),('YhkwMGvtBVQ5NtZLk82kgm6nFFh1',0,0,0,1,0,0),('5pUxKTHISCXBRR1A9yRqefnLnpy1',5,3,8,1,76,5),('bEOSMcdGN9OQJyv8aTrD3Gvmvhb2',0,0,0,1,0,0),('PSct0i7U4AOO64UJ0kawdjdmj0x2',3,0,3,1,0,0),('25',3,0,3,1,0,0),('26',0,0,0,1,0,0);
/*!40000 ALTER TABLE `DST` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `GDT`
--

DROP TABLE IF EXISTS `GDT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `GDT` (
  `UID` varchar(30) DEFAULT NULL,
  `GID` varchar(30) DEFAULT NULL,
  `Percentile` int(11) DEFAULT NULL,
  `IDG` tinyint(1) DEFAULT NULL,
  KEY `gfk` (`UID`),
  CONSTRAINT `gfk` FOREIGN KEY (`UID`) REFERENCES `child` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GDT`
--

LOCK TABLES `GDT` WRITE;
/*!40000 ALTER TABLE `GDT` DISABLE KEYS */;
INSERT INTO `GDT` VALUES ('g6pTMQWqKMaom437eqIUGcSvJBA3','52',99,0),('gNRSHIvAGEPwNoOpbfPFcF3fwRm2','54',99,0),('k4SOzA9qKCchvLcPvDYq7IIAD3n1','56',99,0),('7fb3YgTttRUO524HSoQW4xsFnRm1','57',80,0),('1bognhbFAvOjBqDeDFpPzL7RUj02','58',90,0),('PHxLUkJUqdZ1U3nn91SY3quulaJ3','60',80,0),('JjZw94xcPZhXpTswOEMvBRifL5F3','61',90,0),('41PBOElAoCS5ZmYhbCLtkoeqeE03','62',90,0),('24iby93N2mhyKwJF4pdyKkHChku2','70',99,0),('1JejQH6R3DaM5WYY8QIZEq0LJMo1','71',99,0),('HKttyTxIhtSqXolAAJTMka5ZNf83','72',99,0),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1','73',80,0),('POQpZRGYJPagtcRSe9QmJcuF3lF2','74',80,0),('xRUrJ9zZ5eOseQevk4GNxTCtZj03','75',60,0),('B1sRQGiqGpciZiXdbCEkYjB0iXa2','76',80,0),('AsMtX5qSEkgduxATZvZzm2e2ca83','77',90,0),('EJGHXOkydOMMpEHhQDvdw6Vc5rH3','1',10,1),('YWY7SzsQoObHzqjfmd6p5FqHcGe2','5',10,1),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1','6',10,1),('J6vGWibfcKYRoM3vuoQEVX9xqp52','50',10,1),('5pUxKTHISCXBRR1A9yRqefnLnpy1','59',10,1),('YhkwMGvtBVQ5NtZLk82kgm6nFFh1','63',10,1),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2','23',10,1),('bEOSMcdGN9OQJyv8aTrD3Gvmvhb2','bEOSMcdGN9OQJyv8aTrD3Gvmvhb2',10,1),('PSct0i7U4AOO64UJ0kawdjdmj0x2','PSct0i7U4AOO64UJ0kawdjdmj0x2',10,1),('25','25',10,1),('26','26',10,1);
/*!40000 ALTER TABLE `GDT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RPM`
--

DROP TABLE IF EXISTS `RPM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `RPM` (
  `UID` varchar(30) NOT NULL,
  `Score` int(11) NOT NULL,
  `IDR` tinyint(1) DEFAULT NULL,
  KEY `fk1` (`UID`),
  CONSTRAINT `fk1` FOREIGN KEY (`UID`) REFERENCES `child` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RPM`
--

LOCK TABLES `RPM` WRITE;
/*!40000 ALTER TABLE `RPM` DISABLE KEYS */;
INSERT INTO `RPM` VALUES ('g6pTMQWqKMaom437eqIUGcSvJBA3',19,0),('gNRSHIvAGEPwNoOpbfPFcF3fwRm2',20,0),('k4SOzA9qKCchvLcPvDYq7IIAD3n1',17,0),('7fb3YgTttRUO524HSoQW4xsFnRm1',14,0),('1bognhbFAvOjBqDeDFpPzL7RUj02',21,0),('PHxLUkJUqdZ1U3nn91SY3quulaJ3',26,0),('JjZw94xcPZhXpTswOEMvBRifL5F3',23,0),('41PBOElAoCS5ZmYhbCLtkoeqeE03',27,0),('24iby93N2mhyKwJF4pdyKkHChku2',26,0),('1JejQH6R3DaM5WYY8QIZEq0LJMo1',22,0),('HKttyTxIhtSqXolAAJTMka5ZNf83',18,0),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1',12,1),('POQpZRGYJPagtcRSe9QmJcuF3lF2',22,0),('xRUrJ9zZ5eOseQevk4GNxTCtZj03',15,1),('B1sRQGiqGpciZiXdbCEkYjB0iXa2',14,1),('AsMtX5qSEkgduxATZvZzm2e2ca83',37,0),('EJGHXOkydOMMpEHhQDvdw6Vc5rH3',4,1),('YWY7SzsQoObHzqjfmd6p5FqHcGe2',3,1),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',3,1),('J6vGWibfcKYRoM3vuoQEVX9xqp52',7,1),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2',10,1),('YhkwMGvtBVQ5NtZLk82kgm6nFFh1',9,1),('5pUxKTHISCXBRR1A9yRqefnLnpy1',9,1),('bEOSMcdGN9OQJyv8aTrD3Gvmvhb2',0,1),('PSct0i7U4AOO64UJ0kawdjdmj0x2',2,1),('25',1,1),('26',6,1);
/*!40000 ALTER TABLE `RPM` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Vineland`
--

DROP TABLE IF EXISTS `Vineland`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Vineland` (
  `UID` varchar(30) NOT NULL,
  `VID` varchar(30) NOT NULL,
  `IDV` tinyint(1) DEFAULT NULL,
  `IQV` float DEFAULT NULL,
  PRIMARY KEY (`VID`),
  KEY `vl` (`UID`),
  CONSTRAINT `vl` FOREIGN KEY (`UID`) REFERENCES `child` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Vineland`
--

LOCK TABLES `Vineland` WRITE;
/*!40000 ALTER TABLE `Vineland` DISABLE KEYS */;
INSERT INTO `Vineland` VALUES ('1bognhbFAvOjBqDeDFpPzL7RUj02','1bognhbFAvOjBqDeDFpPzL7RUj02',0,102.85),('1JejQH6R3DaM5WYY8QIZEq0LJMo1','1JejQH6R3DaM5WYY8QIZEq0LJMo1',0,110),('24iby93N2mhyKwJF4pdyKkHChku2','24iby93N2mhyKwJF4pdyKkHChku2',0,110),('25','25',0,113.889),('26','26',0,116.667),('41PBOElAoCS5ZmYhbCLtkoeqeE03','41PBOElAoCS5ZmYhbCLtkoeqeE03',0,94.16),('5pUxKTHISCXBRR1A9yRqefnLnpy1','5pUxKTHISCXBRR1A9yRqefnLnpy1',1,79.9),('7fb3YgTttRUO524HSoQW4xsFnRm1','7fb3YgTttRUO524HSoQW4xsFnRm1',0,96.42),('AsMtX5qSEkgduxATZvZzm2e2ca83','AsMtX5qSEkgduxATZvZzm2e2ca83',0,111.11),('B1sRQGiqGpciZiXdbCEkYjB0iXa2','B1sRQGiqGpciZiXdbCEkYjB0iXa2',0,98.14),('bEOSMcdGN9OQJyv8aTrD3Gvmvhb2','bEOSMcdGN9OQJyv8aTrD3Gvmvhb2',1,62.5),('EJGHXOkydOMMpEHhQDvdw6Vc5rH3','EJGHXOkydOMMpEHhQDvdw6Vc5rH3',1,91.5),('g6pTMQWqKMaom437eqIUGcSvJBA3','g6pTMQWqKMaom437eqIUGcSvJBA3',0,110),('gNRSHIvAGEPwNoOpbfPFcF3fwRm2','gNRSHIvAGEPwNoOpbfPFcF3fwRm2',0,110),('HKttyTxIhtSqXolAAJTMka5ZNf83','HKttyTxIhtSqXolAAJTMka5ZNf83',0,106.66),('J6vGWibfcKYRoM3vuoQEVX9xqp52','J6vGWibfcKYRoM3vuoQEVX9xqp52',0,94.28),('JjZw94xcPZhXpTswOEMvBRifL5F3','JjZw94xcPZhXpTswOEMvBRifL5F3',0,103.7),('k4SOzA9qKCchvLcPvDYq7IIAD3n1','k4SOzA9qKCchvLcPvDYq7IIAD3n1',0,97.56),('PHxLUkJUqdZ1U3nn91SY3quulaJ3','PHxLUkJUqdZ1U3nn91SY3quulaJ3',0,107.4),('POQpZRGYJPagtcRSe9QmJcuF3lF2','POQpZRGYJPagtcRSe9QmJcuF3lF2',0,104.37),('PSct0i7U4AOO64UJ0kawdjdmj0x2','PSct0i7U4AOO64UJ0kawdjdmj0x2',0,71.6667),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1','wmP5aqWAA9ZeAenjTHfEbcPjVMy1',0,84.28),('xRUrJ9zZ5eOseQevk4GNxTCtZj03','xRUrJ9zZ5eOseQevk4GNxTCtZj03',0,104.37),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1','YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',0,101.66),('YhkwMGvtBVQ5NtZLk82kgm6nFFh1','YhkwMGvtBVQ5NtZLk82kgm6nFFh1',1,90),('YWY7SzsQoObHzqjfmd6p5FqHcGe2','YWY7SzsQoObHzqjfmd6p5FqHcGe2',0,101.5),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2','ZtKOYnNo39QhUtrpWXi9qBT8BHv2',0,76.6);
/*!40000 ALTER TABLE `Vineland` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL0`
--

DROP TABLE IF EXISTS `VL0`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL0` (
  `VID` varchar(30) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  `q5` int(11) NOT NULL,
  `q6` int(11) NOT NULL,
  `q7` int(11) NOT NULL,
  `q8` int(11) NOT NULL,
  `q9` int(11) NOT NULL,
  `q10` int(11) NOT NULL,
  `q11` int(11) NOT NULL,
  `q12` int(11) NOT NULL,
  `q13` int(11) NOT NULL,
  `q14` int(11) NOT NULL,
  `q15` int(11) NOT NULL,
  `q16` int(11) NOT NULL,
  `q17` int(11) NOT NULL,
  KEY `vk0` (`VID`),
  CONSTRAINT `vk0` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL0`
--

LOCK TABLES `VL0` WRITE;
/*!40000 ALTER TABLE `VL0` DISABLE KEYS */;
INSERT INTO `VL0` VALUES ('g6pTMQWqKMaom437eqIUGcSvJBA3',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('gNRSHIvAGEPwNoOpbfPFcF3fwRm2',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('k4SOzA9qKCchvLcPvDYq7IIAD3n1',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('7fb3YgTttRUO524HSoQW4xsFnRm1',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('1bognhbFAvOjBqDeDFpPzL7RUj02',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('PHxLUkJUqdZ1U3nn91SY3quulaJ3',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('JjZw94xcPZhXpTswOEMvBRifL5F3',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('41PBOElAoCS5ZmYhbCLtkoeqeE03',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('24iby93N2mhyKwJF4pdyKkHChku2',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('1JejQH6R3DaM5WYY8QIZEq0LJMo1',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('HKttyTxIhtSqXolAAJTMka5ZNf83',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('POQpZRGYJPagtcRSe9QmJcuF3lF2',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('xRUrJ9zZ5eOseQevk4GNxTCtZj03',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('B1sRQGiqGpciZiXdbCEkYjB0iXa2',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('AsMtX5qSEkgduxATZvZzm2e2ca83',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('EJGHXOkydOMMpEHhQDvdw6Vc5rH3',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('YWY7SzsQoObHzqjfmd6p5FqHcGe2',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('J6vGWibfcKYRoM3vuoQEVX9xqp52',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('YhkwMGvtBVQ5NtZLk82kgm6nFFh1',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('5pUxKTHISCXBRR1A9yRqefnLnpy1',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('bEOSMcdGN9OQJyv8aTrD3Gvmvhb2',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),('PSct0i7U4AOO64UJ0kawdjdmj0x2',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),('25',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),('26',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
/*!40000 ALTER TABLE `VL0` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL1`
--

DROP TABLE IF EXISTS `VL1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL1` (
  `VID` varchar(30) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  `q5` int(11) NOT NULL,
  `q6` int(11) NOT NULL,
  `q7` int(11) NOT NULL,
  `q8` int(11) NOT NULL,
  `q9` int(11) NOT NULL,
  `q10` int(11) NOT NULL,
  `q11` int(11) NOT NULL,
  `q12` int(11) NOT NULL,
  `q13` int(11) NOT NULL,
  `q14` int(11) NOT NULL,
  `q15` int(11) NOT NULL,
  `q16` int(11) NOT NULL,
  `q17` int(11) DEFAULT NULL,
  KEY `vk1` (`VID`),
  CONSTRAINT `vk1` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL1`
--

LOCK TABLES `VL1` WRITE;
/*!40000 ALTER TABLE `VL1` DISABLE KEYS */;
INSERT INTO `VL1` VALUES ('g6pTMQWqKMaom437eqIUGcSvJBA3',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('gNRSHIvAGEPwNoOpbfPFcF3fwRm2',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('k4SOzA9qKCchvLcPvDYq7IIAD3n1',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('7fb3YgTttRUO524HSoQW4xsFnRm1',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('1bognhbFAvOjBqDeDFpPzL7RUj02',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('PHxLUkJUqdZ1U3nn91SY3quulaJ3',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('JjZw94xcPZhXpTswOEMvBRifL5F3',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('41PBOElAoCS5ZmYhbCLtkoeqeE03',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('24iby93N2mhyKwJF4pdyKkHChku2',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('1JejQH6R3DaM5WYY8QIZEq0LJMo1',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('HKttyTxIhtSqXolAAJTMka5ZNf83',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('POQpZRGYJPagtcRSe9QmJcuF3lF2',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('xRUrJ9zZ5eOseQevk4GNxTCtZj03',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('B1sRQGiqGpciZiXdbCEkYjB0iXa2',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('AsMtX5qSEkgduxATZvZzm2e2ca83',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('EJGHXOkydOMMpEHhQDvdw6Vc5rH3',0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1),('YWY7SzsQoObHzqjfmd6p5FqHcGe2',0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1),('J6vGWibfcKYRoM3vuoQEVX9xqp52',0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2',0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1),('YhkwMGvtBVQ5NtZLk82kgm6nFFh1',0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1),('5pUxKTHISCXBRR1A9yRqefnLnpy1',0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1),('bEOSMcdGN9OQJyv8aTrD3Gvmvhb2',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),('PSct0i7U4AOO64UJ0kawdjdmj0x2',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),('25',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),('26',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
/*!40000 ALTER TABLE `VL1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL10`
--

DROP TABLE IF EXISTS `VL10`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL10` (
  `VID` varchar(30) DEFAULT NULL,
  `q1` int(11) DEFAULT NULL,
  `q2` int(11) DEFAULT NULL,
  `q3` int(11) DEFAULT NULL,
  `q4` int(11) DEFAULT NULL,
  KEY `vk10` (`VID`),
  CONSTRAINT `vk10` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL10`
--

LOCK TABLES `VL10` WRITE;
/*!40000 ALTER TABLE `VL10` DISABLE KEYS */;
INSERT INTO `VL10` VALUES ('bEOSMcdGN9OQJyv8aTrD3Gvmvhb2',0,0,0,0),('PSct0i7U4AOO64UJ0kawdjdmj0x2',0,0,0,0),('25',0,0,0,0),('26',0,0,0,0);
/*!40000 ALTER TABLE `VL10` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL2`
--

DROP TABLE IF EXISTS `VL2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL2` (
  `VID` varchar(30) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  `q5` int(11) NOT NULL,
  `q6` int(11) NOT NULL,
  `q7` int(11) NOT NULL,
  `q8` int(11) NOT NULL,
  `q9` int(11) NOT NULL,
  `q10` int(11) DEFAULT NULL,
  KEY `vk2` (`VID`),
  CONSTRAINT `vk2` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL2`
--

LOCK TABLES `VL2` WRITE;
/*!40000 ALTER TABLE `VL2` DISABLE KEYS */;
INSERT INTO `VL2` VALUES ('g6pTMQWqKMaom437eqIUGcSvJBA3',1,1,1,1,1,1,1,1,1,1),('gNRSHIvAGEPwNoOpbfPFcF3fwRm2',1,1,1,1,1,1,1,1,1,1),('k4SOzA9qKCchvLcPvDYq7IIAD3n1',1,1,1,1,1,1,1,1,1,1),('7fb3YgTttRUO524HSoQW4xsFnRm1',1,1,1,1,1,1,1,1,1,1),('1bognhbFAvOjBqDeDFpPzL7RUj02',1,1,1,1,1,1,1,1,1,1),('PHxLUkJUqdZ1U3nn91SY3quulaJ3',1,1,1,1,1,1,1,1,1,1),('JjZw94xcPZhXpTswOEMvBRifL5F3',1,1,1,1,1,1,1,1,1,1),('41PBOElAoCS5ZmYhbCLtkoeqeE03',1,1,1,1,1,1,1,1,1,1),('24iby93N2mhyKwJF4pdyKkHChku2',1,1,1,1,1,1,1,1,1,1),('1JejQH6R3DaM5WYY8QIZEq0LJMo1',1,1,1,1,1,1,1,1,1,1),('HKttyTxIhtSqXolAAJTMka5ZNf83',1,1,1,1,1,1,1,1,1,1),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1',1,1,1,1,1,1,1,1,1,1),('POQpZRGYJPagtcRSe9QmJcuF3lF2',1,1,1,1,1,1,1,1,1,1),('xRUrJ9zZ5eOseQevk4GNxTCtZj03',1,1,1,1,1,1,1,1,1,1),('B1sRQGiqGpciZiXdbCEkYjB0iXa2',1,1,1,1,1,1,1,1,1,1),('AsMtX5qSEkgduxATZvZzm2e2ca83',1,1,1,1,1,1,1,1,1,1),('EJGHXOkydOMMpEHhQDvdw6Vc5rH3',1,1,1,1,1,1,1,1,1,1),('YWY7SzsQoObHzqjfmd6p5FqHcGe2',1,1,1,1,1,1,1,1,1,1),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',1,1,1,1,1,1,1,1,1,1),('J6vGWibfcKYRoM3vuoQEVX9xqp52',1,1,1,1,1,1,1,1,1,1),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2',1,1,1,1,1,1,1,1,1,1),('YhkwMGvtBVQ5NtZLk82kgm6nFFh1',1,1,1,1,1,1,1,1,1,1),('5pUxKTHISCXBRR1A9yRqefnLnpy1',1,1,1,1,1,1,1,1,1,1);
/*!40000 ALTER TABLE `VL2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL3`
--

DROP TABLE IF EXISTS `VL3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL3` (
  `VID` varchar(30) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  `q5` int(11) NOT NULL,
  `q6` int(11) DEFAULT NULL,
  KEY `vk3` (`VID`),
  CONSTRAINT `vk3` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL3`
--

LOCK TABLES `VL3` WRITE;
/*!40000 ALTER TABLE `VL3` DISABLE KEYS */;
INSERT INTO `VL3` VALUES ('g6pTMQWqKMaom437eqIUGcSvJBA3',1,1,1,1,1,1),('gNRSHIvAGEPwNoOpbfPFcF3fwRm2',1,1,1,1,1,1),('k4SOzA9qKCchvLcPvDYq7IIAD3n1',1,1,1,1,1,1),('7fb3YgTttRUO524HSoQW4xsFnRm1',1,1,1,1,1,1),('1bognhbFAvOjBqDeDFpPzL7RUj02',1,1,1,1,1,1),('PHxLUkJUqdZ1U3nn91SY3quulaJ3',1,1,1,1,1,1),('JjZw94xcPZhXpTswOEMvBRifL5F3',1,1,1,1,1,1),('41PBOElAoCS5ZmYhbCLtkoeqeE03',1,1,1,1,1,1),('24iby93N2mhyKwJF4pdyKkHChku2',1,1,1,1,1,1),('1JejQH6R3DaM5WYY8QIZEq0LJMo1',1,1,1,1,1,1),('HKttyTxIhtSqXolAAJTMka5ZNf83',1,1,1,1,1,1),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1',1,1,1,1,1,1),('POQpZRGYJPagtcRSe9QmJcuF3lF2',1,1,1,1,1,1),('xRUrJ9zZ5eOseQevk4GNxTCtZj03',1,1,1,1,1,1),('B1sRQGiqGpciZiXdbCEkYjB0iXa2',1,1,1,1,1,1),('AsMtX5qSEkgduxATZvZzm2e2ca83',1,1,1,1,1,1),('EJGHXOkydOMMpEHhQDvdw6Vc5rH3',1,1,1,1,1,1),('YWY7SzsQoObHzqjfmd6p5FqHcGe2',1,1,1,1,1,1),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',1,1,1,1,1,1),('J6vGWibfcKYRoM3vuoQEVX9xqp52',1,1,1,1,1,1),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2',1,1,1,1,1,1),('YhkwMGvtBVQ5NtZLk82kgm6nFFh1',1,1,1,1,1,1),('5pUxKTHISCXBRR1A9yRqefnLnpy1',1,1,1,1,1,1),('bEOSMcdGN9OQJyv8aTrD3Gvmvhb2',0,0,0,0,0,0),('PSct0i7U4AOO64UJ0kawdjdmj0x2',0,0,0,0,0,0),('25',0,1,1,1,1,1),('26',1,1,1,1,1,1);
/*!40000 ALTER TABLE `VL3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL4`
--

DROP TABLE IF EXISTS `VL4`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL4` (
  `VID` varchar(30) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  `q5` int(11) NOT NULL,
  `q6` int(11) NOT NULL,
  KEY `vk4` (`VID`),
  CONSTRAINT `vk4` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL4`
--

LOCK TABLES `VL4` WRITE;
/*!40000 ALTER TABLE `VL4` DISABLE KEYS */;
INSERT INTO `VL4` VALUES ('g6pTMQWqKMaom437eqIUGcSvJBA3',1,1,1,1,1,1),('gNRSHIvAGEPwNoOpbfPFcF3fwRm2',1,1,1,1,1,1),('k4SOzA9qKCchvLcPvDYq7IIAD3n1',1,1,1,1,1,1),('7fb3YgTttRUO524HSoQW4xsFnRm1',1,1,1,1,1,1),('1bognhbFAvOjBqDeDFpPzL7RUj02',1,1,1,1,1,1),('PHxLUkJUqdZ1U3nn91SY3quulaJ3',1,1,1,1,1,1),('JjZw94xcPZhXpTswOEMvBRifL5F3',1,1,1,1,1,1),('41PBOElAoCS5ZmYhbCLtkoeqeE03',1,1,1,1,1,1),('24iby93N2mhyKwJF4pdyKkHChku2',1,1,1,1,1,1),('1JejQH6R3DaM5WYY8QIZEq0LJMo1',1,1,1,1,1,1),('HKttyTxIhtSqXolAAJTMka5ZNf83',1,1,1,1,1,1),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1',1,1,1,1,1,1),('POQpZRGYJPagtcRSe9QmJcuF3lF2',1,1,1,1,1,1),('xRUrJ9zZ5eOseQevk4GNxTCtZj03',1,1,1,1,1,1),('B1sRQGiqGpciZiXdbCEkYjB0iXa2',1,1,1,1,1,1),('AsMtX5qSEkgduxATZvZzm2e2ca83',1,1,1,1,1,1),('EJGHXOkydOMMpEHhQDvdw6Vc5rH3',1,1,1,1,1,1),('YWY7SzsQoObHzqjfmd6p5FqHcGe2',1,1,1,1,1,1),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',1,1,1,1,1,1),('J6vGWibfcKYRoM3vuoQEVX9xqp52',1,1,1,1,1,1),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2',1,1,1,1,1,1),('YhkwMGvtBVQ5NtZLk82kgm6nFFh1',1,1,1,1,1,1),('5pUxKTHISCXBRR1A9yRqefnLnpy1',1,1,1,1,1,1),('bEOSMcdGN9OQJyv8aTrD3Gvmvhb2',0,0,0,0,0,0),('PSct0i7U4AOO64UJ0kawdjdmj0x2',0,0,0,0,0,0),('25',1,1,1,1,1,1),('26',1,1,1,1,1,1);
/*!40000 ALTER TABLE `VL4` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL5`
--

DROP TABLE IF EXISTS `VL5`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL5` (
  `VID` varchar(30) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  `q5` int(11) NOT NULL,
  KEY `vk5` (`VID`),
  CONSTRAINT `vk5` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL5`
--

LOCK TABLES `VL5` WRITE;
/*!40000 ALTER TABLE `VL5` DISABLE KEYS */;
INSERT INTO `VL5` VALUES ('g6pTMQWqKMaom437eqIUGcSvJBA3',0,1,1,0,1),('gNRSHIvAGEPwNoOpbfPFcF3fwRm2',0,1,1,0,1),('k4SOzA9qKCchvLcPvDYq7IIAD3n1',0,0,1,0,1),('7fb3YgTttRUO524HSoQW4xsFnRm1',0,0,1,0,1),('1bognhbFAvOjBqDeDFpPzL7RUj02',0,1,1,0,1),('PHxLUkJUqdZ1U3nn91SY3quulaJ3',1,1,1,1,1),('JjZw94xcPZhXpTswOEMvBRifL5F3',1,1,1,1,1),('41PBOElAoCS5ZmYhbCLtkoeqeE03',1,1,1,1,1),('24iby93N2mhyKwJF4pdyKkHChku2',0,1,1,0,1),('1JejQH6R3DaM5WYY8QIZEq0LJMo1',0,1,1,0,1),('HKttyTxIhtSqXolAAJTMka5ZNf83',0,0,1,0,1),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1',0,0,0,0,1),('xRUrJ9zZ5eOseQevk4GNxTCtZj03',0,1,1,0,1),('POQpZRGYJPagtcRSe9QmJcuF3lF2',1,1,1,1,1),('B1sRQGiqGpciZiXdbCEkYjB0iXa2',1,1,1,1,1),('AsMtX5qSEkgduxATZvZzm2e2ca83',1,1,1,1,1),('EJGHXOkydOMMpEHhQDvdw6Vc5rH3',0,1,1,0,0),('YWY7SzsQoObHzqjfmd6p5FqHcGe2',0,1,1,1,0),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',0,1,1,0,0),('J6vGWibfcKYRoM3vuoQEVX9xqp52',0,1,1,0,0),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2',1,1,1,1,0),('YhkwMGvtBVQ5NtZLk82kgm6nFFh1',0,1,1,0,0),('5pUxKTHISCXBRR1A9yRqefnLnpy1',0,1,1,0,0),('bEOSMcdGN9OQJyv8aTrD3Gvmvhb2',0,0,0,0,0),('PSct0i7U4AOO64UJ0kawdjdmj0x2',0,1,1,1,1),('25',1,1,1,1,1),('26',1,1,1,1,1);
/*!40000 ALTER TABLE `VL5` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL6`
--

DROP TABLE IF EXISTS `VL6`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL6` (
  `VID` varchar(30) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  KEY `vk6` (`VID`),
  CONSTRAINT `vk6` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL6`
--

LOCK TABLES `VL6` WRITE;
/*!40000 ALTER TABLE `VL6` DISABLE KEYS */;
INSERT INTO `VL6` VALUES ('g6pTMQWqKMaom437eqIUGcSvJBA3',1,1,1,1),('gNRSHIvAGEPwNoOpbfPFcF3fwRm2',1,1,1,1),('k4SOzA9qKCchvLcPvDYq7IIAD3n1',0,1,1,1),('7fb3YgTttRUO524HSoQW4xsFnRm1',1,1,0,1),('1bognhbFAvOjBqDeDFpPzL7RUj02',1,1,1,1),('PHxLUkJUqdZ1U3nn91SY3quulaJ3',1,1,1,1),('JjZw94xcPZhXpTswOEMvBRifL5F3',1,1,1,1),('41PBOElAoCS5ZmYhbCLtkoeqeE03',1,1,1,1),('24iby93N2mhyKwJF4pdyKkHChku2',1,1,1,1),('1JejQH6R3DaM5WYY8QIZEq0LJMo1',1,1,1,1),('HKttyTxIhtSqXolAAJTMka5ZNf83',1,1,1,1),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1',0,1,0,1),('POQpZRGYJPagtcRSe9QmJcuF3lF2',1,1,1,1),('xRUrJ9zZ5eOseQevk4GNxTCtZj03',1,1,1,1),('B1sRQGiqGpciZiXdbCEkYjB0iXa2',1,1,1,1),('AsMtX5qSEkgduxATZvZzm2e2ca83',1,1,1,1),('EJGHXOkydOMMpEHhQDvdw6Vc5rH3',1,1,1,1),('YWY7SzsQoObHzqjfmd6p5FqHcGe2',1,1,1,1),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',1,1,1,1),('J6vGWibfcKYRoM3vuoQEVX9xqp52',1,1,1,1),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2',1,1,1,1),('YhkwMGvtBVQ5NtZLk82kgm6nFFh1',1,1,1,1),('5pUxKTHISCXBRR1A9yRqefnLnpy1',1,1,1,1),('bEOSMcdGN9OQJyv8aTrD3Gvmvhb2',0,0,0,0),('PSct0i7U4AOO64UJ0kawdjdmj0x2',1,1,0,0),('25',1,1,1,1),('26',1,1,1,1);
/*!40000 ALTER TABLE `VL6` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL7`
--

DROP TABLE IF EXISTS `VL7`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL7` (
  `VID` varchar(30) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  `q5` int(11) NOT NULL,
  KEY `vk7` (`VID`),
  CONSTRAINT `vk7` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL7`
--

LOCK TABLES `VL7` WRITE;
/*!40000 ALTER TABLE `VL7` DISABLE KEYS */;
INSERT INTO `VL7` VALUES ('7fb3YgTttRUO524HSoQW4xsFnRm1',1,1,0,0,1),('1bognhbFAvOjBqDeDFpPzL7RUj02',1,1,0,0,1),('PHxLUkJUqdZ1U3nn91SY3quulaJ3',1,1,1,1,1),('JjZw94xcPZhXpTswOEMvBRifL5F3',1,1,1,1,1),('41PBOElAoCS5ZmYhbCLtkoeqeE03',1,1,1,1,1),('wmP5aqWAA9ZeAenjTHfEbcPjVMy1',0,0,0,0,1),('xRUrJ9zZ5eOseQevk4GNxTCtZj03',0,0,1,1,1),('POQpZRGYJPagtcRSe9QmJcuF3lF2',1,1,0,0,1),('B1sRQGiqGpciZiXdbCEkYjB0iXa2',1,1,1,1,1),('AsMtX5qSEkgduxATZvZzm2e2ca83',1,1,1,1,1),('EJGHXOkydOMMpEHhQDvdw6Vc5rH3',0,1,0,0,1),('YWY7SzsQoObHzqjfmd6p5FqHcGe2',0,1,0,0,1),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',0,1,0,0,1),('J6vGWibfcKYRoM3vuoQEVX9xqp52',0,1,0,0,1),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2',1,1,0,1,1),('YhkwMGvtBVQ5NtZLk82kgm6nFFh1',0,1,0,0,1),('5pUxKTHISCXBRR1A9yRqefnLnpy1',0,1,0,0,1),('bEOSMcdGN9OQJyv8aTrD3Gvmvhb2',0,0,0,0,0),('PSct0i7U4AOO64UJ0kawdjdmj0x2',0,0,0,0,0),('25',0,0,0,0,0),('26',0,0,0,0,0);
/*!40000 ALTER TABLE `VL7` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL8`
--

DROP TABLE IF EXISTS `VL8`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL8` (
  `VID` varchar(30) DEFAULT NULL,
  `q1` int(11) DEFAULT NULL,
  `q2` int(11) DEFAULT NULL,
  `q3` int(11) DEFAULT NULL,
  `q4` int(11) DEFAULT NULL,
  KEY `vk8` (`VID`),
  CONSTRAINT `vk8` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL8`
--

LOCK TABLES `VL8` WRITE;
/*!40000 ALTER TABLE `VL8` DISABLE KEYS */;
INSERT INTO `VL8` VALUES ('PHxLUkJUqdZ1U3nn91SY3quulaJ3',1,1,1,1),('JjZw94xcPZhXpTswOEMvBRifL5F3',1,1,1,1),('41PBOElAoCS5ZmYhbCLtkoeqeE03',0,1,1,1),('xRUrJ9zZ5eOseQevk4GNxTCtZj03',1,1,0,1),('POQpZRGYJPagtcRSe9QmJcuF3lF2',1,0,1,1),('B1sRQGiqGpciZiXdbCEkYjB0iXa2',0,1,0,1),('AsMtX5qSEkgduxATZvZzm2e2ca83',1,1,1,1),('EJGHXOkydOMMpEHhQDvdw6Vc5rH3',1,1,0,1),('YWY7SzsQoObHzqjfmd6p5FqHcGe2',1,1,0,1),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',1,1,0,1),('J6vGWibfcKYRoM3vuoQEVX9xqp52',1,1,0,1),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2',1,1,1,1),('YhkwMGvtBVQ5NtZLk82kgm6nFFh1',1,1,0,1),('5pUxKTHISCXBRR1A9yRqefnLnpy1',1,1,0,1),('bEOSMcdGN9OQJyv8aTrD3Gvmvhb2',0,0,0,0),('PSct0i7U4AOO64UJ0kawdjdmj0x2',0,0,0,0),('25',0,0,0,0),('26',0,0,0,0);
/*!40000 ALTER TABLE `VL8` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL9`
--

DROP TABLE IF EXISTS `VL9`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL9` (
  `VID` varchar(30) DEFAULT NULL,
  `q1` int(11) DEFAULT NULL,
  `q2` int(11) DEFAULT NULL,
  `q3` int(11) DEFAULT NULL,
  KEY `vk9` (`VID`),
  CONSTRAINT `vk9` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL9`
--

LOCK TABLES `VL9` WRITE;
/*!40000 ALTER TABLE `VL9` DISABLE KEYS */;
INSERT INTO `VL9` VALUES ('PHxLUkJUqdZ1U3nn91SY3quulaJ3',1,1,0),('JjZw94xcPZhXpTswOEMvBRifL5F3',1,0,0),('41PBOElAoCS5ZmYhbCLtkoeqeE03',1,1,0),('B1sRQGiqGpciZiXdbCEkYjB0iXa2',1,0,0),('AsMtX5qSEkgduxATZvZzm2e2ca83',1,1,1),('EJGHXOkydOMMpEHhQDvdw6Vc5rH3',1,1,1),('YWY7SzsQoObHzqjfmd6p5FqHcGe2',1,1,1),('YfkXOoRK6cZgKjKHxnw1cNZ8zCq1',1,1,1),('J6vGWibfcKYRoM3vuoQEVX9xqp52',1,1,1),('ZtKOYnNo39QhUtrpWXi9qBT8BHv2',1,1,1),('YhkwMGvtBVQ5NtZLk82kgm6nFFh1',1,1,1),('5pUxKTHISCXBRR1A9yRqefnLnpy1',1,1,1),('bEOSMcdGN9OQJyv8aTrD3Gvmvhb2',0,0,0),('PSct0i7U4AOO64UJ0kawdjdmj0x2',0,0,0),('25',0,0,0),('26',0,0,0);
/*!40000 ALTER TABLE `VL9` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `c`
--

/*!50001 DROP VIEW IF EXISTS `c`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `c` AS select `C`.`UID` AS `UID`,`C`.`Name` AS `Name`,`C`.`Age` AS `Age`,`C`.`ID` AS `ID`,`C`.`Gender` AS `Gender`,`R`.`Score` AS `Score`,`R`.`IDR` AS `IDR`,`D`.`Forward_Score` AS `Forward_Score`,`D`.`Backward_Score` AS `Backward_Score`,`D`.`Raw_score` AS `Raw_score`,`D`.`IDD` AS `IDD`,`D`.`Std_score` AS `Std_score`,`D`.`Per_score` AS `Per_score`,`B`.`BID` AS `BID`,`B`.`IDB` AS `IDB`,`B`.`IQ` AS `IQ`,`B`.`ID_Type` AS `ID_Type`,`gdt`.`GID` AS `GID`,`gdt`.`Percentile` AS `Percentile`,`gdt`.`IDG` AS `IDG`,`V`.`VID` AS `VID`,`V`.`IDV` AS `IDV` from (`child` `C` join (`rpm` `R` join (`dst` `D` join (`bst` `B` join (`gdt` join `vineland` `V` on((`gdt`.`UID` = `V`.`UID`))) on((`B`.`UID` = `gdt`.`UID`))) on((`D`.`UID` = `B`.`UID`))) on((`R`.`UID` = `D`.`UID`))) on((`C`.`UID` = `R`.`UID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-03 11:20:37
