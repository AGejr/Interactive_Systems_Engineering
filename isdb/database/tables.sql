CREATE TABLE Artist (
    ArtistID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Genre VARCHAR(50),
    Description TEXT
);

CREATE TABLE Album (
    AlbumID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(100),
    ReleaseYear INT,
    ArtistID INT,
    FOREIGN KEY (ArtistID) REFERENCES Artist(ArtistID)
);

CREATE TABLE Song (
    SongID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(100),
    AlbumID INT,
    Duration TIME,
    ArtistID INT,
    FOREIGN KEY (AlbumID) REFERENCES Album(AlbumID),
    FOREIGN KEY (ArtistID) REFERENCES Artist(ArtistID)
);

CREATE TABLE Review (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,
    SongID INT,
    AlbumID INT,
    ReviewerID INT,
    Rating INT,
    Comments TEXT,
    FOREIGN KEY (SongID) REFERENCES Song(SongID),
    FOREIGN KEY (AlbumID) REFERENCES Album(AlbumID)
);

