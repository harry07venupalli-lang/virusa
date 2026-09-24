# Online Retail Sales Analysis Database

## Project Overview
This SQL project builds a relational database for an online retail store and uses SQL queries to extract business insights from customer, product, order, and order-item data.

## Objectives
- Create a relational database for an online store.
- Store customer, product, and order data.
- Analyze sales performance using SQL.
- Identify top-selling products and valuable customers.
- Calculate monthly revenue and category-wise sales.
- Detect inactive customers.

## Database Schema
Customers(customer_id PK, name, city)
Products(product_id PK, name, category, price)
Orders(order_id PK, customer_id FK, date)
Order_Items(order_id PK/FK, product_id PK/FK, quantity)

## Files
- schema.sql - creates tables, constraints, and indexes.
- data/sample_data.sql - inserts sample data.
- sql/analysis_queries.sql - analysis queries.
- PROJECT_REPORT.md - project report.

## How to Run
1. Create a PostgreSQL database named online_retail.
2. Run schema.sql.
3. Run data/sample_data.sql.
4. Run individual queries from sql/analysis_queries.sql.

## Main Insights
Top-selling products, valuable customers, monthly revenue, category revenue, inactive customers, average order value, revenue growth, and product performance.
