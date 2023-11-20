import mysql.connector

# Function to establish a database connection
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password123",
        database="MusicDB"
    )

# Test function to check if the Artist table contains the expected data
def test_artist_table():
    connection = connect_to_db()
    cursor = connection.cursor()

    # Execute a query to select all rows from the Artist table
    cursor.execute("SELECT * FROM Artist")
    artists = cursor.fetchall()

    assert len(artists) == 4  # Ensure there are 4 artists in the table

    # Add more specific assertions based on the expected data in the Artist table

    cursor.close()
    connection.close()

# Similarly, create test functions to check Album, Song, and Review tables

def test_album_table():
    connection = connect_to_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Album")
    albums = cursor.fetchall()

    assert len(albums) == 4  # Ensure there are 4 albums in the table

    # Add more specific assertions based on the expected data in the Album table

    cursor.close()
    connection.close()

# Repeat similar test functions for Song and Review tables

def test_song_table():
    connection = connect_to_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Song")
    songs = cursor.fetchall()

    assert len(songs) == 4  # Ensure there are 4 songs in the table

    # Add more specific assertions based on the expected data in the Song table

    cursor.close()
    connection.close()

def test_review_table():
    connection = connect_to_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Review")
    reviews = cursor.fetchall()

    assert len(reviews) == 4  # Ensure there are 4 reviews in the table

    # Add more specific assertions based on the expected data in the Review table

    cursor.close()
    connection.close()
