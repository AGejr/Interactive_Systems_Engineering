from app import app, get_trending_songs, get_trending_albums
from bs4 import BeautifulSoup  # Import BeautifulSoup for HTML parsing
from flask import url_for

# Test the front_page endpoint
def test_front_page():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"ISDb" in response.data  # Ensure 'ISDb' logo is present
        assert b"Welcome" in response.data  # Check for the welcome text
        assert b"Trending songs" in response.data  # Check for trending songs text
        assert b"Trending albums" in response.data  # Check for trending albums text

        # Parse the HTML response using BeautifulSoup
        soup = BeautifulSoup(response.data, 'html.parser')

        # Count the number of elements representing trending songs
        trending_songs_elements = soup.find_all('div', class_='trending-container')[0].find_all('div', class_='trending-box')
        assert len(trending_songs_elements) == 4, f"Expected 4 trending songs, found {len(trending_songs_elements)}"

        # Count the number of elements representing trending albums
        trending_albums_elements = soup.find_all('div', class_='trending-container')[1].find_all('div', class_='trending-box')
        assert len(trending_albums_elements) == 4, f"Expected 4 trending albums, found {len(trending_albums_elements)}"

# Test the get_trending_songs function
def test_get_trending_songs():
    trending_songs = get_trending_songs()
    # Assuming get_trending_songs fetches 4 songs from the database
    assert len(trending_songs) == 4
    # Add more specific assertions based on the expected behavior of get_trending_songs

# Test the get_trending_albums function
def test_get_trending_albums():
    trending_albums = get_trending_albums()
    # Assuming get_trending_albums fetches 4 albums from the database
    assert len(trending_albums) == 4
    # Add more specific assertions based on the expected behavior of get_trending_albums

# Test the login endpoint
def test_login():
    with app.test_client() as client:
        response = client.get('/login')
        assert response.status_code == 200
        assert b"This is the login page" in response.data  # Replace this with expected login content

