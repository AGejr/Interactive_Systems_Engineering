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

    # Define SQL statements for table creation
    sql_statements = [
        """CREATE TABLE IF NOT EXISTS Artist (
            ArtistID INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(100),
            Genre VARCHAR(50),
            Description TEXT
        )""",
        """CREATE TABLE IF NOT EXISTS Album (
            AlbumID INT AUTO_INCREMENT PRIMARY KEY,
            Title VARCHAR(100),
            ReleaseYear INT,
            ArtistID INT,
            FOREIGN KEY (ArtistID) REFERENCES Artist(ArtistID)
        )""",
        """CREATE TABLE IF NOT EXISTS Song (
            SongID INT AUTO_INCREMENT PRIMARY KEY,
            Title VARCHAR(100),
            AlbumID INT,
            Duration TIME,
            ArtistID INT,
            FOREIGN KEY (AlbumID) REFERENCES Album(AlbumID),
            FOREIGN KEY (ArtistID) REFERENCES Artist(ArtistID)
        )""",
        """CREATE TABLE IF NOT EXISTS Review (
            ReviewID INT AUTO_INCREMENT PRIMARY KEY,
            SongID INT,
            AlbumID INT,
            ReviewerID INT,
            Rating INT,
            Comments TEXT,
            FOREIGN KEY (SongID) REFERENCES Song(SongID),
            FOREIGN KEY (AlbumID) REFERENCES Album(AlbumID)
        )"""
    ]

    # Check and create tables if they do not exist
    for statement in sql_statements:
        try:
            mycursor.execute(statement)
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    print("Tables checked/created successfully!")
    mydb.commit()
    mycursor.close()
    mydb.close()
else:
    print("Connection to MySQL failed.")
