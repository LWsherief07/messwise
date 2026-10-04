from database import get_connection

def generate_report():
    food_consumption_values = [] #a list to store food consumption values for each meal to find the average consumption
    lowest_waste_dictionary = {} #a dictionary to store the meal with the lowest waste

    connection = get_connection()
    if connection is None:
        return
    
    cursor = connection.cursor()
    
    query = "SELECT meal_id, menu, amnt from meals"
    cursor.execute(query)
    records = cursor.fetchall()
    
    for record in records:
        # calculate avg consumption and lowest waste meal
        query = "SELECT COUNT(user_id) FROM attendance WHERE meal_id = %s AND ate = TRUE"
        cursor.execute(query, (record[0],))
        count = cursor.fetchone()[0]
        food_consumption_values.append(count)
        food_wasted = record[2] - count
        lowest_waste_dictionary[record[1]] = food_wasted

        # print meal details
        print(f'Meal ID: {record[0]}, Menu: {record[1]}, Portions Prepared: {record[2]}, Portions Consumed: {count}, Portions Wasted: {food_wasted}')


    print(f'Recommended preparation amount for next meal: {sum(food_consumption_values) // len(food_consumption_values)}')
    print(f'Lowest waste meal: {min(lowest_waste_dictionary, key=lowest_waste_dictionary.get)}')

    cursor.close()
    connection.close()


def reports_menu():
    while True:
        print("\n" + "=" * 40)
        print("       REPORTS AND STATISTICS")
        print("=" * 40)
        print("1. Generate Report")
        print("0. Back")
        print("=" * 40)

        choice = input("\nEnter your choice: ")

        if choice == "1":
            generate_report()
        elif choice == "0":
            break
        else:
            print("\nInvalid choice. Please try again.")