/*
SQLyog Professional v12.4.3 (64 bit)
MySQL - 8.0.28 : Database - quick_api
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`quick_api` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `quick_api`;

/*Table structure for table `api_bills` */

DROP TABLE IF EXISTS `api_bills`;

CREATE TABLE `api_bills` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `company_name` varchar(50) NOT NULL,
  `nit` varchar(50) NOT NULL,
  `code` varchar(50) NOT NULL,
  `client_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_bills_client_id_id_c28594d9_fk_api_clients_id` (`client_id_id`),
  CONSTRAINT `api_bills_client_id_id_c28594d9_fk_api_clients_id` FOREIGN KEY (`client_id_id`) REFERENCES `api_clients` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `api_bills` */

insert  into `api_bills`(`id`,`company_name`,`nit`,`code`,`client_id_id`) values 
(1,'Vehiculos y Antiguedades SA','135-4578965','45789',1);

/*Table structure for table `api_bills_products` */

DROP TABLE IF EXISTS `api_bills_products`;

CREATE TABLE `api_bills_products` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `bill_id_id` bigint NOT NULL,
  `product_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_bills_products_bill_id_id_2795ee6b_fk_api_bills_id` (`bill_id_id`),
  KEY `api_bills_products_product_id_id_444b0b21_fk_api_products_id` (`product_id_id`),
  CONSTRAINT `api_bills_products_bill_id_id_2795ee6b_fk_api_bills_id` FOREIGN KEY (`bill_id_id`) REFERENCES `api_bills` (`id`),
  CONSTRAINT `api_bills_products_product_id_id_444b0b21_fk_api_products_id` FOREIGN KEY (`product_id_id`) REFERENCES `api_products` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `api_bills_products` */

insert  into `api_bills_products`(`id`,`bill_id_id`,`product_id_id`) values 
(1,1,1);

/*Table structure for table `api_clients` */

DROP TABLE IF EXISTS `api_clients`;

CREATE TABLE `api_clients` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `document` varchar(20) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `api_clients` */

insert  into `api_clients`(`id`,`document`,`first_name`,`last_name`,`email`) values 
(1,'1143789456','Carlos','Perez','cperez@gmail.com'),
(2,'1143134567','Laura','Benitez','lbenitez@gmail.com'),
(4,'1143456123','Miguel Andres','Araujo','maraujo@gmail.com\r'),
(6,'4889561','Emma Maria','Suarez','esuarez@gmail.com\r'),
(7,'45671234','Fabio Felipe','Vallejo','ffelipe@gmail.com');

/*Table structure for table `api_products` */

DROP TABLE IF EXISTS `api_products`;

CREATE TABLE `api_products` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` varchar(200) NOT NULL,
  `Attribute_4` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `api_products` */

insert  into `api_products`(`id`,`name`,`description`,`Attribute_4`) values 
(1,'1969 Harley Davidson Ultimate Chopper','This replica features working kickstand','Motorcycles'),
(2,'1952 Alpine Renault 1300','Turnable front wheels','Classic Cars');

/*Table structure for table `api_tokens` */

DROP TABLE IF EXISTS `api_tokens`;

CREATE TABLE `api_tokens` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `token` varchar(300) NOT NULL,
  `active` int NOT NULL,
  `expiry_date` datetime(6) NOT NULL,
  `user_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `api_tokens_user_id_id_1810032a_fk_api_users_id` (`user_id_id`),
  CONSTRAINT `api_tokens_user_id_id_1810032a_fk_api_users_id` FOREIGN KEY (`user_id_id`) REFERENCES `api_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `api_tokens` */

insert  into `api_tokens`(`id`,`token`,`active`,`expiry_date`,`user_id_id`) values 
(1,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTYxMDU4OTIuNTI0OTE4LCJ1c2VyX2lkIjoiYnJhbmRvbiIsInVzZXJfcGFzcyI6IjEyMzQ1In0.4TOBuUAzAwZxNOpZcR0D910jVYcKAaAhd9w3lJ1kCXQ',0,'2022-06-24 16:24:52.524918',1),
(2,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTYxMTAwMDkuNzE2MzAxLCJ1c2VyX2lkIjoiYnJhbmRvbiIsInVzZXJfcGFzcyI6IjEyMzQ1In0.Q5BpAd51Elgcvvl6T00yX7ohQJjJErd6HCR_xQ5j0p0',0,'2022-06-24 17:33:29.716301',1),
(3,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTYxOTk1NTUuODExMDU3LCJ1c2VyX2lkIjoiYnJhbmRvbiIsInVzZXJfcGFzcyI6IjEyMzQ1In0.sAPlqNcPSzQzSbK4iPJ9KbDSaB3u-1juZB9FB4q3bs8',0,'2022-06-25 18:25:55.811057',1),
(4,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTYzMjg0NzYuNTUwMzk5LCJ1c2VyX2lkIjoiYnJhbmRvbiIsInVzZXJfcGFzcyI6IjEyMzQ1In0.UJ_LpejdPrysqHxRrjaQB3xg3VZ1ormM8epc8tMpWCc',1,'2022-06-27 06:14:36.550399',1),
(5,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTYzMzc2MjUuOTA0MjI3LCJ1c2VyX2lkIjoibWFyaWFiQGdtYWlsLmNvbSIsInVzZXJfcGFzcyI6IiNNYmFycmVyYXMifQ.56F4m6OXtuHXAuCzCe9KE1v91TgZDAaTMq9QYwDUOkw',0,'2022-06-27 08:47:05.904227',2),
(6,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTYzNDQyNDUuODM0MjUsInVzZXJfaWQiOiJtYXJpYWJAZ21haWwuY29tIiwidXNlcl9wYXNzIjoiI01iYXJyZXJhcyJ9.7PYCOWnVlGlhgj8T9zibcoB11qghzVxg9URBHRwaBqc',1,'2022-06-27 10:37:25.834250',2);

/*Table structure for table `api_users` */

DROP TABLE IF EXISTS `api_users`;

CREATE TABLE `api_users` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `active` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `api_users` */

insert  into `api_users`(`id`,`user`,`password`,`active`) values 
(1,'brandon','827ccb0eea8a706c4c34a16891f84e7b',1),
(2,'mariab@gmail.com','67924da60d0d811572e5219a0802ee6f',1);

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add clients',7,'add_clients'),
(26,'Can change clients',7,'change_clients'),
(27,'Can delete clients',7,'delete_clients'),
(28,'Can view clients',7,'view_clients'),
(29,'Can add users',8,'add_users'),
(30,'Can change users',8,'change_users'),
(31,'Can delete users',8,'delete_users'),
(32,'Can view users',8,'view_users'),
(33,'Can add tokens',9,'add_tokens'),
(34,'Can change tokens',9,'change_tokens'),
(35,'Can delete tokens',9,'delete_tokens'),
(36,'Can view tokens',9,'view_tokens'),
(37,'Can add products',10,'add_products'),
(38,'Can change products',10,'change_products'),
(39,'Can delete products',10,'delete_products'),
(40,'Can view products',10,'view_products'),
(41,'Can add bills_ products',11,'add_bills_products'),
(42,'Can change bills_ products',11,'change_bills_products'),
(43,'Can delete bills_ products',11,'delete_bills_products'),
(44,'Can view bills_ products',11,'view_bills_products'),
(45,'Can add bills',12,'add_bills'),
(46,'Can change bills',12,'change_bills'),
(47,'Can delete bills',12,'delete_bills'),
(48,'Can view bills',12,'view_bills');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$320000$LDEQb2uzwE7kgKDLX5KvY1$AryJHipRQYVO1CprLgcWsCsZHOENGX6qzwXFXfrggbI=','2022-06-24 18:27:27.020074',1,'admin','','','',1,1,'2022-06-24 18:18:09.805192');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

insert  into `django_admin_log`(`id`,`action_time`,`object_id`,`object_repr`,`action_flag`,`change_message`,`content_type_id`,`user_id`) values 
(1,'2022-06-24 18:29:01.083053','1','Clients object (1)',1,'[{\"added\": {}}]',7,1),
(2,'2022-06-24 19:39:59.680716','1','Users object (1)',1,'[{\"added\": {}}]',8,1);

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(12,'api','bills'),
(11,'api','bills_products'),
(7,'api','clients'),
(10,'api','products'),
(9,'api','tokens'),
(8,'api','users'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2022-06-24 18:13:55.312629'),
(2,'auth','0001_initial','2022-06-24 18:13:58.482544'),
(3,'admin','0001_initial','2022-06-24 18:13:59.322094'),
(4,'admin','0002_logentry_remove_auto_add','2022-06-24 18:13:59.514562'),
(5,'admin','0003_logentry_add_action_flag_choices','2022-06-24 18:13:59.714381'),
(6,'contenttypes','0002_remove_content_type_name','2022-06-24 18:14:00.485254'),
(7,'auth','0002_alter_permission_name_max_length','2022-06-24 18:14:00.837977'),
(8,'auth','0003_alter_user_email_max_length','2022-06-24 18:14:01.152138'),
(9,'auth','0004_alter_user_username_opts','2022-06-24 18:14:01.352090'),
(10,'auth','0005_alter_user_last_login_null','2022-06-24 18:14:01.849857'),
(11,'auth','0006_require_contenttypes_0002','2022-06-24 18:14:02.049654'),
(12,'auth','0007_alter_validators_add_error_messages','2022-06-24 18:14:02.233443'),
(13,'auth','0008_alter_user_username_max_length','2022-06-24 18:14:02.695308'),
(14,'auth','0009_alter_user_last_name_max_length','2022-06-24 18:14:03.067323'),
(15,'auth','0010_alter_group_name_max_length','2022-06-24 18:14:03.370630'),
(16,'auth','0011_update_proxy_permissions','2022-06-24 18:14:03.811636'),
(17,'auth','0012_alter_user_first_name_max_length','2022-06-24 18:14:04.157373'),
(18,'sessions','0001_initial','2022-06-24 18:14:04.663612'),
(19,'api','0001_initial','2022-06-24 18:25:08.030051'),
(20,'api','0002_bills_products_users_tokens_bills_products','2022-06-24 19:12:16.564381'),
(21,'api','0003_alter_tokens_expiry_date','2022-06-24 19:15:56.379449');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('qrbn0qzpgffkleznbuskpaqonuqyrwnf','.eJxVjEsOAiEQBe_C2hCazwAu3XsG0jSNjBommc_KeHedZBa6fVX1XiLhtra0LTynsYizAHH63TLSg_sOyh37bZI09XUes9wVedBFXqfCz8vh_h00XNq3VjX4whQrD85T1TpWWyFbQOfYEhOYYAwMiNpZFYg9ZFNi1QFi0FGJ9wf0kjeu:1o4o1f:wcAstJvU_bUK2m12iNQHP4YmPjCnBrEykv31hBMUAgg','2022-07-08 18:27:27.103425');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
