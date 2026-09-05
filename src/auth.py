from database import get_connection

def login():
    print("\n" + "-" * 40)
    print("               LOGIN")
    print("-" * 40)

    username = input("Username: ")
    password = input("Password: ")

    connection = get_connection()

    if connection is None:
        print("Unable to connect to database.")
        return None

    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT user_id, username, role
        FROM users
        WHERE username = %s AND password = %s
    """

    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    cursor.close()
    connection.close()

    if user:
        return user

    print("\nInvalid username or password.")
    return None

