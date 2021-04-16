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
CREATE TABLE stars (
    id SERIAL PRIMARY KEY,
    book_id INTEGER REFERENCES books,
    choice TEXT
);
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    star_id INTEGER REFERENCES stars,
    sent_at TIMESTAMP
);





