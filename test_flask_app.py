import requests
import pytest

# Assuming a Flask web application running locally for testing purposes


# Scenario 1: As a music enthusiast, I want to search for an artist.
def test_search_artist():
    url = 'http://localhost:5000/'  # Replace with your app's URL
    search_query = 'Queen'  # Replace with an artist in your database

    response = requests.get(url + f'/search?query={search_query}')

    assert response.status_code == 200
    assert search_query in response.text


# Scenario 2: As a music enthusiast, I want to search for an album.
def test_search_album():
    url = 'http://localhost:5000/'  # Replace with your app's URL
    album_query = 'The Dark Side of the Moon'  # Replace with an album in your database

    response = requests.get(url + f'/search?query={album_query}')

    assert response.status_code == 200
    assert album_query in response.text


# Scenario 3: As a music enthusiast, I want to search for a song.
def test_search_song():
    url = 'http://localhost:5000/'  # Replace with your app's URL
    song_query = 'Bohemian Rhapsody'  # Replace with a song in your database

    response = requests.get(url + f'/search?query={song_query}')

    assert response.status_code == 200
    assert song_query in response.text


# Scenario 4: As a music critic, I want to view reviews of a song or album.
def test_view_reviews():
    url = 'http://localhost:5000/'  # Replace with your app's URL
    item_id = '1234'  # Replace with an existing song or album ID in your database

    response = requests.get(url + f'/reviews?id={item_id}')

    assert response.status_code == 200
    assert 'reviews' in response.text


# Scenario 5: As a music enthusiast, I want to view details of an artist.
def test_view_artist_details():
    url = 'http://localhost:5000/'  # Replace with your app's URL
    artist_id = '5678'  # Replace with an existing artist ID in your database

    response = requests.get(url + f'/artist?id={artist_id}')

    assert response.status_code == 200
    assert 'artist details' in response.text


# Scenario 6: As a music enthusiast, I want to view the songs I've listened to.
def test_view_listened_songs():
    url = 'http://localhost:5000/'  # Replace with your app's URL
    user_id = 'user_123'  # Replace with an existing user ID in your database

    response = requests.get(url + f'/listened?id={user_id}')

    assert response.status_code == 200
    assert 'listened songs' in response.text


# Scenario 7: As a user, I want to create a review for a song or album.
def test_create_review():
    url = 'http://localhost:5000/'  # Replace with your app's URL
    user_id = 'user_123'  # Replace with an existing user ID in your database
    item_id = '1234'  # Replace with an existing song or album ID in your database

    review_data = {
        'user_id': user_id,
        'item_id': item_id,
        'rating': 5,
        'comment': 'Awesome song/album!'
    }

    response = requests.post(url + '/create_review', json=review_data)

    assert response.status_code == 201  # Assuming 201 for successful creation
    assert 'Review created' in response.text


# Scenario 8: As a user, I want to rate a song.
def test_rate_song():
    url = 'http://localhost:5000/'  # Replace with your app's URL
    user_id = 'user_123'  # Replace with an existing user ID in your database
    song_id = '1234'  # Replace with an existing song ID in your database

    rating_data = {
        'user_id': user_id,
        'song_id': song_id,
        'rating': 4
    }

    response = requests.post(url + '/rate_song', json=rating_data)

    assert response.status_code == 200  # Assuming 200 for successful rating
    assert 'Song rated' in response.text


if __name__ == "__main__":
    pytest.main(['-s', __file__])

