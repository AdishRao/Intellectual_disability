-- MySQL dump 10.13  Distrib 8.0.12, for macos10.13 (x86_64)
--
-- Host: localhost    Database: Intellectual_disability
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
  `UID` int(11) NOT NULL,
  `BID` int(11) NOT NULL,
  `ID` tinyint(1) DEFAULT NULL,
  `IQ` float DEFAULT NULL,
  `ID_Type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`BID`),
  KEY `fkbst` (`UID`),
  CONSTRAINT `fkbst` FOREIGN KEY (`UID`) REFERENCES `child` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BST`
--

LOCK TABLES `BST` WRITE;
/*!40000 ALTER TABLE `BST` DISABLE KEYS */;
INSERT INTO `BST` VALUES (58,58,1,22.2222,'Severe ID'),(60,60,1,67.1333,'Mild ID'),(432,432,1,22.2222,'Severe ID');
/*!40000 ALTER TABLE `BST` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BST10`
--

DROP TABLE IF EXISTS `BST10`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `BST10` (
  `BID` int(11) DEFAULT NULL,
  `q1` int(11) DEFAULT NULL,
  `q2` int(11) DEFAULT NULL,
  `q3` int(11) DEFAULT NULL,
  `q4` int(11) DEFAULT NULL,
  `q5` int(11) DEFAULT NULL,
  KEY `b10` (`BID`),
  CONSTRAINT `b10` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BST10`
--

LOCK TABLES `BST10` WRITE;
/*!40000 ALTER TABLE `BST10` DISABLE KEYS */;
/*!40000 ALTER TABLE `BST10` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BST3`
--

DROP TABLE IF EXISTS `BST3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `BST3` (
  `BID` int(11) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  `q5` int(11) NOT NULL,
  KEY `fk3` (`BID`),
  CONSTRAINT `fk3` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BST3`
--

LOCK TABLES `BST3` WRITE;
/*!40000 ALTER TABLE `BST3` DISABLE KEYS */;
INSERT INTO `BST3` VALUES (60,1,1,1,1,0);
/*!40000 ALTER TABLE `BST3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BST4`
--

DROP TABLE IF EXISTS `BST4`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `BST4` (
  `BID` int(11) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  KEY `fk4` (`BID`),
  CONSTRAINT `fk4` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BST4`
--

LOCK TABLES `BST4` WRITE;
/*!40000 ALTER TABLE `BST4` DISABLE KEYS */;
INSERT INTO `BST4` VALUES (60,0,1,1,1);
/*!40000 ALTER TABLE `BST4` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BST5`
--

DROP TABLE IF EXISTS `BST5`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `BST5` (
  `BID` int(11) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  `q5` int(11) NOT NULL,
  KEY `fk5` (`BID`),
  CONSTRAINT `fk5` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BST5`
--

LOCK TABLES `BST5` WRITE;
/*!40000 ALTER TABLE `BST5` DISABLE KEYS */;
INSERT INTO `BST5` VALUES (60,1,1,0,1,1);
/*!40000 ALTER TABLE `BST5` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BST6`
--

DROP TABLE IF EXISTS `BST6`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `BST6` (
  `BID` int(11) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  `q5` int(11) NOT NULL,
  KEY `fk6` (`BID`),
  CONSTRAINT `fk6` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BST6`
--

LOCK TABLES `BST6` WRITE;
/*!40000 ALTER TABLE `BST6` DISABLE KEYS */;
INSERT INTO `BST6` VALUES (60,1,1,0,0,0);
/*!40000 ALTER TABLE `BST6` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BST7`
--

DROP TABLE IF EXISTS `BST7`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `BST7` (
  `BID` int(11) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  `q5` int(11) NOT NULL,
  KEY `fk7` (`BID`),
  CONSTRAINT `fk7` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BST7`
--

LOCK TABLES `BST7` WRITE;
/*!40000 ALTER TABLE `BST7` DISABLE KEYS */;
INSERT INTO `BST7` VALUES (60,1,1,1,0,1);
/*!40000 ALTER TABLE `BST7` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BST8`
--

DROP TABLE IF EXISTS `BST8`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `BST8` (
  `BID` int(11) DEFAULT NULL,
  `q1` int(11) DEFAULT NULL,
  `q2` int(11) DEFAULT NULL,
  `q3` int(11) DEFAULT NULL,
  `q4` int(11) DEFAULT NULL,
  `q5` int(11) DEFAULT NULL,
  KEY `b8` (`BID`),
  CONSTRAINT `b8` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BST8`
--

LOCK TABLES `BST8` WRITE;
/*!40000 ALTER TABLE `BST8` DISABLE KEYS */;
INSERT INTO `BST8` VALUES (60,1,0,0,0,0);
/*!40000 ALTER TABLE `BST8` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BST9`
--

DROP TABLE IF EXISTS `BST9`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `BST9` (
  `BID` int(11) DEFAULT NULL,
  `q1` int(11) DEFAULT NULL,
  `q2` int(11) DEFAULT NULL,
  `q3` int(11) DEFAULT NULL,
  `q4` int(11) DEFAULT NULL,
  `q5` int(11) DEFAULT NULL,
  KEY `b9` (`BID`),
  CONSTRAINT `b9` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BST9`
--

LOCK TABLES `BST9` WRITE;
/*!40000 ALTER TABLE `BST9` DISABLE KEYS */;
INSERT INTO `BST9` VALUES (60,0,0,1,1,1);
/*!40000 ALTER TABLE `BST9` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Child`
--

DROP TABLE IF EXISTS `Child`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Child` (
  `UID` int(11) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Age` float NOT NULL,
  `ID` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`UID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Child`
--

LOCK TABLES `Child` WRITE;
/*!40000 ALTER TABLE `Child` DISABLE KEYS */;
INSERT INTO `Child` VALUES (11,'manya',10,1),(12,'Anwesha',12,1),(21,'Anwesha _10',9,1),(23,'Jaslene _12',9,1),(25,'stutthi _16',9,1),(27,'Sripadma _16',9,1),(28,'harshita _18',9,1),(30,'Pawan _7',7,1),(58,'Janani _10',9,1),(60,'Dheeraj _11',9,1),(333,'aiy',7,1),(432,'a',9,1),(1002,'temp ',7,1),(1100,'bla ',8,1);
/*!40000 ALTER TABLE `Child` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DST`
--

DROP TABLE IF EXISTS `DST`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `DST` (
  `UID` int(11) NOT NULL,
  `Forward_Score` int(11) DEFAULT NULL,
  `Backward_Score` int(11) DEFAULT NULL,
  `Raw_score` int(11) DEFAULT NULL,
  `ID` tinyint(1) DEFAULT NULL,
  `Std_score` float DEFAULT NULL,
  `Per_score` float DEFAULT NULL,
  KEY `fk2` (`UID`),
  CONSTRAINT `fk2` FOREIGN KEY (`UID`) REFERENCES `child` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DST`
--

LOCK TABLES `DST` WRITE;
/*!40000 ALTER TABLE `DST` DISABLE KEYS */;
INSERT INTO `DST` VALUES (1002,6,5,11,0,99,47),(333,4,4,8,1,81,10),(23,6,2,8,1,76,5),(25,4,0,4,1,56,0.2),(27,8,4,12,0,96,39),(28,5,1,6,1,66,1),(1100,0,0,0,1,0,0),(432,0,0,0,1,0,0),(58,0,0,0,1,0,0),(60,5,3,8,1,76,5);
/*!40000 ALTER TABLE `DST` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `GDT`
--

DROP TABLE IF EXISTS `GDT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `GDT` (
  `UID` int(11) DEFAULT NULL,
  `GID` int(11) DEFAULT NULL,
  `Percentile` int(11) DEFAULT NULL,
  `ID` tinyint(1) DEFAULT NULL,
  KEY `gfk` (`UID`),
  CONSTRAINT `gfk` FOREIGN KEY (`UID`) REFERENCES `child` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GDT`
--

LOCK TABLES `GDT` WRITE;
/*!40000 ALTER TABLE `GDT` DISABLE KEYS */;
/*!40000 ALTER TABLE `GDT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RPM`
--

DROP TABLE IF EXISTS `RPM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `RPM` (
  `UID` int(11) NOT NULL,
  `Score` int(11) NOT NULL,
  `ID` tinyint(1) DEFAULT NULL,
  KEY `fk1` (`UID`),
  CONSTRAINT `fk1` FOREIGN KEY (`UID`) REFERENCES `child` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RPM`
--

LOCK TABLES `RPM` WRITE;
/*!40000 ALTER TABLE `RPM` DISABLE KEYS */;
INSERT INTO `RPM` VALUES (1002,0,1),(333,1,1),(23,10,1),(25,16,1),(27,11,1),(28,13,1),(28,0,1),(1100,0,1),(432,0,1),(58,9,1),(60,9,1);
/*!40000 ALTER TABLE `RPM` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Vineland`
--

DROP TABLE IF EXISTS `Vineland`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Vineland` (
  `UID` int(11) NOT NULL,
  `VID` int(11) NOT NULL,
  `ID` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`VID`),
  KEY `vl` (`UID`),
  CONSTRAINT `vl` FOREIGN KEY (`UID`) REFERENCES `child` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Vineland`
--

LOCK TABLES `Vineland` WRITE;
/*!40000 ALTER TABLE `Vineland` DISABLE KEYS */;
INSERT INTO `Vineland` VALUES (1002,1002,1);
/*!40000 ALTER TABLE `Vineland` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL0`
--

DROP TABLE IF EXISTS `VL0`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL0` (
  `VID` int(11) NOT NULL,
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
  CONSTRAINT `vk0` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL0`
--

LOCK TABLES `VL0` WRITE;
/*!40000 ALTER TABLE `VL0` DISABLE KEYS */;
INSERT INTO `VL0` VALUES (1002,1,0,1,0,2,0,1,2,0,1,2,0,2,0,2,1,2);
/*!40000 ALTER TABLE `VL0` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL1`
--

DROP TABLE IF EXISTS `VL1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL1` (
  `VID` int(11) NOT NULL,
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
  CONSTRAINT `vk1` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL1`
--

LOCK TABLES `VL1` WRITE;
/*!40000 ALTER TABLE `VL1` DISABLE KEYS */;
INSERT INTO `VL1` VALUES (1002,0,1,2,0,2,0,1,2,1,2,1,0,1,0,2,0,1);
/*!40000 ALTER TABLE `VL1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL10`
--

DROP TABLE IF EXISTS `VL10`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL10` (
  `VID` int(11) DEFAULT NULL,
  `q1` int(11) DEFAULT NULL,
  `q2` int(11) DEFAULT NULL,
  `q3` int(11) DEFAULT NULL,
  `q4` int(11) DEFAULT NULL,
  KEY `vk10` (`VID`),
  CONSTRAINT `vk10` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL10`
--

LOCK TABLES `VL10` WRITE;
/*!40000 ALTER TABLE `VL10` DISABLE KEYS */;
/*!40000 ALTER TABLE `VL10` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL2`
--

DROP TABLE IF EXISTS `VL2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL2` (
  `VID` int(11) NOT NULL,
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
  CONSTRAINT `vk2` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL2`
--

LOCK TABLES `VL2` WRITE;
/*!40000 ALTER TABLE `VL2` DISABLE KEYS */;
/*!40000 ALTER TABLE `VL2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL3`
--

DROP TABLE IF EXISTS `VL3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL3` (
  `VID` int(11) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  `q5` int(11) NOT NULL,
  `q6` int(11) DEFAULT NULL,
  KEY `vk3` (`VID`),
  CONSTRAINT `vk3` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL3`
--

LOCK TABLES `VL3` WRITE;
/*!40000 ALTER TABLE `VL3` DISABLE KEYS */;
/*!40000 ALTER TABLE `VL3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL4`
--

DROP TABLE IF EXISTS `VL4`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL4` (
  `VID` int(11) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  `q5` int(11) NOT NULL,
  `q6` int(11) NOT NULL,
  KEY `vk4` (`VID`),
  CONSTRAINT `vk4` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL4`
--

LOCK TABLES `VL4` WRITE;
/*!40000 ALTER TABLE `VL4` DISABLE KEYS */;
/*!40000 ALTER TABLE `VL4` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL5`
--

DROP TABLE IF EXISTS `VL5`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL5` (
  `VID` int(11) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  `q5` int(11) NOT NULL,
  KEY `vk5` (`VID`),
  CONSTRAINT `vk5` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL5`
--

LOCK TABLES `VL5` WRITE;
/*!40000 ALTER TABLE `VL5` DISABLE KEYS */;
/*!40000 ALTER TABLE `VL5` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL6`
--

DROP TABLE IF EXISTS `VL6`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL6` (
  `VID` int(11) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  KEY `vk6` (`VID`),
  CONSTRAINT `vk6` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL6`
--

LOCK TABLES `VL6` WRITE;
/*!40000 ALTER TABLE `VL6` DISABLE KEYS */;
/*!40000 ALTER TABLE `VL6` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL7`
--

DROP TABLE IF EXISTS `VL7`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL7` (
  `VID` int(11) NOT NULL,
  `q1` int(11) NOT NULL,
  `q2` int(11) NOT NULL,
  `q3` int(11) NOT NULL,
  `q4` int(11) NOT NULL,
  `q5` int(11) NOT NULL,
  KEY `vk7` (`VID`),
  CONSTRAINT `vk7` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL7`
--

LOCK TABLES `VL7` WRITE;
/*!40000 ALTER TABLE `VL7` DISABLE KEYS */;
/*!40000 ALTER TABLE `VL7` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL8`
--

DROP TABLE IF EXISTS `VL8`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL8` (
  `VID` int(11) DEFAULT NULL,
  `q1` int(11) DEFAULT NULL,
  `q2` int(11) DEFAULT NULL,
  `q3` int(11) DEFAULT NULL,
  `q4` int(11) DEFAULT NULL,
  KEY `vk8` (`VID`),
  CONSTRAINT `vk8` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL8`
--

LOCK TABLES `VL8` WRITE;
/*!40000 ALTER TABLE `VL8` DISABLE KEYS */;
/*!40000 ALTER TABLE `VL8` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VL9`
--

DROP TABLE IF EXISTS `VL9`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `VL9` (
  `VID` int(11) DEFAULT NULL,
  `q1` int(11) DEFAULT NULL,
  `q2` int(11) DEFAULT NULL,
  `q3` int(11) DEFAULT NULL,
  KEY `vk9` (`VID`),
  CONSTRAINT `vk9` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VL9`
--

LOCK TABLES `VL9` WRITE;
/*!40000 ALTER TABLE `VL9` DISABLE KEYS */;
/*!40000 ALTER TABLE `VL9` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-24 20:28:18
