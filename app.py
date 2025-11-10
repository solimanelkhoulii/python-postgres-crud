import psycopg2
from psycopg2 import Error
from datetime import date

# The database must be running and accessible.
DB_CONFIG = {
    "host": "localhost",
    "database": "assignment_db", 
    "user": "postgres",         
    "password": "#",
    "port": "5432"
}

def get_db_connection():
    """Establishes a connection to the PostgreSQL database."""
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Error connecting to PostgreSQL database: {e}")
        return None

def getAllStudents():
    """Retrieves and displays all records from the students table."""
    conn = get_db_connection()
    if conn is None:
        return

    try:
        with conn.cursor() as cursor:
            # SQL query to select all students
            cursor.execute("SELECT student_id, first_name, last_name, email, enrollment_date FROM students ORDER BY student_id;")
            records = cursor.fetchall()

            if not records:
                print("The students table is empty.")
                return

            print("\n--- All Students Records ---")
            # Print header
            print(f"{'ID':<4} {'First Name':<15} {'Last Name':<15} {'Email':<30} {'Enrollment Date':<15}")
            print("-" * 80)
            # Print records
            for row in records:
                student_id, first_name, last_name, email, enrollment_date = row
                print(f"{student_id:<4} {first_name:<15} {last_name:<15} {email:<30} {str(enrollment_date):<15}")

    except Error as e:
        print(f"Error retrieving students: {e}")
    finally:
        if conn:
            conn.close()

def addStudent(first_name: str, last_name: str, email: str, enrollment_date: date):
    """Inserts a new student record into the students table."""
    conn = get_db_connection()
    if conn is None:
        return

    try:
        with conn.cursor() as cursor:
            # SQL query to insert a new student record
            sql = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s) RETURNING student_id;"
            cursor.execute(sql, (first_name, last_name, email, enrollment_date))
            new_id = cursor.fetchone()[0]
            conn.commit()
            print(f"\nSuccessfully added new student: {first_name} {last_name} with ID {new_id}.")
            return new_id
    except Error as e:
        print(f"\nError adding student {first_name} {last_name}: {e}")
        conn.rollback()
    finally:
        if conn:
            conn.close()

def updateStudentEmail(student_id: int, new_email: str):
    """Updates the email address for a student with the specified student_id."""
    conn = get_db_connection()
    if conn is None:
        return

    try:
        with conn.cursor() as cursor:
            # SQL query to update the student's email
            sql = "UPDATE students SET email = %s WHERE student_id = %s;"
            cursor.execute(sql, (new_email, student_id))
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\nSuccessfully updated email for student ID {student_id} to {new_email}.")
            else:
                print(f"\nNo student found with ID {student_id}. Email update failed.")
    except Error as e:
        print(f"\nError updating email for student ID {student_id}: {e}")
        conn.rollback()
    finally:
        if conn:
            conn.close()

def deleteStudent(student_id: int):
    """Deletes the record of the student with the specified student_id."""
    conn = get_db_connection()
    if conn is None:
        return

    try:
        with conn.cursor() as cursor:
            # SQL query to delete the student record
            sql = "DELETE FROM students WHERE student_id = %s;"
            cursor.execute(sql, (student_id,))
            conn.commit()
            if cursor.rowcount > 0:
                print(f"\nSuccessfully deleted student with ID {student_id}.")
            else:
                print(f"\nNo student found with ID {student_id}. Deletion failed.")
    except Error as e:
        print(f"\nError deleting student with ID {student_id}: {e}")
        conn.rollback()
    finally:
        if conn:
            conn.close()

def run_demonstration():
    """Demonstrates the functionality of all application functions."""
    print("--- Starting Application Demonstration ---")

    # 1. Initial state (assuming database setup script has been run)
    print("\n--- 1. Initial State: getAllStudents() ---")
    getAllStudents()

    # 2. Add a new student
    print("\n--- 2. CRUD: addStudent() ---")
    new_student_id = addStudent("Alice", "Johnson", "alice.johnson@example.com", date(2023, 10, 15))

    # 3. Verify addition
    print("\n--- 3. State after Addition: getAllStudents() ---")
    getAllStudents()

    # 4. Update the new student's email
    if new_student_id:
        print("\n--- 4. CRUD: updateStudentEmail() ---")
        updateStudentEmail(new_student_id, "alice.j@newdomain.com")

    # 5. Verify update
    print("\n--- 5. State after Update: getAllStudents() ---")
    getAllStudents()

    # 6. Delete the new student
    if new_student_id:
        print("\n--- 6. CRUD: deleteStudent() ---")
        deleteStudent(new_student_id)

    # 7. Verify deletion
    print("\n--- 7. Final State: getAllStudents() ---")
    getAllStudents()

    print("\n--- Application Demonstration Complete ---")


if __name__ == "__main__":

    run_demonstration()
    print("\nPython application file created: app.py")

