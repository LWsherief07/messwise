from database import get_connection


def record_food():
    meal_id = input("Enter meal ID: ")
    prepared = float(input("Enter food prepared: "))
    consumed = float(input("Enter food consumed: "))
    wasted = float(input("Enter food wasted: "))

    if prepared < 0 or consumed < 0 or wasted < 0:
        print("\nFood values cannot be negative.")
        return

    if consumed + wasted > prepared:
        print("\nConsumed plus wasted cannot exceed prepared food.")
        return

    connection = get_connection()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute(
            "SELECT meal_id FROM meals WHERE meal_id = %s",
            (meal_id,)
        )

        if cursor.fetchone() is None:
            print("\nMeal not found.")
            return

        cursor.execute(
            "SELECT record_id FROM food_records WHERE meal_id = %s",
            (meal_id,)
        )

        if cursor.fetchone():
            print("\nFood record already exists for this meal.")
            return

        cursor.execute(
            """
            INSERT INTO food_records
                (meal_id, food_prepared, food_consumed, food_wasted)
            VALUES (%s, %s, %s, %s)
            """,
            (meal_id, prepared, consumed, wasted)
        )

        connection.commit()
        print("\nFood record saved successfully.")

    except Exception as error:
        connection.rollback()
        print(f"\nFailed to save food record: {error}")

    finally:
        cursor.close()
        connection.close()


def view_food_records():
    connection = get_connection()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            SELECT
                f.record_id,
                f.meal_id,
                m.meal_date,
                m.meal_type,
                m.menu,
                f.food_prepared,
                f.food_consumed,
                f.food_wasted,
                CASE
                    WHEN f.food_prepared = 0 THEN 0
                    ELSE (f.food_wasted / f.food_prepared) * 100
                END AS waste_percentage
            FROM food_records f
            JOIN meals m ON f.meal_id = m.meal_id
            ORDER BY m.meal_date DESC, f.record_id DESC
            """
        )

        records = cursor.fetchall()

        print("\n" + "=" * 100)
        print("                         FOOD AND WASTE RECORDS")
        print("=" * 100)

        if not records:
            print("No food records found.")
        else:
            for record in records:
                print(
                    f"Record ID: {record[0]} | "
                    f"Meal ID: {record[1]} | "
                    f"Date: {record[2]} | "
                    f"Type: {record[3].title()} | "
                    f"Menu: {record[4]}"
                )
                print(
                    f"Prepared: {record[5]} | "
                    f"Consumed: {record[6]} | "
                    f"Wasted: {record[7]} | "
                    f"Waste: {record[8]:.2f}%"
                )

    finally:
        cursor.close()
        connection.close()


def food_waste_menu():
    while True:
        print("\n" + "=" * 40)
        print("          FOOD AND WASTE TRACKING")
        print("=" * 40)
        print("1. Record Food")
        print("2. View Food Records")
        print("0. Back")
        print("=" * 40)

        choice = input("\nEnter your choice: ")

        if choice == "1":
            record_food()
        elif choice == "2":
            view_food_records()
        elif choice == "0":
            break
        else:
            print("\nInvalid choice. Please try again.")