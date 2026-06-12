USE employee_training;

-- 1. Menambah records kedalam tabel employee_data
INSERT INTO employee_data (emp_id, emp_name, job_title, dept_name, emp_status) VALUES
	("Di001", "Dila", "Officer Liquidity Risk", "Market & Liquidity Risk", "Aktif"),
    ("Al002", "Alia", "Officer Talent Acquisition", "Human Resource", "Aktif"),
    ("Ja003", "Jason", "Data Analyst", "Management Information", "Aktif"),
    ("Ji004", "Jisoo", "Senior Data Analyst", "Management Information", "Resign"),
    ("Ru005", "Rumi", "Team Leader Treasury System", "Treasury Operation", "Aktif");
    
-- 2. Menambah records kedalam tabel training_data
INSERT INTO training_data (training_id, training_name, training_cat, training_provider, training_valid) VALUES
	(1, "Manajemen Risiko Jenjang 4", "sertifikasi", "LSPP", 4),
    (2, "Pelatihan Rekrutmen dan Seleksi", "non sertifikasi", "Biro Sumber Daya", 0),
    (3, "Visualisasi Data", "non sertifikasi", "PT Cyber Data", 0),
    (4, "Basic Capital Market", "non sertifikasi", "Biro Sumber Daya", 0),
    (5, "Adminstrasi Treasury Operation", "sertifikasi", "PT Keuangan", 2);

-- 3. Menambah records kedalam tabel training_history_data
INSERT INTO training_history_data (tr_history_id, emp_id, training_id, training_date, training_status) VALUES
	(1, "Di001", 1, "2026-05-15", "Aktif"),
    (2, "Al002", 2, "2025-12-22", "Aktif"),
    (3, "Ja003", 3, "2026-01-12", "Aktif"),
    (4, "Ji004", 3, "2026-03-13", "Aktif"),
    (5, "Ru005", 5, "2023-10-11", "Expired");

-- 4. Menambah records kedalam tabel job_competencies
INSERT INTO job_competencies (competency_id, job_title, training_id, mandatory_status) VALUES
	(1, "Officer Liquidity Risk", 1, "Ya"),
    (2, "Officer Liquidity Risk", 4, "Tidak"),
    (3, "Data Analyst", 3, "Ya"),
    (4, "Team Leader Treasury System", 4, "Ya"),
    (5, "Team Leader Treasury System", 5, "Ya");
