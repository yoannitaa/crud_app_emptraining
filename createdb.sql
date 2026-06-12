-- 1. Create New Database
CREATE DATABASE employee_training;
use employee_training;

-- 2. Create Table employee_data
CREATE TABLE IF NOT EXISTS `employee_data` (
    `emp_id` CHAR(5) NOT NULL,
    `emp_name` VARCHAR(255) NOT NULL,
    `job_title` VARCHAR(255) NOT NULL,
    `dept_name` VARCHAR(255) NOT NULL,
    `emp_status` CHAR(20) NOT NULL,
    PRIMARY KEY (`emp_id`)
);

CREATE TABLE IF NOT EXISTS `training_data` (
    `training_id` INT NOT NULL,
    `training_name` VARCHAR(255) NOT NULL,
    `training_cat` CHAR(30) NOT NULL,
    `training_provider` VARCHAR(255),
    `training_valid` INT NOT NULL,
    PRIMARY KEY (`training_id`)
);

CREATE TABLE IF NOT EXISTS `training_history_data` (
    `tr_history_id` INT NOT NULL,
    `emp_id` CHAR(5) NOT NULL,
    `training_id` INT NOT NULL,
    `training_date` DATE NOT NULL,
    `training_status` CHAR(20) NOT NULL,
    PRIMARY KEY (`tr_history_id`)
);

CREATE TABLE IF NOT EXISTS `job_competencies` (
    `competency_id` INT NOT NULL,
    `job_title` VARCHAR(255) NOT NULL,
    `training_id` INT NOT NULL,
    `mandatory_status` CHAR(10) NOT NULL,
    PRIMARY KEY (`competency_id`)
);

-- Foreign key constraints
ALTER TABLE `training_history_data` ADD CONSTRAINT `fk_training_history_data_emp_id` FOREIGN KEY(`emp_id`) REFERENCES `employee_data`(`emp_id`);
ALTER TABLE `training_history_data` ADD CONSTRAINT `fk_training_history_data_training_id` FOREIGN KEY(`training_id`) REFERENCES `training_data`(`training_id`);
ALTER TABLE `job_competencies` ADD CONSTRAINT `fk_job_competencies_training_id` FOREIGN KEY(`training_id`) REFERENCES `training_data`(`training_id`);
