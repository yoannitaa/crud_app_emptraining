# Python CRUD Application for [Business Domain]

A Python application for managing employee training inventory data with Create, Read, Update, and Delete (CRUD) operations — integrated with a MySQL relational database for persistent and structured data storage.

## Business Understanding

This project caters to the banking or financial industry, specifically addressing the need to manage employee training data efficiently. Employee training inventory plays a crucial role in ensuring that employees have skills and competencies that align with the job requirements of the organization.

**Benefits:**

* Improved data accuracy and consistency of employee training records
* Streamlined employee training data management processes
* Easier monitoring of training requirements within each department
* Better tracking of employee competency compliance within the organization
* Real-time access to employee training history and status
* Reduced risk of errors from manual training records
* Better coordination between Employees, HR Staff, and Employee Managers

**Target Users:**

This application is designed for Employees, HR Departments, and Employee Managers within the organization to facilitate skill and competency tracking related to training requirements.

## Features

* **Create:**
* Add new training history entries by referencing existing employee and training data from the database
* Validates that the Employee ID (emp_id) and Training ID (training_id) exist in the database before inserting
* Prevents duplicate entries by checking for existing tr_history_id
* **Read:**
    * Display all employee training records joined from employee_data, training_history_data, and training_data tables
    * Search and retrieve specific employee training records filtered by Employee ID (NIP)
    * Displays comprehensive information including name, job title, department, training name, category, provider, date, validity, and status
* **Update:**
    * Modify existing training history records (training_date, training_status) based on Employee ID
    * Supports selection of specific training record if an employee has multiple training history entries
    * Provides clear confirmation prompts before saving changes
* **Delete:**
    * Remove training history records based on Employee ID
    * Supports selection of specific record if multiple entries exist for one employee
    * Confirmation prompt before permanent deletion

## Installation

1. **Prerequisites:**
    * Python 3.7 or later
    * MySQL Server (local or remote)
    * mysql-connector-python package

2. **Installation:**
    ```bash
   git clone https://github.com/yoannitaa/crud_app_emptraining.git
   cd employee_training_app
    ```
   ```bash
   pip install mysql-connector-python
   ```
    
3. **Database Setup (if applicable):**
    Open MySQL and run the database creation script:
   ```bash
   mysql -u root -p < createdb.sql
   ```
   Populate the database with sample data:
   ```bash
   mysql -u root -p < input_employeetrain.sql
   ```
   Update the database credentials in main.py:
   ```bash
   DB_CONFIG = {
    "host": "localhost",
    "user": "root",       # your MySQL username
    "password": "",       # your MySQL password
    "database": "employee_training"}
   ```

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Add a new training history entry by providing a unique TR History ID, a valid Employee ID (NIP), a valid Training ID, training date (YYYY-MM-DD format), and training status.
    * **Read:** SView all training records, or search by Employee ID (NIP) to see a specific employee's training history.
    * **Update:** Modify training_date or training_status of an existing training history record by Employee ID.
    * **Delete:** Remove a training history record by Employee ID. If the employee has multiple records, you will be prompted to choose which one to delete.

## Data Model
This project uses a MySQL relational database (employee_training) consisting of 4 tables:
employee_data
| Column    | Type         | Constraint            | Description                      |
|-----------|--------------|----------------------|----------------------------------|
| emp_id    | CHAR(5)      | PRIMARY KEY, NOT NULL | Unique employee ID (NIP)         |
| emp_name  | VARCHAR(255) | NOT NULL              | Employee full name               |
| job_title | VARCHAR(255) | NOT NULL              | Employee job title               |
| dept_name | VARCHAR(255) | NOT NULL              | Employee department              |
| emp_status| CHAR(20)     | NOT NULL              | Employment status (Aktif / Resign)|

training_data
| Column | Type | Constraint | Description |
|---|---|---|---|
| training_id | INT | PRIMARY KEY, NOT NULL | Unique training ID |
| training_name | VARCHAR(255) | NOT NULL | Training name |
| training_cat | CHAR(30) | NOT NULL | Category (sertifikasi / non sertifikasi) |
| training_provider | VARCHAR(255) | - | Training provider name |
| training_valid | INT | NOT NULL | Validity in years (0 = no expiry) |

training_history_data
| Column | Type | Constraint | Description |
|---|---|---|---|
| tr_history_id | INT | PRIMARY KEY, NOT NULL | Unique history record ID |
| emp_id | CHAR(5) | FOREIGN KEY, NOT NULL | References employee_data.emp_id |
| training_id | INT | FOREIGN KEY, NOT NULL | References training_data.training_id |
| training_date | DATE | NOT NULL | Date the training was completed |
| training_status | CHAR(20) | NOT NULL | Training status (Aktif / Expired) |

job_competencies
| Column | Type | Constraint | Description |
|---|---|---|---|
| competency_id | INT | PRIMARY KEY, NOT NULL | Unique competency ID |
| job_title | VARCHAR(255) | NOT NULL | Job title |
| training_id | INT | FOREIGN KEY, NOT NULL | References training_data.training_id |
| mandatory_status | CHAR(10) | NOT NULL | Whether mandatory for the job (Ya / Tidak) |

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to [your_email] or submit an issue if you encounter any problems or have suggestions for improvements.

