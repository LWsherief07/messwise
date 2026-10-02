from database import get_connection

def add_student():
    id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    password = name.lower().replace(" ", "") + "12345" #default password 

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute(
                    """
                    INSERT INTO users (user_id, username, password, role)
                    VALUES (%s, %s, %s, 'student')
                    """,
                    (id, name, password)
                )

        connection.commit()

        print("\nStudent added successfully!")

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

    query = "SELECT user_id, username FROM users WHERE role = 'student'"

    cursor.execute(query)
    students = cursor.fetchall()

    print("\n" + "=" * 50)
    print("                 STUDENTS")
    print("=" * 50)

    if not students:
        print("No students found.")
    else:
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}")

    cursor.close()
    connection.close()

def student_menu():
    while True:
        print("\n" + "=" * 40)
        print("        STUDENT MANAGEMENT")
        print("=" * 40)
        print("1. Add Student")
        print("2. View Students")
        print("0. Back")
        print("=" * 40)

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "0":
            break

        else:
            print("\nInvalid choice. Please try again.")