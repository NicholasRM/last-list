-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 20, 2024 at 09:35 AM
-- Server version: 5.7.23-23
-- PHP Version: 8.1.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nicholas_lastlist`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$390000$3R4Gr56eiCwF1bWndJPFu8$/Pvsacu0qD0qRc19pQXFQaXuPPI40+dLI6zTyhaZN/o=', NULL, 0, 'bcorriveau24', 'Ben', 'Corriveau', 'briveau@uri.edu', 0, 1, '2024-04-20 14:20:41.637398'),
(2, 'pbkdf2_sha256$390000$iJwHFuIjbvUqRbaAYehJ6t$tYONYU9XcXM4SrtCLMfbs+2KnpDkLTr2+OCDkRa+oe4=', NULL, 0, 'amaguilar24', 'Alexis', 'Aguilar', 'amonroyaguilar@uri.edu', 0, 1, '2024-04-20 14:21:37.884019'),
(3, 'pbkdf2_sha256$390000$9hEfZf4DAVB9r6avIrK74j$PdUwucXKDrE4SVxsT7j6mV0IzAIWJ8/eBf7JhngDJ9A=', NULL, 0, 'sbrown24', 'Stephen', 'Brown', 'stephen.brown@uri.edu', 0, 1, '2024-04-20 14:22:36.709446'),
(4, 'pbkdf2_sha256$390000$0qptRi2RVwzeP1kArzb0xU$1zUyILV2zilMynhNOp6/SnAPvTNE56aWXJZcV7s54ek=', NULL, 0, 'ecalrson24', 'Ethan', 'Carlson', 'ethan-carlson@uri.edu', 0, 1, '2024-04-20 14:23:09.831968'),
(5, 'pbkdf2_sha256$390000$AJkH7wlEVMJFYJy0l4Iq00$Zu0SPFkK2g7jMyuj6AIKsNf258esidUjdCtA+mWG0g0=', NULL, 0, 'nmendes24', 'Nicholas', 'Mendes', 'nicholas_mendes@uri.edu', 0, 1, '2024-04-20 14:23:45.026810');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `city`
--

CREATE TABLE `city` (
  `city_id` int(11) NOT NULL,
  `city` tinytext COLLATE utf8_unicode_ci NOT NULL,
  `state` tinytext COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `city`
--

INSERT INTO `city` (`city_id`, `city`, `state`) VALUES
(1, 'Warwick', 'Rhode Island'),
(2, 'Swansea', 'Massachusetts'),
(3, 'Cranston', 'Rhode Island'),
(4, 'Lisbon', 'Connecticut'),
(5, 'Smithfield', 'Rhode Island'),
(6, 'Wakefield', 'Rhode Island');

-- --------------------------------------------------------

--
-- Table structure for table `contains`
--

CREATE TABLE `contains` (
  `list_id` int(10) UNSIGNED NOT NULL,
  `item_id` int(10) UNSIGNED NOT NULL,
  `is_replacement` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `contains`
--

INSERT INTO `contains` (`list_id`, `item_id`, `is_replacement`) VALUES
(13, 6, 0),
(13, 8, 0),
(14, 4, 0),
(14, 5, 0),
(15, 1, 0),
(17, 4, 0),
(17, 5, 0),
(17, 8, 0),
(17, 10, 0);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-04-20 14:13:44.509683'),
(2, 'auth', '0001_initial', '2024-04-20 14:13:46.087395'),
(3, 'admin', '0001_initial', '2024-04-20 14:13:46.494961'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-04-20 14:13:46.575218'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-04-20 14:13:46.657782'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-04-20 14:13:47.022485'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-04-20 14:13:47.194271'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-04-20 14:13:47.361029'),
(9, 'auth', '0004_alter_user_username_opts', '2024-04-20 14:13:47.438167'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-04-20 14:13:47.588562'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-04-20 14:13:47.658313'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-04-20 14:13:47.754130'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-04-20 14:13:47.925199'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-04-20 14:13:48.095580'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-04-20 14:13:48.275249'),
(16, 'auth', '0011_update_proxy_permissions', '2024-04-20 14:13:48.461988'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-04-20 14:13:48.629433'),
(18, 'sessions', '0001_initial', '2024-04-20 14:13:48.855130');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `item`
--

CREATE TABLE `item` (
  `item_id` int(11) UNSIGNED NOT NULL,
  `product_id` int(11) UNSIGNED NOT NULL,
  `quantity_id` int(11) UNSIGNED NOT NULL,
  `price_id` int(11) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `item`
--

INSERT INTO `item` (`item_id`, `product_id`, `quantity_id`, `price_id`) VALUES
(1, 1, 1, 2),
(2, 1, 2, 1),
(3, 2, 4, 5),
(4, 3, 6, 7),
(5, 4, 3, 4),
(6, 5, 5, 6),
(7, 2, 4, 3),
(8, 8, 9, 12),
(9, 7, 7, 5),
(10, 9, 10, 11),
(11, 11, 8, 13),
(12, 10, 1, 9),
(13, 10, 2, 10),
(14, 6, 5, 8);

-- --------------------------------------------------------

--
-- Table structure for table `list`
--

CREATE TABLE `list` (
  `list_id` int(10) UNSIGNED NOT NULL,
  `user_id` int(11) NOT NULL,
  `name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `date_created` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `list`
--

INSERT INTO `list` (`list_id`, `user_id`, `name`, `date_created`) VALUES
(1, 1, 'Grocery List', '2024-02-22'),
(2, 2, 'Holiday Gifts', '2024-01-15'),
(3, 3, 'Books List', '2024-02-01'),
(4, 4, 'Work Supplies', '2024-02-10'),
(5, 5, 'Home Improvement', '2023-02-20'),
(6, 1, 'Birthday Planning', '2024-03-01'),
(7, 2, 'Recipe Books', '2024-03-15'),
(8, 3, 'Fitness', '2024-03-20'),
(9, 4, 'For Travel', '2024-04-01'),
(10, 5, 'Research', '2024-04-10'),
(11, 1, 'Movies', '2024-04-15'),
(12, 2, 'Gardening Stuff', '2024-05-01'),
(13, 3, 'Weekly Meal List', '2024-05-15'),
(14, 4, 'DIY Projects', '2024-06-01'),
(15, 5, '4Beach', '2024-06-15'),
(16, 1, 'Book Club Selections', '2024-07-01'),
(17, 2, 'Back to School', '2024-07-15'),
(18, 3, 'Halloween Costumes', '2024-08-01'),
(19, 4, 'Thanksgiving Prep', '2024-08-15'),
(20, 5, 'Party', '2024-09-01');

-- --------------------------------------------------------

--
-- Table structure for table `price`
--

CREATE TABLE `price` (
  `price_id` int(11) UNSIGNED NOT NULL,
  `price` decimal(5,2) NOT NULL,
  `date_recorded` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `price`
--

INSERT INTO `price` (`price_id`, `price`, `date_recorded`) VALUES
(1, 14.44, '2023-10-05 00:00:00'),
(2, 7.49, '2023-10-05 12:30:00'),
(3, 5.31, '2023-10-15 06:24:01'),
(4, 1.89, '2023-10-16 00:00:00'),
(5, 4.98, '2023-11-01 03:29:00'),
(6, 5.98, '2024-01-01 15:28:20'),
(7, 7.89, '2024-01-20 02:40:07'),
(8, 20.59, '2024-02-22 11:29:36'),
(9, 11.99, '2024-02-23 12:30:30'),
(10, 12.39, '2024-02-23 13:40:30'),
(11, 1.89, '2024-02-23 17:30:30'),
(12, 10.58, '2024-02-23 15:03:01'),
(13, 5.48, '2024-02-24 04:00:30');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `product_id` int(11) UNSIGNED NOT NULL,
  `name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `brand` varchar(30) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`product_id`, `name`, `brand`) VALUES
(1, 'Coca Cola', 'Coca Cola'),
(2, 'Lay\'s Original', 'Lay\'s'),
(3, 'Printer Paper', 'Up & Up'),
(4, 'Ball Point Pen', 'bic'),
(5, '21 Whole Grains and Seeds', 'Dave\'s Killer Bread'),
(6, 'White Sandwich Bread', 'WONDER'),
(7, 'Creamy Peanut Butter', 'Jif'),
(8, '3 Subject Notebook - Black', 'FiveStar'),
(9, 'Two Pocket Folder - Blue', 'FiveStar'),
(10, 'Pulp Free Orange Juice', 'Tropicana'),
(11, 'Honey Mustard', 'Ken\'s Steakhouse');

-- --------------------------------------------------------

--
-- Table structure for table `product_rating`
--

CREATE TABLE `product_rating` (
  `user_id` int(11) NOT NULL,
  `product_id` int(10) UNSIGNED NOT NULL,
  `score` int(10) UNSIGNED NOT NULL,
  `date_recorded` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `product_rating`
--

INSERT INTO `product_rating` (`user_id`, `product_id`, `score`, `date_recorded`) VALUES
(1, 2, 2, '2024-02-25'),
(1, 5, 4, '2024-02-24'),
(2, 1, 4, '2024-02-19'),
(2, 2, 2, '2024-02-19'),
(2, 9, 2, '2024-02-25'),
(3, 8, 3, '2024-02-25'),
(4, 4, 4, '2024-02-13'),
(4, 7, 1, '2024-02-25'),
(5, 3, 5, '2024-02-17'),
(5, 4, 3, '2024-02-16'),
(5, 11, 1, '2024-02-25');

-- --------------------------------------------------------

--
-- Table structure for table `quantity`
--

CREATE TABLE `quantity` (
  `quantity_id` int(11) UNSIGNED NOT NULL,
  `measurement` int(11) NOT NULL,
  `unit` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `count` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `quantity`
--

INSERT INTO `quantity` (`quantity_id`, `measurement`, `unit`, `count`) VALUES
(1, 64, 'fluid ounces', 1),
(2, 12, 'fluid ounces', 12),
(3, 1, 'pen', 6),
(4, 13, 'ounces', 1),
(5, 27, 'ounces', 1),
(6, 750, 'sheets', 1),
(7, 40, 'ounces', 1),
(8, 24, 'ounces', 1),
(9, 1, 'notebook', 1),
(10, 1, 'folder', 1);

-- --------------------------------------------------------

--
-- Table structure for table `stock`
--

CREATE TABLE `stock` (
  `vendor_id` int(10) UNSIGNED NOT NULL,
  `item_id` int(10) UNSIGNED NOT NULL,
  `status` tinyint(3) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `stock`
--

INSERT INTO `stock` (`vendor_id`, `item_id`, `status`) VALUES
(1, 2, 0),
(2, 4, 0),
(4, 3, 1),
(5, 5, 1),
(8, 1, 1),
(8, 6, 0),
(9, 7, 0);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(10) UNSIGNED NOT NULL,
  `username` varchar(12) COLLATE utf8_unicode_ci NOT NULL,
  `fname` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `lname` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `password_hash` char(32) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `age` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `username`, `fname`, `lname`, `password_hash`, `email`, `age`) VALUES
(1, 'bcorriveau24', 'Ben', 'Corriveau', '5f4dcc3b5aa765d61d8327deb882cf99', 'briveau@uri.edu', 0),
(2, 'amaguilar24', 'Alexis', 'Aguilar', '5f4dcc3b5aa765d61d8327deb882cf99', 'amonroyaguilar@uri.edu', 0),
(3, 'sbrown24', 'Stephen', 'Brown', '5f4dcc3b5aa765d61d8327deb882cf99', 'stephen.brown@uri.edu', 0),
(4, 'ecarlson24', 'Ethan', 'Carlson', '5f4dcc3b5aa765d61d8327deb882cf99', 'ethan-carlson@uri.edu', 0),
(5, 'nmendes24', 'Nicholas', 'Mendes', '5f4dcc3b5aa765d61d8327deb882cf99', 'nicholas_mendes@uri.edu', 0),
(7, 'jordandoe12', 'Jordan', 'Doe', '5f4dcc3b5aa765d61d8327deb882cf99', 'jordandoe@uri.edu', 20);

-- --------------------------------------------------------

--
-- Table structure for table `vendor`
--

CREATE TABLE `vendor` (
  `vendor_id` int(10) UNSIGNED NOT NULL,
  `name` tinytext COLLATE utf8_unicode_ci NOT NULL,
  `street_number` int(10) UNSIGNED NOT NULL,
  `street_name` tinytext COLLATE utf8_unicode_ci NOT NULL,
  `city_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `vendor`
--

INSERT INTO `vendor` (`vendor_id`, `name`, `street_number`, `street_name`, `city_id`) VALUES
(1, 'Walmart', 840, 'Post Rd', 1),
(2, 'Target', 400, 'Bald Hill Rd', 1),
(3, 'Walmart', 54, 'Cousineau Dr', 2),
(4, 'Walmart', 1776, 'Plainfield Pike', 3),
(5, 'Target', 195, 'River Rd', 4),
(6, 'Target', 371, 'Putnam Pike', 5),
(7, 'Stop & Shop', 2470, 'Warwick Ave', 1),
(8, 'Stop & Shop', 275, 'Warwick Ave', 3),
(9, 'Shaw\'s', 160, 'Old Tower Hill Rd', 6);

-- --------------------------------------------------------

--
-- Table structure for table `vendor_rating`
--

CREATE TABLE `vendor_rating` (
  `user_id` int(11) NOT NULL,
  `vendor_id` int(10) UNSIGNED NOT NULL,
  `score` int(10) UNSIGNED NOT NULL,
  `date_recorded` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `vendor_rating`
--

INSERT INTO `vendor_rating` (`user_id`, `vendor_id`, `score`, `date_recorded`) VALUES
(1, 7, 5, '2024-02-25'),
(1, 9, 2, '2024-02-25'),
(2, 3, 3, '2024-02-25'),
(2, 4, 3, '2024-02-25'),
(2, 8, 3, '2024-02-22'),
(3, 3, 4, '2024-02-25'),
(3, 6, 4, '2024-02-25'),
(4, 1, 1, '2024-02-25'),
(4, 9, 3, '2024-02-25'),
(5, 2, 1, '2024-02-25'),
(5, 5, 4, '2024-02-22'),
(5, 6, 1, '2024-02-25');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `city`
--
ALTER TABLE `city`
  ADD PRIMARY KEY (`city_id`);

--
-- Indexes for table `contains`
--
ALTER TABLE `contains`
  ADD PRIMARY KEY (`list_id`,`item_id`),
  ADD KEY `item_id` (`item_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `item`
--
ALTER TABLE `item`
  ADD PRIMARY KEY (`item_id`),
  ADD KEY `price_id` (`price_id`),
  ADD KEY `product_id` (`product_id`),
  ADD KEY `quantity_id` (`quantity_id`);

--
-- Indexes for table `list`
--
ALTER TABLE `list`
  ADD PRIMARY KEY (`list_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `price`
--
ALTER TABLE `price`
  ADD PRIMARY KEY (`price_id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `product_rating`
--
ALTER TABLE `product_rating`
  ADD PRIMARY KEY (`user_id`,`product_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `quantity`
--
ALTER TABLE `quantity`
  ADD PRIMARY KEY (`quantity_id`);

--
-- Indexes for table `stock`
--
ALTER TABLE `stock`
  ADD PRIMARY KEY (`vendor_id`,`item_id`),
  ADD KEY `item_id` (`item_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `vendor`
--
ALTER TABLE `vendor`
  ADD PRIMARY KEY (`vendor_id`);

--
-- Indexes for table `vendor_rating`
--
ALTER TABLE `vendor_rating`
  ADD PRIMARY KEY (`user_id`,`vendor_id`),
  ADD KEY `vendor_id` (`vendor_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `city`
--
ALTER TABLE `city`
  MODIFY `city_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `item`
--
ALTER TABLE `item`
  MODIFY `item_id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `list`
--
ALTER TABLE `list`
  MODIFY `list_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `price`
--
ALTER TABLE `price`
  MODIFY `price_id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `product_id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `quantity`
--
ALTER TABLE `quantity`
  MODIFY `quantity_id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `vendor`
--
ALTER TABLE `vendor`
  MODIFY `vendor_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `contains`
--
ALTER TABLE `contains`
  ADD CONSTRAINT `contains_ibfk_1` FOREIGN KEY (`list_id`) REFERENCES `list` (`list_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `contains_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `item` (`item_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `item`
--
ALTER TABLE `item`
  ADD CONSTRAINT `item_ibfk_1` FOREIGN KEY (`price_id`) REFERENCES `price` (`price_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `item_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `item_ibfk_3` FOREIGN KEY (`quantity_id`) REFERENCES `quantity` (`quantity_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `list`
--
ALTER TABLE `list`
  ADD CONSTRAINT `list_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `product_rating`
--
ALTER TABLE `product_rating`
  ADD CONSTRAINT `product_rating_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `product_rating_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `stock`
--
ALTER TABLE `stock`
  ADD CONSTRAINT `stock_ibfk_1` FOREIGN KEY (`item_id`) REFERENCES `item` (`item_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `stock_ibfk_2` FOREIGN KEY (`vendor_id`) REFERENCES `vendor` (`vendor_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `vendor_rating`
--
ALTER TABLE `vendor_rating`
  ADD CONSTRAINT `vendor_rating_ibfk_2` FOREIGN KEY (`vendor_id`) REFERENCES `vendor` (`vendor_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `vendor_rating_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
