-- DIGITAL LIBRARY AUDIT
-- PostgreSQL-compatible SQL

DROP TABLE IF EXISTS IssuedBooks;
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Students;

CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(200) NOT NULL,
    Author VARCHAR(150) NOT NULL,
    Category VARCHAR(100) NOT NULL,
    PublishedYear INT
);

CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(150) NOT NULL,
    Email VARCHAR(200) UNIQUE,
    JoinDate DATE NOT NULL
);

CREATE TABLE IssuedBooks (
    IssueID INT PRIMARY KEY,
    BookID INT NOT NULL REFERENCES Books(BookID),
    StudentID INT NOT NULL REFERENCES Students(StudentID),
    IssueDate DATE NOT NULL,
    ReturnDate DATE NULL
);

CREATE INDEX idx_issuedbooks_book ON IssuedBooks(BookID);
CREATE INDEX idx_issuedbooks_student ON IssuedBooks(StudentID);
CREATE INDEX idx_issuedbooks_issue_date ON IssuedBooks(IssueDate);
