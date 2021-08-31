DROP TABLE if EXISTS songs CASCADE;
DROP TABLE if EXISTS artists CASCADE;
DROP TABLE if EXISTS genres CASCADE;
DROP TABLE if EXISTS albums CASCADE;
DROP TABLE if EXISTS sub_genres CASCADE;
DROP TABLE if EXISTS tags CASCADE;

CREATE TABLE songs (
    id SERIAL PRIMARY KEY NOT NULL,
    title TEXT NOT NULL,
    album INTEGER FOREIGN KEY REFERENCES albums(id),
    artist INTEGER NOT NULL FOREIGN KEY REFERENCES artists(id),
    genre INTEGER[2] NOT NULL, --Each song only has 2 genres associated with it for the sake of
                            --simplicity. This could be extended later with weights on the genres
                            --to increase playlist creation flexibility.
    rating REAL --Ratings being floating point feels right, exact convention TBD
);

CREATE TABLE artists (
    id SERIAL PRIMARY KEY NOT NULL,
    artist_name VARCHAR(50)
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY NOT NULL,
    title TEXT NOT NULL,
    artist INTEGER NOT NULL FOREIGN KEY REFERENCES artists(id),
    genre INTEGER[2] NOT NULL -- Same logic as song genre specification. PostgreSQL does not enforce
                              -- array length so while I will stick to 2 genres as convention, adding
                              -- more in the future won't break the code (yet).
);

CREATE TABLE genres (
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE sub_genres (
    id SERIAL PRIMARY KEY NOT NULL,
    parent_id INTEGER NOT NULL FOREIGN KEY REFERENCES genres(id),
    name VARCHAR(50) NOT NULL
);

CREATE TABLE tags (
    song_id INTEGER NOT NULL FOREIGN KEY REFERENCES songs(id),
    tag_content TEXT NOT NULL
);