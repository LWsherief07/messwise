# Messwise Project Context

## 1. Introduction

Messwise is a food waste management system designed to address the recurring problem of excessive food wastage in messes, hostels, cafeterias, and institutional dining facilities around the world. In many places, food is prepared without accurate insight into actual attendance, consumption patterns, or meal demand, which leads to surplus food, financial loss, and unnecessary waste.

This project presents a practical digital solution to reduce waste by tracking meal records, student attendance, and consumption trends in a structured and efficient manner. It is implemented as a Python command-line application with a MySQL database backend and is designed to support role-based operations for administrators and students.

## 2. Objectives

The main objectives of the project are:

- Reduce food wastage in mess operations by making meal preparation decisions more data-driven.
- Manage student records in a hostel or mess environment.
- Track meals by date and type, such as breakfast, lunch, and dinner.
- Record meal attendance to reflect actual consumption patterns.
- Generate basic reports to identify waste and estimate recommended preparation quantities.
- Provide role-based access control so that only authorized users can access certain functions.
- Support better planning and accountability in mess administration.

## 3. Existing System

The existing system in many messes and dining facilities around the world still relies heavily on manual or semi-manual processes. These traditional methods often lead to several common problems:

- Meals are prepared based on estimated demand rather than actual attendance.
- Student attendance is not consistently tracked, making it difficult to estimate consumption.
- Excess food is often cooked and left unused due to poor planning and lack of records.
- Mess administrators have limited access to precise data for forecasting and waste analysis.
- There is no standardized way to compare prepared portions with actual consumption.
- Food shortages or overproduction may occur because records are not updated in real time.
- Manual tracking creates confusion, errors, and inconsistent meal planning.

These issues contribute to financial loss, poor resource utilization, and environmental harm. Food waste is not only a logistical problem but also a social and sustainability challenge across institutions and communities.

In this context, the project recognizes the need for a better management system that can help messes become more organized, transparent, and efficient.

## 4. Proposed System

The proposed system is a digital mess management solution developed to directly address the above issues. Instead of relying on guesswork and manual record keeping, the system uses a simple but effective database-driven workflow to monitor meals, attendance, and food usage.

Our project provides the following solutions:

- Secure login and role-based access for admin and student users.
- A centralized database for managing users, meals, and attendance records.
- Meal planning based on date, meal type, menu, and portion quantities.
- Attendance recording to capture whether a student consumed a given meal.
- Personal attendance history for students to review their participation.
- Administrative reporting to calculate portions prepared, consumed, and wasted.
- Recommendation logic that suggests suitable preparation quantities for future meals based on consumption trends.

This proposed solution helps mess administrators reduce waste by improving visibility into actual food consumption and making more informed preparation decisions. The system is designed as a practical and accessible tool that can be implemented in real mess environments to support sustainability, cost control, and operational efficiency.

## 5. SDLC (Tagged by File Name)

The following SDLC stages are represented in the project files:

| SDLC Phase | Description | Relevant File(s) |
|---|---|---|
| Requirements Analysis | Core needs identified: user login, meal management, attendance tracking, and reporting | `src/main.py`, `database/schema.sql` |
| System Design | Role-based flow and menu-driven navigation are defined | `src/main.py`, `src/auth.py` |
| Database Design | Schema for users, meals, and attendance is defined | `database/schema.sql` |
| Implementation | Functional modules for authentication, student management, meal management, attendance, and reports | `src/auth.py`, `src/students.py`, `src/meals.py`, `src/attendance.py`, `src/reports.py` |
| Integration | Database access is connected to the modules through a shared connection layer | `src/database.py` |
| Testing | No formal automated test suite is currently present in the repository | None identified |
| Deployment / Maintenance | The application is intended to run as a local Python-based CLI application using MySQL | `src/main.py`, `src/database.py` |

## 6. System Requirements

### Functional Requirements

- The system must allow users to log in with a username and password.
- The system must support at least two roles: admin and student.
- Admin users must be able to add and view students.
- Admin users must be able to add and view meals.
- Student users must be able to record attendance for meals offered by the mess.
- Student users must be able to view their attendance records.
- Admin users must be able to generate reports on meal consumption and corresponding waste.
- The system must prevent unauthorized access to restricted menu options based on user role.

### Non-Functional Requirements

- The application should be simple to operate through a terminal interface.
- Database access should be centralized to avoid repeated connection setup logic.
- Data should be stored persistently in MySQL.
- Reports should provide quick insight into portions prepared, portions consumed, and waste level.
- The system should handle invalid user inputs gracefully.

### Technical Requirements

- Python 3.x
- MySQL database server
- `mysql-connector-python` package
- `python-dotenv` package
- Environment variables for database configuration
- Command-line terminal environment

### Database Requirements

The database must provide the following data structure:

- `users(user_id, username, password, role)`
- `meals(meal_id, meal_date, meal_type, menu, amnt)`
- `attendance(user_id, meal_id, ate)`

### Operational Requirements

- The database server must be running before the application is used.
- User credentials must be created in the `users` table before login.
- Students should be added before attendance is tracked for them.
- Meal records should be created before attendance can be marked for those meals.

## Summary

Messwise is a compact but practical mess-management solution for tracking food consumption and reducing waste. The current system already provides a workable foundation in Python and MySQL, with clear role separation and operational modules for students, meals, attendance, and reporting. The proposed system continues this direction by emphasizing secure access, organized data handling, and data-driven meal planning to support better decisions in mess operations.
