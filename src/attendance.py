from database import get_connection

def record_attendance(user):
    user_id = user["user_id"]
    
    connection = get_connection()
    if connection is None:
        return

    cursor = connection.cursor()

    query = "SELECT meal_id, meal_date, meal_type, menu FROM meals NATURAL JOIN attendance WHERE user_id = %s AND ate = FALSE ORDER BY meal_date DESC"
    cursor.execute(query, (user_id,))
    meal = cursor.fetchone()

    if meal is None:
        print("\nNo available meal for attendance.")
        cursor.close()
        connection.close()
        return

    else:
        print(f'Available meal for attendance: {meal}')
        decision = input("Do you want to mark attendance for this meal? (yes/no): ").strip().lower()

        if decision != 'yes':
            print("\nAttendance not recorded.")
            cursor.close()
            connection.close()
            return
        
        else:
            query = "UPDATE attendance SET ate = TRUE WHERE user_id = %s AND meal_id = %s"
            cursor.execute(query, (user_id, meal[0]))
            connection.commit()
            print("\nAttendance recorded successfully!")
    
    cursor.close()
    connection.close()


def view_attendance(user):
    user_id = user["user_id"]
    connection = get_connection()
    if connection is None:
        return

    cursor = connection.cursor()

    query = "SELECT meal_date, meal_type, menu, ate FROM meals NATURAL JOIN attendance WHERE user_id = %s ORDER BY meal_date DESC"
    cursor.execute(query, (user_id,))
    records = cursor.fetchall()

    for record in records:
        print(f"Date: {record[0]}, Type: {record[1]}, Menu: {record[2]}, Ate: {record[3]}")

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
            view_attendance(user)
        elif choice == "0":
            break
        else:
            print("\nInvalid choice. Please try again.")