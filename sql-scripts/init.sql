CREATE TABLE IF NOT EXISTS Artist (
    ArtistID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Genre VARCHAR(50),
    Description TEXT
);

CREATE TABLE IF NOT EXISTS Album (
    AlbumID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(100),
    ReleaseYear INT,
    ArtistID INT,
    FOREIGN KEY (ArtistID) REFERENCES Artist(ArtistID)
);

CREATE TABLE IF NOT EXISTS Song (
    SongID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(100),
    AlbumID INT,
    Duration TIME,
    ArtistID INT,
    FOREIGN KEY (AlbumID) REFERENCES Album(AlbumID),
    FOREIGN KEY (ArtistID) REFERENCES Artist(ArtistID)
);

CREATE TABLE IF NOT EXISTS Review (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,
    SongID INT,
    AlbumID INT,
    ReviewerID INT,
    Rating INT,
    Comments TEXT,
    FOREIGN KEY (SongID) REFERENCES Song(SongID),
    FOREIGN KEY (AlbumID) REFERENCES Album(AlbumID)
);
CREATE TABLE IF NOT EXISTS User (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100)
);

-- Insert sample data into the User table (optional)
INSERT INTO User (first_name, email, password) VALUES
    ('John', 'john@example.com', 'hashed_password_here'),
    ('Alice', 'alice@example.com', 'hashed_password_here');

-- Inserting sample data into the Artist table
INSERT INTO Artist (Name, Genre, Description) VALUES
    ('Queen', 'Rock', 'Legendary British rock band'),
    ('Michael Jackson', 'Pop', 'King of Pop'),
    ('The Beatles', 'Rock', 'Influential rock band'),
    ('Madonna', 'Pop', 'Queen of Pop');

-- Inserting sample data into the Album table
INSERT INTO Album (Title, ReleaseYear, ArtistID) VALUES
    ('A Night at the Opera', 1975, 1),  -- Queen
    ('Thriller', 1982, 2),              -- Michael Jackson
    ('Abbey Road', 1969, 3),            -- The Beatles
    ('Like a Prayer', 1989, 4);         -- Madonna

-- Inserting sample data into the Song table
INSERT INTO Song (Title, AlbumID, Duration, ArtistID) VALUES
    ('Bohemian Rhapsody', 1, '5:55', 1),      -- Queen
    ('Billie Jean', 2, '4:54', 2),            -- Michael Jackson
    ('Come Together', 3, '4:20', 3),          -- The Beatles
    ('Like a Prayer', 4, '5:41', 4);          -- Madonna

-- Inserting sample data into the Review table
INSERT INTO Review (SongID, AlbumID, ReviewerID, Rating, Comments) VALUES
    (1, 1, 101, 5, 'One of the greatest albums ever!'),    -- Bohemian Rhapsody - A Night at the Opera (Queen)
    (2, 2, 102, 4, 'Classic track by MJ'),               -- Billie Jean - Thriller (Michael Jackson)
    (3, 3, 103, 5, 'Timeless Beatles hit'),              -- Come Together - Abbey Road (The Beatles)
    (4, 4, 104, 4, 'Madonna at her best'),               -- Like a Prayer - Like a Prayer (Madonna)
    (1, 1, 104, 4, 'Queen at their best');               -- queen 2
