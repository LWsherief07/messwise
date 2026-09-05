CREATE DATABASE IF NOT EXISTS messwise;

USE messwise;

-- Users and roles
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'manager', 'student') NOT NULL
);

-- Students
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    room_no VARCHAR(20),
);

-- Meals
CREATE TABLE meals (
    meal_id INT AUTO_INCREMENT PRIMARY KEY,
    meal_date DATE NOT NULL,
    meal_type ENUM('breakfast', 'lunch', 'dinner') NOT NULL,
    menu VARCHAR(255) NOT NULL
);

-- Attendance
CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    meal_id INT NOT NULL,
    ate BOOLEAN NOT NULL,

    FOREIGN KEY (student_id) REFERENCES students(student_id)
        ON DELETE CASCADE,

    FOREIGN KEY (meal_id) REFERENCES meals(meal_id)
        ON DELETE CASCADE,

    UNIQUE (student_id, meal_id)
);

-- Food and waste records
CREATE TABLE food_records (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    meal_id INT NOT NULL,
    food_prepared DECIMAL(10,2) NOT NULL,
    food_consumed DECIMAL(10,2) NOT NULL,
    food_wasted DECIMAL(10,2) NOT NULL,

    FOREIGN KEY (meal_id) REFERENCES meals(meal_id)
        ON DELETE CASCADE
);