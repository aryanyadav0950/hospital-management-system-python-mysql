CREATE DATABASE hospital_db;
USE hospital_db;

CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    disease VARCHAR(200),
    room_no VARCHAR(10),
    bill_amount DECIMAL(10,2)
);
