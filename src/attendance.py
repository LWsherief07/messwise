from database import get_connection

def record_attendance(user):
    student_id = user["user_id"]
    meal_id = input("Enter meal ID: ")

    connection = get_connection()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        # appropriate meal
        cursor.execute(
            "SELECT meal_id FROM meals WHERE meal_id = %s",
            (meal_id,)
        )

        if cursor.fetchone() is None:
            print("\nMeal not found.")
            return

        # no duplicates
        cursor.execute(
            """
            SELECT attendance_id
            FROM attendance
            WHERE student_id = %s AND meal_id = %s
            """,
            (student_id, meal_id)
        )

        if cursor.fetchone():
            print("\nAttendance already recorded.")
            return


        cursor.execute(
            """
            INSERT INTO attendance (student_id, meal_id, ate)
            VALUES (%s, %s, TRUE)
            """,
            (student_id, meal_id)
        )

        connection.commit()
        print("\nAttendance recorded successfully!")

    except Exception as error:
        connection.rollback()
        print(f"\nFailed to record attendance: {error}")

    finally:
        cursor.close()
        connection.close()


def view_attendance():
    connection = get_connection()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            SELECT
                a.attendance_id,
                s.name,
                m.meal_date,
                m.meal_type
            FROM attendance a
            JOIN students s ON a.student_id = s.student_id
            JOIN meals m ON a.meal_id = m.meal_id
            ORDER BY m.meal_date DESC, a.attendance_id DESC
            """
        )

        records = cursor.fetchall()

        print("\n" + "=" * 65)
        print("                     ATTENDANCE")
        print("=" * 65)

        if not records:
            print("No attendance records found.")
        else:
            for record in records:
                print(
                    f"ID: {record[0]} | "
                    f"Student: {record[1]} | "
                    f"Date: {record[2]} | "
                    f"Meal: {record[3].title()}"
                )

    finally:
        cursor.close()
        connection.close()


def attendance_menu(user):
    while True:
        print("\n" + "=" * 40)
        print("             ATTENDANCE")
        print("=" * 40)
        print("1. Record Attendance")
        print("2. View Attendance")
        print("0. Back")
        print("=" * 40)

        choice = input("\nEnter your choice: ")

        if choice == "1":
            record_attendance(user)
        elif choice == "2":
            view_attendance()
        elif choice == "0":
            break
        else:
            print("\nInvalid choice. Please try again.")