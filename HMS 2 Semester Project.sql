-- CREATE DATABASE
CREATE DATABASE HostelManagementSystem;

-- USE DATABASE
USE HostelManagementSystem;

-- =========================
-- WARDEN TABLE
-- =========================
CREATE TABLE Warden (
    warden_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    shift_time VARCHAR(50)
);

-- =========================
-- ROOM TABLE
-- =========================
CREATE TABLE Room (
    room_id INT PRIMARY KEY AUTO_INCREMENT,
    room_number VARCHAR(10) NOT NULL,
    capacity INT NOT NULL,
    status VARCHAR(20),
    warden_id INT,
    
    FOREIGN KEY (warden_id)
    REFERENCES Warden(warden_id)
);

-- =========================
-- STUDENT TABLE
-- =========================
CREATE TABLE Student (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    gender VARCHAR(10),
    phone VARCHAR(15),
    address VARCHAR(255),
    room_id INT,
    
    FOREIGN KEY (room_id)
    REFERENCES Room(room_id)
);

-- =========================
-- FEE TABLE
-- =========================
CREATE TABLE Fee (
    fee_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    amount DECIMAL(10,2),
    payment_date DATE,
    status VARCHAR(20),
    
    FOREIGN KEY (student_id)
    REFERENCES Student(student_id)
);

-- =========================
-- COMPLAINT TABLE
-- =========================
CREATE TABLE Complaint (
    complaint_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    complaint_text VARCHAR(255),
    complaint_date DATE,
    status VARCHAR(20),
    
    FOREIGN KEY (student_id)
    REFERENCES Student(student_id)
);complaint