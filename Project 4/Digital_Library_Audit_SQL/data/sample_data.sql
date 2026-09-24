-- SAMPLE DATA FOR DIGITAL LIBRARY AUDIT
INSERT INTO Books (BookID,Title,Author,Category,PublishedYear) VALUES
(1,'The Silent River','A. Rao','Fiction',2019),(2,'Introduction to Physics','R. Kumar','Science',2021),(3,'World History Basics','S. Mehta','History',2018),(4,'Modern Chemistry','P. Singh','Science',2020),(5,'The Lost Kingdom','N. Sharma','Fiction',2017),(6,'Indian History Today','K. Iyer','History',2022),(7,'Data Structures','M. Verma','Technology',2023),(8,'Machine Learning Fundamentals','D. Patel','Technology',2024),(9,'Poems of the Moon','L. Das','Poetry',2016),(10,'Environmental Science','T. Nair','Science',2022);

INSERT INTO Students (StudentID,StudentName,Email,JoinDate) VALUES
(101,'Aarav Sharma','aarav@example.com','2022-06-10'),(102,'Priya Reddy','priya@example.com','2023-01-15'),(103,'Rahul Verma','rahul@example.com','2021-08-20'),(104,'Sneha Rao','sneha@example.com','2020-03-11'),(105,'Arjun Mehta','arjun@example.com','2024-02-01'),(106,'Ananya Singh','ananya@example.com','2022-09-18'),(107,'Vikram Nair','vikram@example.com','2021-12-05'),(108,'Kavya Patel','kavya@example.com','2024-07-12');

INSERT INTO IssuedBooks (IssueID,BookID,StudentID,IssueDate,ReturnDate) VALUES
(1001,1,101,CURRENT_DATE-INTERVAL '5 days',CURRENT_DATE-INTERVAL '1 day'),
(1002,2,102,CURRENT_DATE-INTERVAL '20 days',NULL),
(1003,3,103,CURRENT_DATE-INTERVAL '10 days',CURRENT_DATE-INTERVAL '2 days'),
(1004,4,104,CURRENT_DATE-INTERVAL '40 days',NULL),
(1005,5,105,CURRENT_DATE-INTERVAL '7 days',NULL),
(1006,6,106,CURRENT_DATE-INTERVAL '25 days',CURRENT_DATE-INTERVAL '5 days'),
(1007,7,107,CURRENT_DATE-INTERVAL '120 days',NULL),
(1008,8,102,CURRENT_DATE-INTERVAL '35 days',CURRENT_DATE-INTERVAL '10 days'),
(1009,9,101,CURRENT_DATE-INTERVAL '15 days',NULL),
(1010,10,102,CURRENT_DATE-INTERVAL '60 days',NULL),
(1011,1,103,CURRENT_DATE-INTERVAL '8 days',CURRENT_DATE-INTERVAL '2 days'),
(1012,2,102,CURRENT_DATE-INTERVAL '5 days',NULL),
(1013,3,104,CURRENT_DATE-INTERVAL '30 days',NULL),
(1014,4,105,CURRENT_DATE-INTERVAL '3 days',NULL),
(1015,5,106,CURRENT_DATE-INTERVAL '12 days',CURRENT_DATE-INTERVAL '2 days'),
(1016,6,102,CURRENT_DATE-INTERVAL '18 days',NULL),
(1017,7,108,CURRENT_DATE-INTERVAL '2 days',NULL),
(1018,8,102,CURRENT_DATE-INTERVAL '22 days',CURRENT_DATE-INTERVAL '3 days'),
(1019,9,104,CURRENT_DATE-INTERVAL '45 days',NULL),
(1020,10,103,CURRENT_DATE-INTERVAL '16 days',NULL),
(1021,1,105,CURRENT_DATE-INTERVAL '9 days',NULL),
(1022,2,106,CURRENT_DATE-INTERVAL '6 days',NULL),
(1023,3,107,CURRENT_DATE-INTERVAL '4 years',CURRENT_DATE-INTERVAL '4 years'+INTERVAL '10 days'),
(1024,4,107,CURRENT_DATE-INTERVAL '4 years'-INTERVAL '10 days',CURRENT_DATE-INTERVAL '4 years');
