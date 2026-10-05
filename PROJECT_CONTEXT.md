# Messwise Project Context

## 1. Introduction

Messwise is a food waste management system designed for a hostel or mess environment. The project is implemented as a Python command-line application with a MySQL database backend. It supports two user roles: admin and student. The system allows administrators to manage students and meals, while students can mark their attendance for meals and review their food consumption history.

The core purpose of the application is to help the mess administration track meal preparation, monitor student attendance, and generate useful statistics to reduce food wastage and improve planning decisions.

## 2. Objectives

The main objectives of the project are:

- Manage student records in a mess or hostel environment.
- Add and track meals by date and type (breakfast, lunch, dinner).
- Record student meal attendance and maintain historical participation data.
- Generate basic reports to analyze food consumption and identify meal waste.
- Provide role-based access control so that only authorized users can access certain functions.
- Support efficient decision-making for food preparation based on consumption patterns.

## 3. Existing System

The current project already contains a working CLI-based system with the following features:

- User authentication using username and password against the users table.
- Role-based menu access for admin and student users.
- Student management functions: add student and view student list.
- Meal management functions: add meal and view meals.
- Attendance management functions: record attendance and view personal attendance history.
- Reporting module: generate report with consumption, waste, and recommended preparation guidance.

The application architecture is organized into modular Python files:

- `src/main.py` — application entry point and navigation flow
- `src/auth.py` — login logic
- `src/database.py` — database connection logic
- `src/students.py` — student registration and listing
- `src/meals.py` — meal creation and viewing
- `src/attendance.py` — attendance recording and display
- `src/reports.py` — report generation and statistics

The database schema is defined in `database/schema.sql` and includes:

- `users` table for login and roles
- `meals` table for meal records
- `attendance` table for user-meal attendance mapping

The current system uses a MySQL database with environment variables for configuration, including host, user, password, and database name.

## 4. Proposed System

The proposed system is a structured, role-based mess management platform that automates the core operations of meal tracking and student attendance. The solution builds on the current CLI model and expands it into a more formal digital system for day-to-day mess operations.

The proposed system should include:

- Secure login and authorization for admins and students.
- Centralized database storage for users, meals, and attendance.
- Meal planning based on date, meal type, menu, and portion quantities.
- Attendance marking for each student against each meal served.
- Attendance history review for individual students.
- Administrative reporting for consumption trends and waste measurement.
- Recommendation logic to estimate future preparation quantities by comparing meal demand and actual attendance.

The system is intended to reduce manual record-keeping and provide a simple but effective decision support layer for mess operations. It is especially useful in environments where meal preparation decisions need to be based on real attendance and consumption records.

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
