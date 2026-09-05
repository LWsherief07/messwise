from database import get_connection

def add_student():
    name = input("Enter student name: ")
    room_no = input("Enter room number: ")
    password = name.lower().replace(" ", "") + "12345"  #default password

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        #user table
        cursor.execute(
            """
            INSERT INTO users (username, password, role)
            VALUES (%s, %s, 'student')
            """,
            (name, password)
        )

        #user id
        student_id = cursor.lastrowid # returns the auto generated id of the last inserted row

        #student id = user id
        cursor.execute(
            """
            INSERT INTO students (student_id, name, room_no)
            VALUES (%s, %s, %s)
            """,
            (student_id, name, room_no)
        )

        connection.commit()

        print("\nStudent and user account created successfully!")
        print(f"Student ID: {student_id}")

    except Exception as error:
        connection.rollback()
        print(f"\nFailed to create student: {error}")

    finally:
        cursor.close()
        connection.close()

def view_students():
    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    query = "SELECT student_id, name, room_no FROM students"

    cursor.execute(query)
    students = cursor.fetchall()

    print("\n" + "=" * 50)
    print("                 STUDENTS")
    print("=" * 50)

    if not students:
        print("No students found.")
    else:
        for student in students:
            print(
                f"ID: {student[0]} | "
                f"Name: {student[1]} | "
                f"Room: {student[2]}"
            )

    cursor.close()
    connection.close()


def update_student():
    student_id = input("Enter student ID to update: ")
    name = input("Enter new name: ")
    room_no = input("Enter new room number: ")

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    query = """
        UPDATE students
        SET name = %s, room_no = %s
        WHERE student_id = %s
    """

    cursor.execute(query, (name, room_no, student_id))
    connection.commit()

    if cursor.rowcount == 0:
        print("\nStudent not found.")
    else:
        print("\nStudent updated successfully!")

    cursor.close()
    connection.close()

def student_menu():
    while True:
        print("\n" + "=" * 40)
        print("        STUDENT MANAGEMENT")
        print("=" * 40)
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("0. Back")
        print("=" * 40)

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            update_student()

        elif choice == "0":
            break

        else:
            print("\nInvalid choice. Please try again.")