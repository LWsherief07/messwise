from database import get_connection


def daily_report():
    report_date = input("Enter date (YYYY-MM-DD): ")

    connection = get_connection()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            SELECT
                m.meal_id,
                m.meal_type,
                m.menu,
                f.food_prepared,
                f.food_consumed,
                f.food_wasted,
                (f.food_wasted / NULLIF(f.food_prepared, 0)) * 100
            FROM food_records f
            JOIN meals m ON f.meal_id = m.meal_id
            WHERE m.meal_date = %s
            ORDER BY m.meal_type
            """,
            (report_date,)
        )

        records = cursor.fetchall()
        print_report(records, f"DAILY REPORT - {report_date}")

    finally:
        cursor.close()
        connection.close()


def monthly_statistics():
    month = input("Enter month (YYYY-MM): ")

    connection = get_connection()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            SELECT
                COUNT(f.record_id),
                COALESCE(SUM(f.food_prepared), 0),
                COALESCE(SUM(f.food_consumed), 0),
                COALESCE(SUM(f.food_wasted), 0),
                (
                    COALESCE(SUM(f.food_wasted), 0) /
                    NULLIF(COALESCE(SUM(f.food_prepared), 0), 0)
                ) * 100
            FROM food_records f
            JOIN meals m ON f.meal_id = m.meal_id
            WHERE DATE_FORMAT(m.meal_date, '%Y-%m') = %s
            """,
            (month,)
        )

        statistics = cursor.fetchone()

        print("\n" + "=" * 60)
        print(f"MONTHLY STATISTICS - {month}")
        print("=" * 60)
        print(f"Food records: {statistics[0]}")
        print(f"Total prepared: {statistics[1]}")
        print(f"Total consumed: {statistics[2]}")
        print(f"Total wasted: {statistics[3]}")
        print(f"Waste percentage: {statistics[4] or 0:.2f}%")

    finally:
        cursor.close()
        connection.close()


def waste_extremes():
    connection = get_connection()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            SELECT
                m.meal_id,
                m.meal_date,
                m.meal_type,
                m.menu,
                f.food_wasted / NULLIF(f.food_prepared, 0) * 100
            FROM food_records f
            JOIN meals m ON f.meal_id = m.meal_id
            ORDER BY f.food_wasted / NULLIF(f.food_prepared, 0) DESC
            LIMIT 1
            """
        )
        highest = cursor.fetchone()

        cursor.execute(
            """
            SELECT
                m.meal_id,
                m.meal_date,
                m.meal_type,
                m.menu,
                f.food_wasted / NULLIF(f.food_prepared, 0) * 100
            FROM food_records f
            JOIN meals m ON f.meal_id = m.meal_id
            ORDER BY f.food_wasted / NULLIF(f.food_prepared, 0)
            LIMIT 1
            """
        )
        lowest = cursor.fetchone()

        print_extreme("HIGHEST WASTE MEAL", highest)
        print_extreme("LOWEST WASTE MEAL", lowest)

    finally:
        cursor.close()
        connection.close()


def print_report(records, title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)

    if not records:
        print("No records found.")
        return

    for record in records:
        print(
            f"Meal ID: {record[0]} | "
            f"Type: {record[1].title()} | "
            f"Menu: {record[2]}"
        )
        print(
            f"Prepared: {record[3]} | "
            f"Consumed: {record[4]} | "
            f"Wasted: {record[5]} | "
            f"Waste: {record[6] or 0:.2f}%"
        )


def print_extreme(title, record):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    if record is None:
        print("No records found.")
        return

    print(
        f"Meal ID: {record[0]} | "
        f"Date: {record[1]} | "
        f"Type: {record[2].title()} | "
        f"Menu: {record[3]} | "
        f"Waste: {record[4] or 0:.2f}%"
    )


def reports_menu():
    while True:
        print("\n" + "=" * 40)
        print("       REPORTS AND STATISTICS")
        print("=" * 40)
        print("1. Daily Report")
        print("2. Monthly Statistics")
        print("3. Highest/Lowest Waste Meals")
        print("0. Back")
        print("=" * 40)

        choice = input("\nEnter your choice: ")

        if choice == "1":
            daily_report()
        elif choice == "2":
            monthly_statistics()
        elif choice == "3":
            waste_extremes()
        elif choice == "0":
            break
        else:
            print("\nInvalid choice. Please try again.")