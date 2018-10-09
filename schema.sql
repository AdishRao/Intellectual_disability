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
  `UID` int(11) NOT NULL,
  `BID` int(11) NOT NULL,
  `IDB` tinyint(1) DEFAULT NULL,
  `IQ` float DEFAULT NULL,
  `ID_Type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`BID`),
  KEY `fkbst` (`UID`),
  CONSTRAINT `fkbst` FOREIGN KEY (`UID`) REFERENCES `child` (`uid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `b10` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `fk3` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `fk4` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `fk5` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `fk6` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `fk7` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `b8` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `b9` FOREIGN KEY (`BID`) REFERENCES `bst` (`bid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
-- Table structure for table `child`
--

DROP TABLE IF EXISTS `child`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `child` (
  `UID` int(11) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Age` float NOT NULL,
  `ID` tinyint(1) DEFAULT NULL,
  `Gender` char(1) DEFAULT NULL,
  `DateOfTest` date DEFAULT NULL,
  `RID` int(11) DEFAULT NULL,
  PRIMARY KEY (`UID`),
  KEY `refer` (`RID`),
  CONSTRAINT `refer` FOREIGN KEY (`RID`) REFERENCES `child` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  `IDD` tinyint(1) DEFAULT NULL,
  `Std_score` float DEFAULT NULL,
  `Per_score` float DEFAULT NULL,
  KEY `fk2` (`UID`),
  CONSTRAINT `fk2` FOREIGN KEY (`UID`) REFERENCES `child` (`uid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  `IDG` tinyint(1) DEFAULT NULL,
  KEY `gfk` (`UID`),
  CONSTRAINT `gfk` FOREIGN KEY (`UID`) REFERENCES `child` (`uid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `RPM`
--

DROP TABLE IF EXISTS `RPM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `RPM` (
  `UID` int(11) NOT NULL,
  `Score` int(11) NOT NULL,
  `IDR` tinyint(1) DEFAULT NULL,
  KEY `fk1` (`UID`),
  CONSTRAINT `fk1` FOREIGN KEY (`UID`) REFERENCES `child` (`uid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Vineland`
--

DROP TABLE IF EXISTS `Vineland`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Vineland` (
  `UID` int(11) NOT NULL,
  `VID` int(11) NOT NULL,
  `IDV` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`VID`),
  KEY `vl` (`UID`),
  CONSTRAINT `vl` FOREIGN KEY (`UID`) REFERENCES `child` (`uid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `vk0` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `vk1` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `vk10` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `vk2` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `vk3` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `vk4` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `vk5` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `vk6` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `vk7` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `vk8` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `vk9` FOREIGN KEY (`VID`) REFERENCES `vineland` (`vid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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

-- Dump completed on 2018-10-09 16:38:52
