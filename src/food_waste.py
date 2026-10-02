from database import get_connection


def record_food():

    connection = get_connection()
    if connection is None:
        return
    cursor = connection.cursor()

    query = "SELECT meal_id, meal_date, meal_type, menu FROM meals"
    cursor.execute(query)
    meals = cursor.fetchall()
    for meal in meals:
        print(f"Meal ID: {meal[0]}, Date: {meal[1]}, Type: {meal[2]}, Menu: {meal[3]}")

    meal_id = input("Enter meal ID: ")
    amnt = int(input("Enter food prepared: "))

    query = "INSERT INTO food_records(meal_id, food_prepared) VALUES (%s, %s)"
    cursor.execute(query, (meal_id, amnt))
    print("\nFood prepared amount recorded successfully!")
    connection.commit()

    cursor.close()
    connection.close()


def view_food_records():
    connection = get_connection()
    if connection is None:
        return

    cursor = connection.cursor()

    query = "SELECT meal_id, menu, food_prepared from meals NATURAL JOIN food_records"
    cursor.execute(query)
    records = cursor.fetchall()

    for record in records:
        query = "SELECT COUNT(user_id) FROM attendance WHERE meal_id = %s AND ate = TRUE"
        cursor.execute(query, (record[0],))
        count = cursor.fetchone()[0]
        print(f"Meal ID: {record[0]}, Menu: {record[1]}, Food Prepared: {record[2]}, Food Consumed: {count}, Food Wasted: {record[2] - count}")

    cursor.close()
    connection.close()

def food_waste_menu():
    while True:
        print("\n" + "=" * 40)
        print("          FOOD AND WASTE TRACKING")
        print("=" * 40)
        print("1. Record Food Prepared")
        print("2. View Food Consumption and Waste")
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