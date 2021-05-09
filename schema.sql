CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    admin INTEGER
);
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    book_title TEXT,
    author_name TEXT,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP,
    info TEXT,
    visibility TEXT

);
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    book_id INTEGER REFERENCES books,
    stars INTEGER,
    text_review TEXT,
    visibility TEXT,
    sent_at TIMESTAMP,
    user_id INTEGER REFERENCES users
);
CREATE TABLE clubs (
    id SERIAL PRIMARY KEY,
    club_title TEXT,
    club_info TEXT,
    club_password TEXT,
    user_id INTEGER REFERENCES users,
    visibility TEXT
);
CREATE TABLE persons_of_club (
    id SERIAL PRIMARY KEY,
    club_id INTEGER REFERENCES clubs,
    user_id INTEGER REFERENCES users
);