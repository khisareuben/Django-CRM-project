import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mei chan su mysql"
    )

    if mydb.is_connected():
        print("Successfully connected to the database")

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE crm")
    print("Database 'crm' created successfully")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("MySQL connection is closed")
