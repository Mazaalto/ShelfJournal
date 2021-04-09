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
    sent_at TIMESTAMP
);
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    review TEXT,
    user_id INTEGER REFERENCES books,
    sent_at TIMESTAMP
);




