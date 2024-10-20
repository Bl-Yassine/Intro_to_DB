import mysql.connector
from mysql.connector import Error

try :
    mydb = mysql.connector.connect(
        host ="localhost",
        user="Bl-Yassine",
        password="Alx@SQL123",
        database="alx_book_store"
    )

    cursor = mydb.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    cursor.execute("USE alx_book_store")

    cursor.close()
    mydb.close()

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")