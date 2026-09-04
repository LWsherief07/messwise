import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv('host')
db_user = os.getenv('user')
db_password = os.getenv('password')
db_database = os.getenv('database')

def get_connection():
    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database)
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None