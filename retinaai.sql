-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 18, 2026 at 07:09 PM
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
-- Database: `retinaai`
--

-- --------------------------------------------------------

--
-- Table structure for table `scanrecord`
--

CREATE TABLE `scanrecord` (
  `id` int(11) NOT NULL,
  `scan_code` varchar(20) DEFAULT NULL,
  `patient_code` varchar(20) NOT NULL,
  `image_path` varchar(255) NOT NULL,
  `diagnosis` varchar(255) NOT NULL,
  `severity` varchar(255) NOT NULL,
  `confidence` float NOT NULL,
  `timestamp` datetime NOT NULL,
  `notes` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `scanrecord`
--

INSERT INTO `scanrecord` (`id`, `scan_code`, `patient_code`, `image_path`, `diagnosis`, `severity`, `confidence`, `timestamp`, `notes`) VALUES
(1, NULL, 'UNKNOWN', 'uploads/64381e57-6b3c-427c-ba1f-58cf48c9d176.jpg', 'No_DR', 'No_DR', 0.999987, '2026-03-13 05:36:26', NULL),
(2, NULL, 'UNKNOWN', 'uploads/f297c26e-25a1-4a08-84b4-9365609e257b.jpg', 'Moderate', 'Moderate', 0.512675, '2026-03-13 05:36:36', NULL),
(3, NULL, 'UNKNOWN', 'uploads/6ecc7b8c-2d70-47e5-9e9d-90169d1ad484.jpg', 'Moderate', 'Moderate', 0.556759, '2026-03-13 05:36:51', NULL),
(4, NULL, 'UNKNOWN', 'uploads/7bec64a9-632a-474c-b500-62bc35fab602.jpg', 'Proliferative_DR', 'Proliferative_DR', 0.603544, '2026-03-13 05:37:01', NULL),
(5, 'RA-SCAN-0005', 'RA-PAT-0011', 'uploads/be363803-6bf2-4d72-98bc-84e2c7c89eb6.jpg', 'Moderate', 'Moderate', 0.556759, '2026-03-13 08:31:10', NULL),
(6, 'RA-SCAN-0006', 'RA-PAT-0014', 'uploads/132782da-a159-4d72-9ad0-56d535a11253.jpg', 'Moderate', 'Moderate', 0.601561, '2026-03-15 08:29:28', NULL),
(7, 'RA-SCAN-0007', 'RA-PAT-0014', 'uploads/0c46ab32-0363-4286-9f48-8809197aa3e0.jpg', 'Moderate', 'Moderate', 0.602869, '2026-03-15 08:29:42', NULL),
(8, 'RA-SCAN-0008', 'RA-PAT-0014', 'uploads/f0926727-8f22-4abe-82f5-97bffd235d38.jpg', 'Moderate', 'Moderate', 0.600471, '2026-03-15 08:29:50', NULL),
(9, 'RA-SCAN-0009', 'RA-PAT-0014', 'uploads/1fc04460-9d62-4685-836d-459d4ae4715b.jpg', 'Moderate', 'Moderate', 0.602166, '2026-03-15 08:30:08', NULL),
(10, 'RA-SCAN-0010', 'RA-PAT-0014', 'uploads/7969a280-b8ec-41ea-acdb-7adaaf17042c.jpg', 'Moderate', 'Moderate', 0.609192, '2026-03-15 08:37:48', NULL),
(11, 'RA-SCAN-0011', 'RA-PAT-0014', 'uploads/ca74f64c-b0e0-4b65-93f2-d9850dad5226.jpg', 'Moderate', 'Moderate', 0.609688, '2026-03-15 08:37:55', NULL),
(12, 'RA-SCAN-0012', 'RA-PAT-0014', 'uploads/15161032-b777-4328-b057-e87e61fe839f.jpg', 'Moderate', 'Moderate', 0.608649, '2026-03-15 08:38:13', NULL),
(13, 'RA-SCAN-0013', 'RA-PAT-0014', 'uploads/be0aab20-cf8c-4932-92a2-f1caa9c54c89.jpg', 'Moderate', 'Moderate', 0.609192, '2026-03-15 08:38:38', NULL),
(14, 'RA-SCAN-0014', 'RA-PAT-0014', 'uploads/cc2deb0d-eab7-4f38-bca3-98b6a15fe27c.jpg', 'Moderate', 'Moderate', 0.512675, '2026-03-15 09:26:15', NULL),
(15, 'RA-SCAN-0015', 'RA-PAT-0014', 'uploads/9218af67-037a-4532-a430-3e4e4026d190.jpg', 'No_DR', 'No_DR', 0.926024, '2026-03-15 09:26:21', NULL),
(16, 'RA-SCAN-0016', 'RA-PAT-0014', 'uploads/b78609b6-25cf-4e28-bd21-84559c2c9d2d.jpg', 'No_DR', 'No_DR', 0.999987, '2026-03-15 09:26:29', NULL),
(17, 'RA-SCAN-0017', 'RA-PAT-0014', 'uploads/e026cfee-9e74-4095-9b1b-43e4b239a45a.jpg', 'Moderate', 'Moderate', 0.556759, '2026-03-15 09:26:38', NULL),
(18, 'RA-SCAN-0018', 'RA-PAT-0014', 'uploads/5ed62e77-013b-4d4c-a326-dcb2e47e6697.jpg', 'Mild', 'Mild', 0.761139, '2026-03-15 09:26:44', NULL),
(19, 'RA-SCAN-0019', 'RA-PAT-0014', 'uploads/1b1d0568-5f99-46f4-aebf-dcd431ae0b9e.jpg', 'No_DR', 'No_DR', 0.926024, '2026-03-15 09:43:29', NULL),
(20, 'RA-SCAN-0020', 'RA-PAT-0014', 'uploads/d84cc2ba-cf6d-4549-ac19-13c1fc84c5f0.jpg', 'Mild', 'Mild', 0.761139, '2026-03-15 09:43:41', NULL),
(21, 'RA-SCAN-0021', 'RA-PAT-0014', 'uploads/b233f7d4-e24f-4b23-b176-8438840e3cfd.jpg', 'Mild', 'Mild', 0.761139, '2026-03-15 11:08:48', NULL),
(22, 'RA-SCAN-0022', 'RA-PAT-0014', 'uploads/9506e348-8607-42cb-a020-75c09a4b46d1.jpg', 'Severe', 'Severe', 0.696451, '2026-03-15 12:00:26', NULL),
(23, 'RA-SCAN-0023', 'RA-PAT-0014', 'uploads/beb9cbf7-b5ea-4a07-80a1-c66d7d397dba.jpg', 'Severe', 'Severe', 0.696451, '2026-03-15 12:16:12', NULL),
(24, 'RA-SCAN-0024', 'RA-PAT-0014', 'uploads/71bc6d8b-0a81-4c4c-88c9-fcdd73ddb451.jpg', 'Severe', 'Severe', 0.696451, '2026-03-15 12:21:30', NULL),
(25, 'RA-SCAN-0025', 'RA-PAT-0014', 'uploads/fe300436-b18c-430b-838c-2bd6fd04f714.jpg', 'Severe', 'Severe', 0.696451, '2026-03-15 12:43:13', NULL),
(26, 'RA-SCAN-0026', 'RA-PAT-0014', 'uploads/6feced88-5dcd-4f26-89ef-5775627d6b89.jpg', 'Severe', 'Severe', 0.696451, '2026-03-15 12:46:40', NULL),
(27, 'RA-SCAN-0027', 'RA-PAT-0014', 'uploads/ca880552-1ab8-49cb-95a1-7cf280df407a.jpg', 'Severe', 'Severe', 0.696451, '2026-03-15 12:50:11', NULL),
(28, 'RA-SCAN-0028', 'RA-PAT-0014', 'uploads/25ba8da0-33c3-488a-aa95-959bac14f5c7.jpg', 'Severe', 'Severe', 0.696451, '2026-03-15 12:51:06', NULL),
(29, 'RA-SCAN-0029', 'RA-PAT-0014', 'uploads/c00d9142-c3ea-425b-bcec-8f41ee439d91.jpg', 'Severe', 'Severe', 0.696451, '2026-03-15 12:56:20', NULL),
(30, 'RA-SCAN-0030', 'RA-PAT-0014', 'uploads/2569206e-53ae-42eb-909d-fa905c9d702b.jpg', 'Severe', 'Severe', 0.696451, '2026-03-15 12:56:38', NULL),
(31, 'RA-SCAN-0031', 'RA-PAT-0014', 'uploads/68860627-caaf-4805-a71b-839e44b9ee19.jpg', 'Severe', 'Severe', 0.696451, '2026-03-15 13:01:11', NULL),
(32, 'RA-SCAN-0032', 'RA-DOC-0026', 'uploads/54ea1c33-d46b-4ea0-b957-5af09483c8b0.jpg', 'Severe', 'Severe', 0.696451, '2026-03-16 04:12:24', NULL),
(33, 'RA-SCAN-0033', 'RA-DOC-0026', 'uploads/8a6333ca-3f05-46c5-adda-7b4da634f2ce.jpg', 'Severe', 'Severe', 0.696451, '2026-03-16 04:12:46', NULL),
(34, 'RA-SCAN-0034', 'RA-DOC-0026', 'uploads/59d33909-432c-4eba-aa1f-ddb5022f0f11.jpg', 'Severe', 'Severe', 0.696451, '2026-03-16 04:12:49', NULL),
(35, 'RA-SCAN-0035', 'RA-PAT-0014', 'uploads/2dd4b928-2f98-4db2-b7e9-1fc9c904eeb3.jpg', 'Severe', 'Severe', 0.696451, '2026-03-21 04:06:11', NULL),
(36, 'RA-SCAN-0036', 'RA-PAT-0014', 'uploads/4c129271-7075-490d-ac93-6b14ca77bd2a.jpg', 'Severe', 'Severe', 0.696451, '2026-03-21 04:36:47', NULL),
(37, 'RA-SCAN-0037', 'RA-PAT-0014', 'uploads/58a5c1ae-2e9f-403a-9f85-2cbd910204f9.jpg', 'Severe', 'Severe', 0.501456, '2026-03-21 10:15:30', NULL),
(38, 'RA-SCAN-0038', 'RA-PAT-0014', 'uploads/6664d22f-5b81-4ef8-b992-91fdbbbf75c3.jpg', 'No_DR', 'No_DR', 0.462388, '2026-03-21 11:49:54', NULL),
(39, 'RA-SCAN-0039', 'RA-PAT-0014', 'uploads/40f6e128-fa42-4c3e-b2cb-2bbf3380acb9.jpg', 'No_DR', 'No_DR', 0.462388, '2026-03-21 11:50:32', NULL),
(40, 'RA-SCAN-0040', 'RA-PAT-0014', 'uploads/3d52d828-d205-4ae2-a438-5bcfe2b672bf.jpg', 'Severe', 'Severe', 0.501456, '2026-03-21 11:59:20', NULL),
(41, 'RA-SCAN-0041', 'RA-PAT-0014', 'uploads/c8500488-675d-4df6-b18b-2961ef3950aa.jpg', 'Severe', 'Severe', 0.501456, '2026-03-23 15:29:24', NULL),
(42, 'RA-SCAN-0042', 'RA-PAT-0014', 'uploads/07208890-c5a3-4e23-b5ff-42e44479d2fb.jpg', 'Severe', 'Severe', 0.501456, '2026-03-24 04:02:14', NULL),
(43, 'RA-SCAN-0043', 'RA-DOC-0026', 'uploads/9c573175-e41e-456b-93c6-6e2c313f0847.jpg', 'Severe', 'Severe', 0.501456, '2026-03-24 04:03:23', NULL),
(44, 'RA-SCAN-0044', 'RA-DOC-0026', 'uploads/f55d2ee7-abcb-4c27-b2d8-f6abaaf1cf16.jpg', 'Severe', 'Severe', 0.501456, '2026-03-24 04:21:01', NULL),
(45, 'RA-SCAN-0045', 'RA-DOC-0026', 'uploads/44fa45dc-ee75-42c0-9ad4-7f59e7aeab64.jpg', 'Severe', 'Severe', 0.501456, '2026-03-24 04:21:03', NULL),
(46, 'RA-SCAN-0046', 'RA-PAT-0014', 'uploads/924b842c-e0ad-4026-a21d-cff5fec5a7e5.jpg', 'Severe', 'Severe', 0.680306, '2026-03-24 04:44:14', NULL),
(47, 'RA-SCAN-0047', 'RA-PAT-0014', 'uploads/d0306c38-7849-406f-a39a-0ea0bc142f8c.jpg', 'Severe', 'Severe', 0.501456, '2026-03-24 04:46:35', NULL),
(48, 'RA-SCAN-0048', 'RA-PAT-0014', 'uploads/9718bdb2-b89b-4e41-bfcc-bffcea28bfd9.jpg', 'Severe', 'Severe', 0.501456, '2026-03-24 08:26:01', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `patient_code` varchar(20) DEFAULT NULL,
  `full_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `password_hash` varchar(255) DEFAULT NULL,
  `role` varchar(255) NOT NULL,
  `is_verified` tinyint(1) NOT NULL,
  `otp_code` varchar(255) DEFAULT NULL,
  `otp_expiry` datetime DEFAULT NULL,
  `medical_license_id` varchar(255) DEFAULT NULL,
  `specialization` varchar(255) DEFAULT NULL,
  `hospital_name` varchar(255) DEFAULT NULL,
  `experience` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `is_active` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `patient_code`, `full_name`, `email`, `phone`, `password_hash`, `role`, `is_verified`, `otp_code`, `otp_expiry`, `medical_license_id`, `specialization`, `hospital_name`, `experience`, `created_at`, `is_active`) VALUES
(1, NULL, 'Test Patient', 'testpatient@example.com', '1234567890', '$2b$12$yiOcSeelLapKsZfBt8tgeux4gB4vNKCwD7BjIkh.S6X9NgUAjSgqK', 'Patient', 1, NULL, NULL, NULL, NULL, NULL, NULL, '2026-03-15 12:41:04', 1),
(2, NULL, 'Test Doctor', 'testdoctor@example.com', '0987654321', 'testdoctor@123', 'Doctor', 1, NULL, NULL, 'MD12345', 'Retina Specialist', 'General Hospital', '10 years', '2026-03-15 12:41:04', 1),
(14, 'RA-PAT-0014', 'Bhargav Reddy ', 'bhargavreddynakkala10@gmail.com', '9381464041', '$2b$12$tHtkub1bOF1Axq625mnhbOi15.nPSKCF/IlGAKDqEvyBxVBQo52gu', 'Patient', 1, NULL, NULL, NULL, NULL, NULL, NULL, '2026-03-15 07:53:41', 1),
(26, 'RA-DOC-0026', 'sudheer Reddy ', 'bhargavreddyn0266.sse@saveetha.com', '9876543141', '$2b$12$L.D4GeY3VaLw1AbY.ucxueltgWbItO1TcBQazScgcUqF2YTti11US', 'Doctor', 1, NULL, NULL, 'MD12345', 'Retina Specialist', 'General Hospital', '10 years', '2026-03-16 03:35:23', 1),
(29, 'RA-DOC-0029', 'bhargav', 'bhargavreddynakkala@gmail.com', '9381464041', '$2b$12$0MTvI0BQwvddzmxv9x0isOsa7K2VQhhiAqK4IFSH30bPpqM2dyotC', 'Doctor', 1, '236324', '2026-03-21 12:49:16', 'docjshs', 'opthalmologist ', 'apollo ', '4 years', '2026-03-21 12:44:16', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `scanrecord`
--
ALTER TABLE `scanrecord`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `scan_code` (`scan_code`),
  ADD UNIQUE KEY `scan_code_2` (`scan_code`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ix_user_email` (`email`),
  ADD UNIQUE KEY `patient_code` (`patient_code`),
  ADD KEY `ix_user_medical_license_id` (`medical_license_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `scanrecord`
--
ALTER TABLE `scanrecord`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
