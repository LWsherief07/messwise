from auth import login

def show_banner():
    print('=' * 40)
    print("              messwise")
    print("      food waste management system")
    print('=' * 40)

def show_menu(user):
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

def main():
    show_banner()

    user = login()

    if user is None:
        print("\nLogin failed. Exiting messwise.")
        return

    while True:
        show_menu(user)

        choice = input('\nEnter your choice: ')

        if choice == '1':
            print('\nFeature 1 selected')
        elif choice == '2':
            print('\nFeature 2 selected')
        elif choice == '0':
            print('\nthank you for using messwise.')
            break
        else:
            print('\nInvalid choice. Please try again!')

if __name__ == '__main__':
    main()