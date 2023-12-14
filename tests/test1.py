import pytest
from flask import url_for

# Test Scenario: Looking up artists
def test_lookup_artist(client):
    # GIVEN the user goes to the webpage
    response = client.get('/')
    assert response.status_code == 200

    # AND finds the artist via search, album, or songlist
    # For the sake of demonstration, let's assume artist search by name "ArtistName"
    search_query = "ArtistName"
    search_response = client.get(f'/search?query={search_query}')
    assert search_response.status_code == 200

    # WHEN the user clicks on a specific artist
    artist_name = "ArtistName"  # Replace with the specific artist's name
    artist_url = url_for('show_artist', artist_name=artist_name)
    artist_response = client.get(artist_url)

    # THEN the artist is displayed
    assert artist_response.status_code == 200
    assert artist_name in artist_response.data.decode()

# Test Scenario: Looking up albums
def test_lookup_album(client):
    # GIVEN the user goes to the webpage
    response = client.get('/')
    assert response.status_code == 200

    # AND finds the album via search, artist, or albumlist
    # For the sake of demonstration, let's assume album search by title "AlbumTitle"
    search_query = "AlbumTitle"
    search_response = client.get(f'/search?query={search_query}')
    assert search_response.status_code == 200

    # WHEN the user clicks on a specific album
    album_id = 1  # Replace with the specific album ID
    album_url = url_for('show_album', album_id=album_id)
    album_response = client.get(album_url)

    # THEN the album is displayed
    assert album_response.status_code == 200
    assert "AlbumTitle" in album_response.data.decode()

# Test Scenario: Looking up songs
def test_lookup_song(client):
    # GIVEN the user goes to the webpage
    response = client.get('/')
    assert response.status_code == 200

    # AND finds the song via search, album, songlist, or artist
    # For the sake of demonstration, let's assume song search by title "SongTitle"
    search_query = "SongTitle"
    search_response = client.get(f'/search?query={search_query}')
    assert search_response.status_code == 200

    # WHEN the user clicks on a specific song
    song_id = 1  # Replace with the specific song ID
    song_url = url_for('show_song', song_id=song_id)
    song_response = client.get(song_url)

    # THEN the song is displayed
    assert song_response.status_code == 200
    assert "SongTitle" in song_response.data.decode()

# Test Scenario: Looking up reviews of songs and albums
def test_lookup_reviews(client):
    # GIVEN the user goes to the webpage
    response = client.get('/')
    assert response.status_code == 200

    # AND finds the song or album
    # For the sake of demonstration, let's assume review search by song ID
    song_id = 1
    review_response = client.get(f'/song/{song_id}/reviews')

    # THEN the song or album and the reviews for the song or album are displayed
    assert review_response.status_code == 200
    assert "Reviews" in review_response.data.decode()
    # Add assertions for verifying the presence of reviews data

# Test Scenario: Looking up an artist for an overview of their work
def test_artist_overview(client):
    # GIVEN the user goes to the webpage
    response = client.get('/')
    assert response.status_code == 200

    # AND finds the artist via search, album, or songlist
    # For the sake of demonstration, let's assume artist search by name "ArtistName"
    search_query = "ArtistName"
    search_response = client.get(f'/search?query={search_query}')
    assert search_response.status_code == 200

    # WHEN the user clicks on a specific artist
    artist_name = "ArtistName"  # Replace with the specific artist's name
    artist_url = url_for('show_artist', artist_name=artist_name)
    artist_response = client.get(artist_url)

    # THEN the artist is displayed
    assert artist_response.status_code == 200
    assert artist_name in artist_response.data.decode()

# Test Scenario: Looking up songs heard to identify the artist
def test_identify_artist(client):
    # GIVEN the user goes to the webpage
    response = client.get('/')
    assert response.status_code == 200

    # AND finds the song via search, album, songlist, or artist
    # For the sake of demonstration, let's assume song search by title "SongTitle"
    search_query = "SongTitle"
    search_response = client.get(f'/search?query={search_query}')
    assert search_response.status_code == 200

    # WHEN the user clicks on a specific song
    song_id = 1  # Replace with the specific song ID
    song_url = url_for('show_song', song_id=song_id)
    song_response = client.get(song_url)

    # THEN the song is displayed
    assert song_response.status_code == 200
    assert "SongTitle" in song_response.data.decode()

