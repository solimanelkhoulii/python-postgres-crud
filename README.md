# Built a Python application with full CRUD functionality connected to a PostgreSQL database, including dynamic query execution, data validation, and a CLI interface.


**Name:** Soliman E.

## Demonstration Video

A complete video demonstration of the database setup and application functionality is available here: [Application Demonstration Video](https://www.youtube.com/watch?v=iT_ehXae6KI)

## Table of Contents

1. [Prerequisites](#prerequisites)

1. [Setup Instructions](#setup-instructions)

1. [Database Setup](#database-setup)

1. [Application Configuration](#application-configuration)

1. [How to Run the Application](#how-to-run-the-application)

1. [Application Functions](#application-functions)

## 1. Prerequisites

To run this application, you will need:

- **PostgreSQL Server:** A running instance of a PostgreSQL database server.

- **Python 3:** The Python interpreter installed on your system.

- **`psycopg2`**** library:** The PostgreSQL adapter for Python.

You can install the required Python library using `pip`:

```bash
python -m pip install psycopg2-binary
```

## 2. Setup Instructions

### Project Structure

The repository is structured as follows:

```
postgres_app/
├── app.py                  # The main Python application file
├── setup_database.sql      # SQL script for creating the table and initial data
└── README.md               # This file
```

## 3. Database Setup

The `setup_database.sql` file contains the necessary SQL commands to create the `students` table and populate it with the initial data.

**To set up the database:**

1. Ensure your PostgreSQL server is running.

1. Connect to your target database (e.g., using `psql` or pgAdmin).

1. Execute the commands in the `setup_database.sql` file.

## 4. Application Configuration

The Python application requires your database connection details.

Open `app.py` and modify the `DB_CONFIG` dictionary with your specific PostgreSQL credentials. **Note: The password field below is a placeholder for security.**

```python
DB_CONFIG = {
    "host": "localhost",
    "database": "assignment_db", # The database used for the demonstration
    "user": "postgres",         # The default PostgreSQL user
    "password": "YOUR_POSTGRES_PASSWORD_HERE", # REPLACE WITH YOUR ACTUAL PASSWORD TO RUN
    "port": "5432"
}
```

## 5. How to Run the Application

The `app.py` file contains a `run_demonstration()` function that executes all required CRUD operations sequentially to demonstrate functionality.

1. Ensure you have completed the steps in [Database Setup](#database-setup) and [Application Configuration](#application-configuration).

1. Ensure the `run_demonstration()` call at the bottom of `app.py` is uncommented.

1. Run the Python script from your terminal:

## 6. Application Functions

The `app.py` file implements the following functions, each with comments explaining its purpose and functionality:

| Function Name | Description | Operation |
| --- | --- | --- |
| `get_db_connection()` | Helper function to establish a connection to the database. | Connection |
| `getAllStudents()` | Retrieves and displays all records from the `students` table. | **Read** |
| `addStudent(first_name, last_name, email, enrollment_date)` | Inserts a new student record into the table. | **Create** |
| `updateStudentEmail(student_id, new_email)` | Updates the email address for a specified student ID. | **Update** |
| `deleteStudent(student_id)` | Deletes the record of the student with the specified ID. | **Delete** |

### Code Quality and Documentation

The code adheres to good practices:

- **Modularity:** Database connection logic is separated into a helper function.

- **Error Handling:** `try...except...finally` blocks are used to manage database errors and ensure connections are closed.

- **Readability:** Functions, variables, and logic are clearly named and commented, fulfilling the documentation requirements of the assignment.

