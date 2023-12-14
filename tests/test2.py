import pytest
from your_app import create_app, db  # Replace 'your_app' with your Flask app module
from your_models import Artist, Album, Song, Review, User  # Import your SQLAlchemy models

# Fixture to create a test app context and provide a test client
@pytest.fixture
def client():
    app = create_app()  # Replace with the method that creates your Flask app
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use an in-memory SQLite DB for testing
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create tables in the test database
            yield client

# Fixture to populate the test database with sample data
@pytest.fixture
def populate_db(client):
    # Insert sample data into the database
    queen = Artist(Name='Queen', Genre='Rock', Description='Legendary British rock band')
    michael_jackson = Artist(Name='Michael Jackson', Genre='Pop', Description='King of Pop')
    the_beatles = Artist(Name='The Beatles', Genre='Rock', Description='Influential rock band')
    madonna = Artist(Name='Madonna', Genre='Pop', Description='Queen of Pop')
    db.session.add_all([queen, michael_jackson, the_beatles, madonna])
    db.session.commit()

    night_at_the_opera = Album(Title='A Night at the Opera', ReleaseYear=1975, ArtistID=1)
    thriller = Album(Title='Thriller', ReleaseYear=1982, ArtistID=2)
    abbey_road = Album(Title='Abbey Road', ReleaseYear=1969, ArtistID=3)
    like_a_prayer = Album(Title='Like a Prayer', ReleaseYear=1989, ArtistID=4)
    db.session.add_all([night_at_the_opera, thriller, abbey_road, like_a_prayer])
    db.session.commit()

    bohemian_rhapsody = Song(Title='Bohemian Rhapsody', AlbumID=1, Duration='5:55', ArtistID=1)
    billie_jean = Song(Title='Billie Jean', AlbumID=2, Duration='4:54', ArtistID=2)
    come_together = Song(Title='Come Together', AlbumID=3, Duration='4:20', ArtistID=3)
    like_a_prayer_song = Song(Title='Like a Prayer', AlbumID=4, Duration='5:41', ArtistID=4)
    db.session.add_all([bohemian_rhapsody, billie_jean, come_together, like_a_prayer_song])
    db.session.commit()

    review_1 = Review(SongID=1, AlbumID=1, ReviewerID=101, Rating=5, Comments='One of the greatest albums ever!')
    review_2 = Review(SongID=2, AlbumID=2, ReviewerID=102, Rating=4, Comments='Classic track by MJ')
    review_3 = Review(SongID=3, AlbumID=3, ReviewerID=103, Rating=5, Comments='Timeless Beatles hit')
    review_4 = Review(SongID=4, AlbumID=4, ReviewerID=104, Rating=4, Comments='Madonna at her best')
    review_5 = Review(SongID=1, AlbumID=1, ReviewerID=104, Rating=4, Comments='Queen at their best')
    db.session.add_all([review_1, review_2, review_3, review_4, review_5])
    db.session.commit()

# Test scenarios using the provided data
def test_lookup_artist(client, populate_db):
    # GIVEN the user goes to the webpage
    response = client.get('/')
    assert response.status_code == 200

    # ... (rest of the test follows similar steps as shown in the previous example)

# Similarly, create tests for other scenarios using the populated database.
