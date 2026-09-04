from database import get_connection

def show_banner():
    print('=' * 40)
    print('messwise')
    print('food waste management system')
    print('=' * 40)

def show_menu():
    print('\nmain menu')
    print('-' * 40)
    print('1. feature 1')
    print('2. feature 2')
    print('0. exit')
    
def main():
    show_banner()
    connection = get_connection()

    if connection:
        print('Database connection successful. Check main menu now.')
    else:
        print('Failed to connect to MySQL database')
        return

    while True:
        show_menu()
        choice = input('Enter your choice: ')

        if choice == '1':
            print('Feature 1 selected')
        elif choice == '2':
            print('Feature 2 selected')
        elif choice == '0':
            print('thank you for using messwise.')
            break
        else:
            print('Invalid choice. Please try again!')

    connection.close()

if __name__ == '__main__':
    main()