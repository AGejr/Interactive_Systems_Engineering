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
    
# Function to establish MySQL connection
def connect_to_db():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
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


if __name__ == '__main__':
    app.run(debug=True)
