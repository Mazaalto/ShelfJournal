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





