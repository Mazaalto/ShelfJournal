CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    book_title TEXT,
    author_name TEXT,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP,
    info TEXT

);
CREATE TABLE review_as_stars (
    id SERIAL PRIMARY KEY,
    topic TEXT,
    created_at TIMESTAMP
);
CREATE TABLE stars (
    id SERIAL PRIMARY KEY,
    book_id INTEGER REFERENCES review_as_stars,
    stars TEXT
);
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    stars_id INTEGER REFERENCES stars,
    sent_at TIMESTAMP
);




