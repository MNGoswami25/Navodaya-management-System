/*
SQLyog Community v9.63 
MySQL - 5.1.45-community : Database - cs_project
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`cs_project` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `cs_project`;

/*Table structure for table `account` */

DROP TABLE IF EXISTS `account`;

CREATE TABLE `account` (
  `SR_NO` decimal(10,0) NOT NULL,
  `BANK` varchar(20) DEFAULT NULL,
  `ACCOUNT_NO` decimal(50,0) DEFAULT NULL,
  `IFSC` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`SR_NO`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `account` */

insert  into `account`(`SR_NO`,`BANK`,`ACCOUNT_NO`,`IFSC`) values ('5','sbi','789654123','sfdsfgs'),('100','SBI','963258714','Sbi00123'),('101','SBI','23651478','Sbino1234'),('102','PNB','65412307','Pn0123'),('103','PNb','7896541230','Pnb2345'),('104','LKN','78965412','lk1234'),('105','PNB','56982012','Pnb4157'),('106','sbi','14785985','sbino100'),('107','PNB','5456656','asd4152'),('108','PNB','12589635','sf45221'),('109','PNB','41598752','s45565'),('110','SBI','45565565','fhd45454'),('111','Sbi','78965412','sbi9985'),('112','Pnb','78965478521','pb234234'),('113','SBI','789654123','sbi1234'),('114','SBI','789658745','78965'),('116','Sbi','78965857','fd3234'),('117','Sbi','1246567534','sbi32224'),('118','sbi','789654123','dsdssds'),('129','asas','12121','asass2112');

/*Table structure for table `address` */

DROP TABLE IF EXISTS `address`;

CREATE TABLE `address` (
  `SR_NO` decimal(10,0) NOT NULL,
  `VILLAGE` varchar(50) NOT NULL,
  `POST_OFFICE` varchar(20) NOT NULL,
  `PIN_CODE` varchar(10) NOT NULL,
  `BLOCK` varchar(20) NOT NULL,
  `DISTRICT` varchar(20) NOT NULL,
  `STATE` varchar(20) NOT NULL,
  PRIMARY KEY (`SR_NO`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `address` */

insert  into `address`(`SR_NO`,`VILLAGE`,`POST_OFFICE`,`PIN_CODE`,`BLOCK`,`DISTRICT`,`STATE`) values ('100','Ranikhet','Ranikhet','263652','Tarikhet','Almora','Uttarakhand'),('101','Tarikhet','Tarikhet','263658','Tarikhet','Almora','Uttarakhand'),('102','Ranikhet','Tarikhet','263615','Tarikhet','Almora','Uttarakhand'),('103','Naula','Bhikiyasen','263653','Bhikiyasen','Almora','Uttarakhand'),('104','Papnai','Tarikhet','263625','Tarikhet','Almora','Uttarakhand'),('105','Chaunaliya','Chaunaliya','263652','Bhikiyasen','Almora','Uttarakhand'),('106','Chakhutiya','Bhikiyasen','263654','Bhikiyasen','Almora','Uttarakhand'),('107','Dhaka','naula','565847','Dwarahat','Almora','Uttarakhand'),('108','Barsila','Kharna','458745','Tarikhet','Almora','Uttarakhand'),('109','Golu','Bhikiyasen','458965','Lamgara','Almora','Uttarakhand'),('110','Chona','Dwarahat','365458','Dwarahat','Almora','Uttarakhand'),('111','Kosi','Kosi','263656','Hawalbag','Almora','Uttarakhand'),('112','Kote','Bhikiyasen','598685','Bhikiyasen','Almora','Uttarakhand'),('113','Gangoli','Saalt','45874','Saalt','Almora','Uttarakhand'),('114','Binser','Tarikhet','78954','Tarikhet','Almora','Uttarakhand'),('116','Theroli','Masi','78596','Bhikiyasen','Almora','Uttarakhand'),('117','Lachima','Salt','78596','Salt','Almora','Uttrakhand'),('118','masi','chachutiya','8547','bhikiyasen','almora','uttarakhand'),('120','fsdg','dfsg','dfsg','sdfgdf','dfsgd','dfg'),('129','Gujargari','Gahtti','26278','Bhikyashen','Almora','Almorauttralkhnd');

/*Table structure for table `house` */

DROP TABLE IF EXISTS `house`;

CREATE TABLE `house` (
  `HOUSE_ID` decimal(5,0) NOT NULL,
  `HOUSE_NAME` varchar(20) NOT NULL,
  `NO_OF_BOYS` int(5) DEFAULT NULL,
  `NO_OF_GIRLS` int(5) DEFAULT NULL,
  `HOUSE_MASTER` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`HOUSE_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `house` */

insert  into `house`(`HOUSE_ID`,`HOUSE_NAME`,`NO_OF_BOYS`,`NO_OF_GIRLS`,`HOUSE_MASTER`) values ('10','Corbett',0,0,'Ghansham joshi'),('20','Gangotri',0,0,'Arvind Kumar Gejwal'),('30','Nanda',0,0,'Atul Verma'),('40','Rajaji',0,0,'Raj kishora Uniyal');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `email` varchar(50) NOT NULL,
  `passwrd` varchar(50) NOT NULL,
  `type_user` varchar(10) DEFAULT 'user',
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`email`,`passwrd`,`type_user`,`name`) values ('cp123@gmail.com','1230','user','Chetan'),('deep123@gmail.com','1230','user','Deepanshu'),('dfgdsfgds','dgdsgds','user','dsfg'),('dgfd','dfsg','user','fdgd'),('dsfdf','fsdf','user','xdzfds'),('ff','fsd','user','fsf'),('ffa','ff','user','l;fjkj'),('fhgggfdh','gfhgh','user','jghfg'),('gk1234@gmail.com','123456','user','Ganesh'),('gsdgsklgjsdkg','gldskjgkls','user','klhgdskljgd'),('gyrtg','retwet','user','ertgewy'),('kb123@gmail.com','1230','user','Khuswant'),('km123@gmail.com','1230','user','kamal'),('kt123@gmail.com','1230','user','Kamal'),('ku1234@gmail.com','1230','user','khusu'),('ps123@gmail.com','1230','user','prabhanshu'),('ram12345@gmail.com','12300','user','pushkar'),('rgnv1234@gmail.com','1230','admin','Manoj'),('sdf','sdf','user','sfd'),('sdfsf','123','user','sdf'),('ssp1234@gmail.com','1230','user','Saurabh'),('xcss','xtftr','user','dxexc');

/*Table structure for table `student_data` */

DROP TABLE IF EXISTS `student_data`;

CREATE TABLE `student_data` (
  `SR_NO` decimal(10,0) NOT NULL,
  `NAME` varchar(50) NOT NULL,
  `FATHER_NAME` varchar(50) NOT NULL,
  `MOTHER_NAME` varchar(50) NOT NULL,
  `CONTACT_NO` decimal(50,0) NOT NULL,
  `DOB` date DEFAULT NULL,
  `GENDER` varchar(10) NOT NULL,
  `AADHAR` decimal(20,0) DEFAULT NULL,
  `RELIGION` varchar(10) NOT NULL,
  `HOUSE_ID` int(10) NOT NULL,
  `ADMISSION_DATE` date NOT NULL,
  `catagery` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`SR_NO`),
  UNIQUE KEY `AADHAR` (`AADHAR`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `student_data` */

insert  into `student_data`(`SR_NO`,`NAME`,`FATHER_NAME`,`MOTHER_NAME`,`CONTACT_NO`,`DOB`,`GENDER`,`AADHAR`,`RELIGION`,`HOUSE_ID`,`ADMISSION_DATE`,`catagery`) values ('100','Ravi','Ram','Rani','9638527410','2000-12-15','M','789654123014','Hindu',10,'2021-03-01',NULL),('101','Karan','Madhan','Kareena','9632587410','2003-11-15','M','789654123012','Hindu',10,'2021-03-02','obc'),('102','Reema Joshi','Jitandra','Geeta','7896523654','2003-12-16','F','7896541230','Hindu',30,'2021-03-05','Gen'),('103','Geeta','Pandey','Sita','7896541230','2002-10-20','F','745632018974','Hindu',20,'2021-03-05','sc'),('104','Deepak','Dhani','Chandni','7458965874','2004-05-15','M','458796320145','Hindu',40,'2021-03-05','Gen'),('105','Shalani','Mohan','Seeta','4578963254','2006-04-21','F','478596325478','Hindu',10,'2021-03-05','SC'),('106','Mohan','Lalit','Shalu','7896541201','2004-11-15','M','458796325410','Hindu',20,'2021-03-05','SC'),('107','Vikash','GIrish','Geeta','7896582589','2003-06-06','M','482369852014','Hindu',30,'2021-03-05','OBC'),('108','Anju','Kamal','Suman','7895412036','2005-08-19','F','859674123085','Hindu',40,'2021-03-05','Obc'),('109','Mohit','Manish','MOhini','9856987458','2002-11-01','M','78965412301','Hindu',20,'2021-03-20','obc'),('110','Suman','Raja','Devi','8574963214','2002-10-05','F','789658745896','Hindu',30,'2021-03-20','Gen'),('111','Rohit Joshi','Raj Kumar Joshi','Radha Joshi','9988776655','2000-01-04','M','786954321234','hINDU',40,'2021-03-23','gen'),('112','Kamlesh Giri','Vimal','Maya','7896587458','2002-01-12','M',NULL,'hindu',10,'2021-03-23','obc'),('113','Vinay Bisht','Gopal Bisht','Shanti Devi','1745869855','2002-01-15','M','789654123654','Hindu',20,'2021-03-27','Gen'),('114','Rohan Kumar','Ravi','Radha','7896859874','2002-01-15','M','741896589741','Hindu',30,'2021-03-27','sc'),('116','Deepak Adhikari','Kamal Adhikari','Khusi Devi','7896587410','2002-01-15','M',NULL,'Hindu',10,'2021-03-30','gen'),('117','Parul Goswami','John ','Radha','7896541023','2002-01-15','F',NULL,'Hindu',20,'2021-03-31','obc'),('118','Harshit Sharma','Deepak Sharma','Deepa Sharma','7896541589','2000-01-15','M','745896369852','Hindu',40,'2021-04-08','gen'),('119','Chetan Kumar','Arun Kumar','Sita Devi','7412589635','2000-09-07','M','234567654323','Hindu',30,'2021-04-08','sc'),('120','Arun','Ram','Rani','7485748578','2001-05-06','M','987656787654','HIndu',40,'2021-04-08','obc'),('121','Ram','Sham','Radha','3232233232','2002-04-04','M','789609876543','HIndu',10,'2021-04-08','st'),('122','faul','kaul','naul','7458745874','2002-01-09','f',NULL,'hindu',10,'2021-04-08','st'),('123','kalu','lalu','nalu','7896578545','2001-03-04','m',NULL,'hindu',20,'2021-04-08','st'),('124','shaym','ram','radha','7458963210','2001-04-05','m','202928272623','ddsf',30,'2021-04-08','af'),('125','dsf','dsf','df','1111111111','2003-02-02','m','222222222222','fdsf',20,'2021-04-08','dsf'),('126','dsf','sdaf','df','4444444444','2002-04-04','m','323232323232','grdgf',30,'2021-04-08','dfgd'),('127','sadf','df','df','5555555555','2001-06-06','m','111111111111','adf',40,'2021-04-08','dfa'),('128','Rohit Shaarma','Karan Sharma','Tulsi Devi','7896541233','2002-04-05','M',NULL,'Hundu',10,'2021-04-11','gen'),('129','dipanshu','asaa','sdswe','1234567890','2004-03-01','m','121212121212','Hindu',20,'2021-04-11','gen');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
