import mysql.connector

# Establish a connection to MySQL (without specifying a database)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword"
)

# Check if the connection is successful
if mydb.is_connected():
    print("Connected to the MySQL server!")
else:
    print("Connection to MySQL failed.")

# Create a cursor object to execute SQL
mycursor = mydb.cursor()

# Create the database
try:
    mycursor.execute("CREATE DATABASE MusicDB")
    print("Database 'MusicDB' created successfully!")
except mysql.connector.Error as err:
    print(f"Error: {err}")