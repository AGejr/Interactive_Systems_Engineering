from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)



# Endpoint for the front page
@app.route('/')
def front_page():
    # Retrieve trending songs and albums from the database (sample data)
    trending_songs = get_trending_songs()
    trending_albums = get_trending_albums()

    return render_template('frontpage.html', songs=trending_songs, albums=trending_albums)

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
@app.route('/login')
def login():
    return "This is the login page"  # Replace this with your login logic or template

# Endpoint for search
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        query = request.args.get('query')
        # Perform search logic here based on the 'query' parameter
        return f"Search results for: {query}"  # Replace this with your search logic


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
