CREATE DATABASE  IF NOT EXISTS `esquema_cinturon` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `esquema_cinturon`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: esquema_cinturon
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `posteos`
--

DROP TABLE IF EXISTS `posteos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `posteos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `posteo` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_posteos_usuarios_idx` (`usuario_id`),
  CONSTRAINT `fk_posteos_usuarios` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posteos`
--

LOCK TABLES `posteos` WRITE;
/*!40000 ALTER TABLE `posteos` DISABLE KEYS */;
INSERT INTO `posteos` VALUES (1,'\nEs increíble un tipo haciendo un tutorial Gratis de 3:15 horas explicando tan bien todo que perfectamente podría ser un docente de universidad. Muchas gracias enserio',NULL,'2023-01-29 08:34:40',2),(2,'Muy buen video, increible el tiempo que uno pierde en redes socales :( teniendo gente tan grande compartiendo conocimiento.',NULL,'2023-01-29 08:35:12',2),(14,'Es un mensaje',NULL,NULL,3),(15,'Esto es otro mensaje',NULL,NULL,3),(16,'Seguir probando',NULL,NULL,1),(20,'Probando comentarios',NULL,NULL,1),(21,'Y yo pensaba que no podría aprender Python en un solo día, la verdad te la rifaste con las explicaciones de cada cosa sin dar tanto enredo, todo sencillo, muchas gracia',NULL,NULL,1),(22,'Probando publicación del prueba 4',NULL,NULL,6);
/*!40000 ALTER TABLE `posteos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-29  9:30:57
