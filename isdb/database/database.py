import mysql.connector

# Establish a connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password123",
    database="MusicDB"
)

# Check if the connection is successful
if mydb.is_connected():
    print("Connected to the MySQL server!")
    mycursor = mydb.cursor()

    # Check if the tables exist
    mycursor.execute("SHOW TABLES")
    tables = mycursor.fetchall()
    table_names = [table[0] for table in tables]

    # Read SQL statements from tables.sql
    with open("tables.sql", "r") as file:
        sql_statements = file.read().split(';')

    for statement in sql_statements:
        table_name = statement.split('(')[0].split()[-1]
        if table_name not in table_names and statement.strip():
            mycursor.execute(statement)

    print("Tables created successfully!")
    mydb.commit()
    mycursor.close()
    mydb.close()
else:
    print("Connection to MySQL failed.")
