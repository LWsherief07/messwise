from database import get_connection

def add_meal():
    meal_date = input("Enter meal date (YYYY-MM-DD): ")
    meal_type = input("Enter meal type (breakfast/lunch/dinner): ").lower()
    menu = input("Enter menu: ")

    if meal_type not in ["breakfast", "lunch", "dinner"]:
        print("\nInvalid meal type.")
        return

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    query = """
        INSERT INTO meals (meal_date, meal_type, menu)
        VALUES (%s, %s, %s)
    """

    cursor.execute(query, (meal_date, meal_type, menu))
    connection.commit()

    print("\nMeal added successfully!")

    cursor.close()
    connection.close()


def view_meals():
    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    query = """
        SELECT meal_id, meal_date, meal_type, menu
        FROM meals
        ORDER BY meal_date DESC, meal_id DESC
    """

    cursor.execute(query)
    meals = cursor.fetchall()

    print("\n" + "=" * 60)
    print("                    MEALS")
    print("=" * 60)

    if not meals:
        print("No meals found.")
    else:
        for meal in meals:
            print(
                f"ID: {meal[0]} | "
                f"Date: {meal[1]} | "
                f"Type: {meal[2].title()} | "
                f"Menu: {meal[3]}"
            )

    cursor.close()
    connection.close()


def update_meal():
    meal_id = input("Enter meal ID to update: ")
    menu = input("Enter new menu: ")

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    query = """
        UPDATE meals
        SET menu = %s
        WHERE meal_id = %s
    """

    cursor.execute(query, (menu, meal_id))
    connection.commit()

    if cursor.rowcount == 0:
        print("\nMeal not found.")
    else:
        print("\nMeal updated successfully!")

    cursor.close()
    connection.close()


def meal_menu():
    while True:
        print("\n" + "=" * 40)
        print("          MEAL MANAGEMENT")
        print("=" * 40)
        print("1. Add Meal")
        print("2. View Meals")
        print("3. Update Meal")
        print("0. Back")
        print("=" * 40)

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_meal()

        elif choice == "2":
            view_meals()

        elif choice == "3":
            update_meal()

        elif choice == "0":
            break

        else:
            print("\nInvalid choice. Please try again.")