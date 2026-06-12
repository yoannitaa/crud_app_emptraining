USE employee_training;
-- query employee training data
select * from employee_data where employee_data.emp_status ="Aktif";

select * from training_history_data where year(training_history_data.training_date) =2025;

SELECT 
	a.*,
    b.training_id,
    b.training_date,
    b.training_status
FROM employee_data a
LEFT JOIN training_history_data b
ON a.emp_id = b.emp_id;

SELECT 
    training_cat,
    COUNT(training_id) AS total_training
FROM training_data
GROUP BY training_cat;

SELECT
	COUNT(training_id) AS training_aktif
FROM
	training_history_data a
INNER JOIN employee_data b ON a.emp_id = b.emp_id
WHERE b.emp_status = "Aktif" and a.training_status ="Aktif";
