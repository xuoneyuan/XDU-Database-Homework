DROP SCHEMA IF EXISTS library;
CREATE SCHEMA IF NOT EXISTS library;

USE library;

CREATE TABLE IF NOT EXISTS book (
    ISBN CHAR(13),
    book_name CHAR(20),
    press CHAR(20),
    author CHAR(20),
    book_classification CHAR(20),
    year_of_publication CHAR(4),
    remaining_quantity INT
);



CREATE TABLE IF NOT EXISTS borrowing (
    internal BOOLEAN,
    ISBN CHAR(13),
    ID_number CHAR(20),
    borrow_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    return_time TIMESTAMP,
    fine INT DEFAULT 0
);



CREATE TABLE IF NOT EXISTS internal_staff (
    ID_number CHAR(18),
    full_name CHAR(20),
    number_of_books_borrowed INT DEFAULT 0,
    overdue INT DEFAULT 0
);



CREATE TABLE IF NOT EXISTS external_staff (
    ID_number CHAR(18),
    full_name CHAR(20),
    number_of_books_borrowed INT DEFAULT 0,
    overdue INT DEFAULT 0
);
