# Digital Library Audit

PostgreSQL-compatible SQL project for auditing library books, students, and borrowing activity.

## Features
- Relational library schema
- Overdue-book report
- Category popularity index
- Inactive-student analysis
- Cleanup query with a SELECT preview
- Currently borrowed books report
- Full issue history

## Run
Create a PostgreSQL database, run `schema.sql`, then `data/sample_data.sql`, followed by the required queries in `analysis_queries.sql`.