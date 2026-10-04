CREATE DATABASE IF NOT EXISTS messwise;

USE messwise;

-- Users
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'student') NOT NULL
);


-- Meals
CREATE TABLE meals (
    meal_id INT PRIMARY KEY,
    meal_date DATE NOT NULL,
    meal_type ENUM('breakfast', 'lunch', 'dinner') NOT NULL,
    menu VARCHAR(255) NOT NULL,
    amnt INT NOT NULL
);

-- Attendance
CREATE TABLE attendance (
    user_id INT NOT NULL,
    meal_id INT NOT NULL,
    ate BOOLEAN DEFAULT FALSE,

    FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE CASCADE,

    FOREIGN KEY (meal_id) REFERENCES meals(meal_id)
        ON DELETE CASCADE,

    UNIQUE (user_id, meal_id)
);

-- Trigger (to automatically create new attendance record for every student (Default ate = False) when a new meal is added)

/*DELIMITER //

CREATE TRIGGER after_meal_insert
AFTER INSERT ON meals
FOR EACH ROW
BEGIN
    INSERT INTO attendance (user_id, meal_id, ate)
    SELECT user_id, NEW.meal_id, FALSE
    FROM users
    WHERE role = 'student';
END //

DELIMITER ;*/
