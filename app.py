from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)



# Endpoint for the front page
@app.route('/')
def front_page():
    # Retrieve trending songs and albums from the database (sample data)
    trending_songs = get_trending_songs()
    trending_albums = get_trending_albums()

    return render_template('frontpage.html', songs=trending_songs, albums=trending_albums)

# Route for the sign-in page
@app.route('/signin')
def signin():
    return render_template('SignIn.html')  # Replace with the actual content of your signin.html

# Route for the create account page
@app.route('/create_account')
def create_account():
    # Replace with your create_account.html content
    return render_template('CreateAccount.html')

# Function to retrieve trending songs from the database
def get_trending_songs():
    # Connect to the MySQL database
    mydb = mysql.connector.connect(
        host="mysql",
        user="root",
        password="password123",
        database="MusicDB"
    )
    cursor = mydb.cursor()

    # Execute a query to fetch trending songs (replace with your actual query)
    cursor.execute("SELECT title FROM Song LIMIT 4")  # Fetching 4 trending songs as an example
    trending_songs = [song[0] for song in cursor.fetchall()]

    cursor.close()
    mydb.close()

    return trending_songs

# Function to retrieve trending albums from the database
def get_trending_albums():
    # Connect to the MySQL database
    mydb = mysql.connector.connect(
        host="mysql",
        user="root",
        password="password123",
        database="MusicDB"
    )
    cursor = mydb.cursor()

    # Execute a query to fetch trending albums (replace with your actual query)
    cursor.execute("SELECT title FROM Album LIMIT 4")  # Fetching 4 trending albums as an example
    trending_albums = [album[0] for album in cursor.fetchall()]

    cursor.close()
    mydb.close()

    return trending_albums

# Endpoint for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Connect to the MySQL database
        mydb = connect_to_db()

        if mydb:
            cursor = mydb.cursor()

            # Check if user exists with provided email and password
            query = "SELECT * FROM User WHERE email = %s AND password = %s"
            user_data = (email, password)

            cursor.execute(query, user_data)
            user = cursor.fetchone()

            if user:
                # Successful login - Redirect to front_page or any other page
                return redirect(url_for('front_page'))
            else:
                # Incorrect username or password - Display an error message
                return "Incorrect username or password"

            cursor.close()
            mydb.close()

    return render_template('SignIn.html')  # Render the sign-in page

# Endpoint for search
@app.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':
        query = request.args.get('query')

        if query:
            # Connect to the MySQL database
            mydb = connect_to_db()

            if mydb:
                cursor = mydb.cursor()

                # Execute queries to search for songs, albums, and artists based on the input query
                song_query = "SELECT title, 'Song' as category FROM Song WHERE title LIKE %s"
                album_query = "SELECT title, 'Album' as category FROM Album WHERE title LIKE %s"
                artist_query = "SELECT name, 'Artist' as category FROM Artist WHERE name LIKE %s"
                param = ('%' + query + '%',)

                cursor.execute(song_query, param)
                song_results = cursor.fetchall()

                cursor.execute(album_query, param)
                album_results = cursor.fetchall()

                cursor.execute(artist_query, param)
                artist_results = cursor.fetchall()

                # Combine results from all queries
                search_results = song_results + album_results + artist_results

                cursor.close()
                mydb.close()

                return render_template('FilterPage.html', query=query, results=search_results)
            else:
                return "Unable to connect to the database."
        else:
            return "No search query provided."
 
# Function to establish MySQL connection
def connect_to_db():
    try:
        mydb = mysql.connector.connect(
            host="mysql",
            user="root",
            password="password123",
            database="MusicDB"
        )
        return mydb
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None
    
@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Extract form data
        first_name = request.form['first-name']
        email = request.form['email']
        password = request.form['password']
        # Add more fields as needed

        # Connect to MySQL
        mydb = connect_to_db()

        if mydb:
            print("Connected to the MySQL server!")
            mycursor = mydb.cursor()

            # Insert user details into a 'User' table (assuming it exists)
            insert_query = "INSERT INTO User (first_name, email, password) VALUES (%s, %s, %s)"
            user_data = (first_name, email, password)

            try:
                mycursor.execute(insert_query, user_data)
                mydb.commit()
                print("User data inserted successfully!")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
            
            mycursor.close()
            mydb.close()

    return "Form submitted successfully!"


@app.route('/album/<int:album_id>')
def show_album(album_id):

    mydb = mysql.connector.connect(
        host="mysql",
        user="root",
        password="password123", 
        database="MusicDB",
        raise_on_warnings=True
    )

    cursor = mydb.cursor(dictionary=True)
    album_query = '''
        SELECT Album.Title AS album_title, Album.ReleaseYear AS release_year,
               Artist.Name AS artist_name
        FROM Album
        JOIN Artist ON Album.ArtistID = Artist.ArtistID
        WHERE Album.AlbumID = %s
    '''
    cursor.execute(album_query, (album_id,))
    album_info = cursor.fetchone()

    # Fetch reviews for the album
    review_query = '''
        SELECT Review.Rating AS rating, Review.Comments AS comments
        FROM Review
        WHERE Review.AlbumID = %s
    '''
    cursor.execute(review_query, (album_id,))
    reviews = cursor.fetchall()

    # Fetch songs for the album
    song_query = '''
        SELECT Song.Title AS song_title
        FROM Song
        WHERE Song.AlbumID = %s
    '''
    cursor.execute(song_query, (album_id,))
    songs = [song['song_title'] for song in cursor.fetchall()]

    cursor.close()

    if album_info:
        return render_template('Album.html', album=album_info, reviews=reviews, songs=songs)
    else:
        return "Album not found"

if __name__ == '__main__':
    app.run(debug=True)
