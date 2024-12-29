/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - career_guidance
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`career_guidance` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `career_guidance`;

/*Table structure for table `career_guidance` */

DROP TABLE IF EXISTS `career_guidance`;

CREATE TABLE `career_guidance` (
  `career_guidance_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `team_name` varchar(100) DEFAULT NULL,
  `office_place` varchar(100) DEFAULT NULL,
  `land_mark` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`career_guidance_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `career_guidance` */

insert  into `career_guidance`(`career_guidance_id`,`login_id`,`team_name`,`office_place`,`land_mark`,`pincode`,`phone`,`email`,`status`) values 
(1,4,'TEAM ABC','PALAKKAD','KSRTC STAND','455866','9048039943','neenu@gmail.com','accepted'),
(2,5,'GUIDANCE','Eranakulam','maharajas','986544','9048039943','mehanakroy2200@gmail.com','accepted');

/*Table structure for table `chats` */

DROP TABLE IF EXISTS `chats`;

CREATE TABLE `chats` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `sender_type` varchar(100) DEFAULT NULL,
  `receiver_id` varchar(100) DEFAULT NULL,
  `receiver_type` varchar(100) DEFAULT NULL,
  `message` varchar(100) DEFAULT NULL,
  `date_time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `chats` */

insert  into `chats`(`chat_id`,`sender_id`,`sender_type`,`receiver_id`,`receiver_type`,`message`,`date_time`) values 
(1,1,'student','1','career_guidance','hello','11/12/12'),
(2,2,'student','1','career_guidance','hii','10/05/12'),
(3,1,'career_guidance','1','student','hello...','2021-02-20 10:16:07'),
(4,1,'career_guidance','2','student','yesss','2021-02-20 10:16:22'),
(5,2,'student','2','career_guidance','hi','2024-12-28 09:42:38');

/*Table structure for table `courses` */

DROP TABLE IF EXISTS `courses`;

CREATE TABLE `courses` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `institute_id` int(11) DEFAULT NULL,
  `course_name` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `courses` */

insert  into `courses`(`course_id`,`institute_id`,`course_name`,`description`) values 
(1,1,'CS','hghvhjfytfr6'),
(2,1,'MATHS','iyguyg'),
(3,1,'BIO SCIENCE','sdgjghy');

/*Table structure for table `institutes` */

DROP TABLE IF EXISTS `institutes`;

CREATE TABLE `institutes` (
  `institute_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`institute_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `institutes` */

insert  into `institutes`(`institute_id`,`login_id`,`name`,`type`,`place`,`pincode`,`phone`,`email`) values 
(1,2,'GHSS CHATHANUR','school','PALAKKAD','679533','9947306829','jinjgjhg@gmail.com'),
(2,3,'GVHSS VATTENAD','school','PALAKKAD','685411','9947306829','neenu@gmail.com');

/*Table structure for table `job_applications` */

DROP TABLE IF EXISTS `job_applications`;

CREATE TABLE `job_applications` (
  `application_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `vacancy_id` int(11) DEFAULT NULL,
  `date_time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`application_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `job_applications` */

insert  into `job_applications`(`application_id`,`student_id`,`vacancy_id`,`date_time`) values 
(1,1,1,'11/14/20');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `user_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`user_type`) values 
(1,'admin','admin','admin'),
(2,'school','school','institute'),
(3,'school1','school1','institute'),
(4,'team','team','career_guidance'),
(5,'team1','team1','career_guidance'),
(6,'student','student','student'),
(7,'s','s','student');

/*Table structure for table `ratings` */

DROP TABLE IF EXISTS `ratings`;

CREATE TABLE `ratings` (
  `rate_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `career_guidance_id` int(11) DEFAULT NULL,
  `rate` varchar(100) DEFAULT NULL,
  `review` varchar(100) DEFAULT NULL,
  `date_time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`rate_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `ratings` */

insert  into `ratings`(`rate_id`,`student_id`,`career_guidance_id`,`rate`,`review`,`date_time`) values 
(1,1,1,'4','azxs','14/01/12'),
(2,1,2,'3','lkjui','14/10/20'),
(3,2,2,'4','ok','2024-12-26'),
(4,2,1,'5','very good','2024-12-26');

/*Table structure for table `resume` */

DROP TABLE IF EXISTS `resume`;

CREATE TABLE `resume` (
  `resume_id` int(11) NOT NULL AUTO_INCREMENT,
  `vacancy_id` int(11) DEFAULT NULL,
  `resume` varchar(100) DEFAULT NULL,
  `out` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`resume_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `resume` */

insert  into `resume`(`resume_id`,`vacancy_id`,`resume`,`out`) values 
(1,1,'static/320b01d6-0f2e-4a95-93fd-249bc8e6ae2fChildbg.png',NULL),
(2,2,'static/imagesfbd82d11-0fd6-4b05-af91-c317fd5995e5fine.jpg',NULL),
(3,2,'static/images00b39c8f-181a-47fd-bc3e-bd2dcc366136Childbg.png',NULL),
(4,1,'static/images/c716d2a9-140a-4d35-8b05-2d744bdeb225Smart_Transit_initial_phase_Report.pdf',NULL),
(5,1,'static/images/abe82386-dd33-4826-afef-c8d6b06fa5e9anomaly.pdf',NULL),
(6,1,'static/images/4b587efe-ad94-4048-b28d-7358e30dbd2fanomaly.pdf','ENFP'),
(7,1,'static/images/24e57165-5cd0-4956-867c-b91a42144836anomaly.pdf','ENFP');

/*Table structure for table `seminar_request` */

DROP TABLE IF EXISTS `seminar_request`;

CREATE TABLE `seminar_request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `seminar_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `date_time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `seminar_request` */

insert  into `seminar_request`(`request_id`,`seminar_id`,`student_id`,`status`,`date_time`) values 
(1,1,1,'rejected','11/12/20'),
(2,2,2,'accepted','14/12/20');

/*Table structure for table `seminars` */

DROP TABLE IF EXISTS `seminars`;

CREATE TABLE `seminars` (
  `seminar_id` int(11) NOT NULL AUTO_INCREMENT,
  `career_guidance_id` int(11) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `venue` varchar(100) DEFAULT NULL,
  `event_date_time` varchar(100) DEFAULT NULL,
  `date_time` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`seminar_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `seminars` */

insert  into `seminars`(`seminar_id`,`career_guidance_id`,`title`,`description`,`venue`,`event_date_time`,`date_time`,`status`) values 
(1,1,'BASIC JAVA','JHJJGFHFGTFD','CMD CENTER','2021-02-11T13:02','2021-02-20 10:02:12','pending'),
(2,1,'HOW TO BECOME A DEVELOPER','SFASGSDG','GHSS THOPPE','2021-10-14T10:00','2021-02-20 10:03:21','planed');

/*Table structure for table `students` */

DROP TABLE IF EXISTS `students`;

CREATE TABLE `students` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `house_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `students` */

insert  into `students`(`student_id`,`login_id`,`first_name`,`last_name`,`house_name`,`place`,`pincode`,`course_id`,`phone`,`email`) values 
(1,6,'AKSHAY','AK','PALATHINKAL','EKM','478512',3,'9874526334','neenu@gmail.com'),
(2,7,'AMAL','AS','MAGHODE','KOCHIN','678594',2,'9874561447','jisssa398@gmail.com');

/*Table structure for table `vacancies` */

DROP TABLE IF EXISTS `vacancies`;

CREATE TABLE `vacancies` (
  `vacancy_id` int(11) NOT NULL AUTO_INCREMENT,
  `career_guidance_id` int(11) DEFAULT NULL,
  `company_name` varchar(100) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `vacancy_count` varchar(100) DEFAULT NULL,
  `date_time` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`vacancy_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `vacancies` */

insert  into `vacancies`(`vacancy_id`,`career_guidance_id`,`company_name`,`post`,`vacancy_count`,`date_time`,`status`) values 
(1,1,'GALAXY','TRAINEE','10','2021-02-20 10:04:19','inactive'),
(2,1,'ABCD','TRAINEE','25','2021-02-20 10:04:37','active');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
