CREATE DATABASE  IF NOT EXISTS `db_website` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `db_website`;
-- MySQL dump 10.13  Distrib 5.7.34, for Linux (x86_64)
--
-- Host: 172.27.0.3    Database: db_website
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `administrators`
--

DROP TABLE IF EXISTS `administrators`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `administrators` (
  `worker_id` varchar(15) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `reg_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `vkey` varchar(255) NOT NULL,
  `verified` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`worker_id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `worker_id` (`worker_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrators`
--

LOCK TABLES `administrators` WRITE;
/*!40000 ALTER TABLE `administrators` DISABLE KEYS */;
INSERT  IGNORE INTO `administrators` (`worker_id`, `name`, `email`, `password`, `reg_time`, `vkey`, `verified`) VALUES ('123','123','123@123.123com','a79a4cb3563db62c0daabb72e99e1f21f2ec5be6d9ba571d4a3b812f4e1ce44b','2020-06-30 12:59:56','0.612578491748926',0);
/*!40000 ALTER TABLE `administrators` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `courses_code`
--

DROP TABLE IF EXISTS `courses_code`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `courses_code` (
  `serial` int NOT NULL AUTO_INCREMENT,
  `course_code` varchar(45) NOT NULL,
  `course_name` varchar(100) NOT NULL,
  `credit` int NOT NULL,
  `hours` int NOT NULL,
  `state` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`serial`),
  UNIQUE KEY `courses_id_UNIQUE` (`serial`),
  UNIQUE KEY `course_code_UNIQUE` (`course_code`),
  UNIQUE KEY `course_name_UNIQUE` (`course_name`)
) ENGINE=InnoDB AUTO_INCREMENT=904 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses_code`
--

LOCK TABLES `courses_code` WRITE;
/*!40000 ALTER TABLE `courses_code` DISABLE KEYS */;
INSERT  IGNORE INTO `courses_code` (`serial`, `course_code`, `course_name`, `credit`, `hours`, `state`) VALUES (1,'G801','Basic Mandarin ',3,4,0),(2,'G804','JSP',3,1,0),(3,'G802','Big Data Analysis',3,3,0),(4,'G803','Java',3,1,0),(5,'G805','Golang',3,3,0),(6,'G806','JavaScript',3,3,0);
/*!40000 ALTER TABLE `courses_code` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `students` (
  `student_id` varchar(8) NOT NULL,
  `name` varchar(50) NOT NULL,
  `grade` text NOT NULL,
  `gender` varchar(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(256) NOT NULL,
  `reg_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `vkey` varchar(256) NOT NULL,
  `file` varchar(256) NOT NULL,
  `verified` tinyint(1) NOT NULL DEFAULT '0',
  `state` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`student_id`),
  UNIQUE KEY `student_id` (`student_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT  IGNORE INTO `students` (`student_id`, `name`, `grade`, `gender`, `email`, `password`, `reg_time`, `vkey`, `file`, `verified`, `state`) VALUES ('1233','cantik','Master of Computer Science and Information Engineering','Female','herlinafitri18@gmail.com','a79a4cb3563db62c0daabb72e99e1f21f2ec5be6d9ba571d4a3b812f4e1ce44b','2021-06-21 06:52:46','b16d39ac6388bbbd79efcff76fb4e2264da1c5d67828a879f8ead6a286daaa22','Not Uploaded Yet',1,0),('4A807021','Fathria Nurul Fadillah','Master of Electrical Engineering','Female','fathrianf@gmail.com','$2y$12$0fSWiSZrfZx5IExZ3tI0nemfoa6ZMQvxCSoq4d63U2O/eVkXuPs.e','2020-08-31 09:00:26','8f21f62e10aab1374338ad1852bbd2506bf72f465671a574562e8daed6b0f772d93d8356c5422948a634c7585b3cb173b336','',0,0),('4A817010','student','Master of Computer Science and Information Engineering','Unknown','herlinafitrih1@gmail.com','f7327560e89bf63ad5d018609047945df75b810531e11ba2444d2311346009f6','2021-06-17 11:14:37','049bb6060b0e18d74a6b6e1484bfd09ca775da3a0005cfd0d78fb7ca5d54b416','Not Uploaded Yet',0,0),('4A817012','student1','Master of Computer Science and Information Engineering','Unknown','herlinafitri12@gmail.com','ee210560cbe2932d2bc6a24b8d51b9be5776c96d32df28ab3dda13fd4c3cb3b1','2021-06-17 11:13:18','893879002cffb2590952ef6ed3dc812c0ac51102c31e9ce91512c7be9bd8e067','Not Uploaded Yet',0,0),('4A817021','Herlina Fitri Handayani','Master of Computer Science and Information Engineering','Female','Herlinafitri13@gmail.com','b93a8a0902ca42e6728d227e005edcbd032543e82c962001168ed6fe225e485c','2021-06-17 10:57:01','57074cafb7b20c2bb85dba71ced3a9aaeb3fe785627e82b3028915cd5e628c3f','',1,0),('4A817022','He Yi Na','Master of Computer Science and Information Engineering','Female','herlinafitri15@gmail.com','$2y$12$mj5rjIx7cxDhjJ.Ob85zY.BQlLWStHoziEsToa/PKwKOdFofE8Exu','2020-09-05 02:28:09','68f68a54864440c0c03d9046e04757a66f43df68fa886edade15e064dcb8f9f6461e8faa5a477bf0dbe20499874b9df2948a','',1,0);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students_courses`
--

DROP TABLE IF EXISTS `students_courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `students_courses` (
  `serial` int NOT NULL AUTO_INCREMENT,
  `student_id` varchar(8) NOT NULL,
  `course_id` int NOT NULL,
  PRIMARY KEY (`serial`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students_courses`
--

LOCK TABLES `students_courses` WRITE;
/*!40000 ALTER TABLE `students_courses` DISABLE KEYS */;
INSERT  IGNORE INTO `students_courses` (`serial`, `student_id`, `course_id`) VALUES (1,'4A807021',1),(2,'4A807021',4),(4,'4A817030',2),(5,'4A817030',5),(6,'4A817030',6),(12,'4A817021',1),(13,'4A817021',6),(14,'1233',2),(15,'1233',4),(16,'1233',3),(17,'4A817010',2),(18,'4A817022',1);
/*!40000 ALTER TABLE `students_courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students_monitoring`
--

DROP TABLE IF EXISTS `students_monitoring`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `students_monitoring` (
  `id` int NOT NULL AUTO_INCREMENT,
  `student_id` varchar(8) NOT NULL,
  `course_id` varchar(10) NOT NULL,
  `time_arrive` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students_monitoring`
--

LOCK TABLES `students_monitoring` WRITE;
/*!40000 ALTER TABLE `students_monitoring` DISABLE KEYS */;
INSERT  IGNORE INTO `students_monitoring` (`id`, `student_id`, `course_id`, `time_arrive`) VALUES (1,'4A817030','1','2020-09-13 09:43:50'),(2,'4A817030','2','2020-09-13 09:43:50'),(3,'4A817030','3','2020-09-13 09:43:50'),(4,'4A817021','4','2020-09-13 09:43:50'),(5,'4A817021','5','2020-09-13 09:43:50'),(6,'4A807021','1','2020-09-13 09:43:50'),(7,'4A807021','6','2020-09-13 09:43:50'),(8,'1233','4','2021-06-21 00:00:00'),(9,'1233','3','2021-06-21 00:00:00'),(10,'1233','2','2021-06-21 00:00:00'),(11,'4A807021','1','2021-06-22 04:12:49'),(12,'4A817021','1','2021-06-22 04:13:10'),(13,'1233','2','2021-06-22 04:13:27'),(14,'4A807021','1','2021-06-22 04:13:28'),(15,'4A807021','1','2021-06-22 04:13:28'),(16,'1233','2','2021-06-22 04:14:07'),(17,'4A817010','2','2021-06-22 04:14:08'),(18,'4A807021','1','2021-06-22 07:29:38'),(19,'4A817022','1','2021-06-22 07:36:37'),(20,'4A817021','1','2021-06-22 08:02:01'),(21,'4A817021','1','2021-06-22 08:03:00'),(22,'4A817022','1','2021-06-22 08:03:15'),(32,'1233','2','2021-06-23 02:26:05'),(33,'1233','2','2021-06-23 02:31:30');
/*!40000 ALTER TABLE `students_monitoring` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teachers` (
  `teacher_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `reg_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `vkey` varchar(256) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `state` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`teacher_id`),
  UNIQUE KEY `teacher_id` (`teacher_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=457 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;
/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
INSERT  IGNORE INTO `teachers` (`teacher_id`, `name`, `email`, `password`, `reg_time`, `vkey`, `verified`, `state`) VALUES (123,'Jason','123@1211113.com','a79a4cb3563db62c0daabb72e99e1f21f2ec5be6d9ba571d4a3b812f4e1ce44b','2020-08-31 09:05:26','46f80c7a89b92a04ad9eed39f4cb7f48b93598f2765a48d4ca81244a4f042dbd',0,0),(456,'Herlina Fitri Handayani','herlinafitri16@gmail.com','3f0042158a11f49f29656359c80b5cf2a5470e1e1d4e9d03ae65316b5aca0927','2021-06-21 06:48:14','0c11d2b27ded297c7cb5e609fef99e318076e6377392ec54c4c0046781050f2e',1,0);
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachers_courses`
--

DROP TABLE IF EXISTS `teachers_courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teachers_courses` (
  `serial` int NOT NULL AUTO_INCREMENT,
  `teacher_id` varchar(20) NOT NULL,
  `course_code_id` varchar(15) NOT NULL,
  `day` varchar(10) NOT NULL,
  `time_start` varchar(45) DEFAULT NULL,
  `time_end` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`serial`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers_courses`
--

LOCK TABLES `teachers_courses` WRITE;
/*!40000 ALTER TABLE `teachers_courses` DISABLE KEYS */;
INSERT  IGNORE INTO `teachers_courses` (`serial`, `teacher_id`, `course_code_id`, `day`, `time_start`, `time_end`) VALUES (1,'456','3','Monday','10:05:00','12:05:00'),(2,'456','1','Tuesday','10:05:00','11:05:00'),(3,'456','5','Wednesday','09:05:00','10:05:00'),(4,'123','2','Thursday','10:05:00','11:05:00'),(5,'123','3','Friday','08:05:00','10:05:00'),(6,'123','6','Saturday','09:05:00','11:05:00');
/*!40000 ALTER TABLE `teachers_courses` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-01  9:56:19
