-- DIGITAL LIBRARY AUDIT - ANALYTICAL QUERIES

SELECT s.StudentID,s.StudentName,b.BookID,b.Title,b.Category,ib.IssueDate,CURRENT_DATE-ib.IssueDate AS DaysBorrowed
FROM IssuedBooks ib JOIN Students s ON s.StudentID=ib.StudentID JOIN Books b ON b.BookID=ib.BookID
WHERE ib.ReturnDate IS NULL AND ib.IssueDate<CURRENT_DATE-INTERVAL '14 days' ORDER BY ib.IssueDate;

SELECT b.Category,COUNT(*) AS TimesBorrowed
FROM IssuedBooks ib JOIN Books b ON b.BookID=ib.BookID GROUP BY b.Category ORDER BY TimesBorrowed DESC;

SELECT s.StudentID,s.StudentName,MAX(ib.IssueDate) AS LastBorrowDate
FROM Students s LEFT JOIN IssuedBooks ib ON ib.StudentID=s.StudentID
GROUP BY s.StudentID,s.StudentName
HAVING MAX(ib.IssueDate) IS NULL OR MAX(ib.IssueDate)<CURRENT_DATE-INTERVAL '3 years'
ORDER BY LastBorrowDate NULLS FIRST;

-- Review the SELECT above before running this cleanup.
DELETE FROM Students s
WHERE NOT EXISTS (
    SELECT 1 FROM IssuedBooks ib
    WHERE ib.StudentID=s.StudentID AND ib.IssueDate>=CURRENT_DATE-INTERVAL '3 years'
);

SELECT s.StudentName,b.Title,ib.IssueDate
FROM IssuedBooks ib JOIN Students s ON s.StudentID=ib.StudentID JOIN Books b ON b.BookID=ib.BookID
WHERE ib.ReturnDate IS NULL ORDER BY ib.IssueDate;

SELECT ib.IssueID,s.StudentName,b.Title,b.Category,ib.IssueDate,ib.ReturnDate
FROM IssuedBooks ib JOIN Students s ON s.StudentID=ib.StudentID JOIN Books b ON b.BookID=ib.BookID
ORDER BY ib.IssueDate DESC;
