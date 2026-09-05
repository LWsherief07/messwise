from auth import login

def show_banner():
    print('=' * 40)
    print("              messwise")
    print("      food waste management system")
    print('=' * 40)

def show_main_menu(user):
    print('\n' + '-'*40)
    print('              main menu')
    print('-' * 40)
    print(f'logged in as: {user["username"]} ({user["role"]})')
    print('-' * 40)

    print("1. Student Management")
    print("2. Meal Management")
    print("3. Attendance")
    print("4. Food & Waste Tracking")
    print("5. Reports & Statistics")
    print("6. Preparation Recommendation")
    print("7. My Account")
    print("8. Logout")
    print("0. Exit")

    print('-' * 40)

def has_permission(user, allowed_roles):
    return user['role'] in allowed_roles

def run_app(user):
     while True:
        show_main_menu(user)

        choice = input("\nEnter your choice: ")

        if choice == "1":
            if has_permission(user, ["admin", "manager"]):
                from students import student_menu
                student_menu()
            else:
                print("\nUnauthorized access.")

        elif choice == "2":
            if has_permission(user, ["admin", "manager"]):
                from meals import meal_menu
                meal_menu()
            else:
                print("\nUnauthorized access.")

        elif choice == "3":
            if has_permission(user, ["admin", "student"]):
                from attendance import attendance_menu
                attendance_menu(user)
            else:
                print("\nUnauthorized access.")

        elif choice == "4":
            if has_permission(user, ["admin", "manager"]):
                from food_waste import food_waste_menu
                food_waste_menu()
            else:
                print("\nUnauthorized access.")

        elif choice == "0":
            print("\nthank you for using messwise. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")

def main():
    show_banner()

    user = login()

    if user is None:
        print("\nLogin failed. Exiting messwise.")
        return

    run_app(user)

if __name__ == '__main__':
    main()