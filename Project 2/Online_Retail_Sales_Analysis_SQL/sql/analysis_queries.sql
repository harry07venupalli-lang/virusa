-- Online Retail Sales Analysis

SELECT o.order_id,o.date,c.customer_id,c.name AS customer_name,p.product_id,p.name AS product_name,p.category,oi.quantity,p.price,oi.quantity*p.price AS line_revenue
FROM orders o JOIN customers c ON c.customer_id=o.customer_id JOIN order_items oi ON oi.order_id=o.order_id JOIN products p ON p.product_id=oi.product_id
ORDER BY o.date,o.order_id;

SELECT p.product_id,p.name AS product_name,p.category,SUM(oi.quantity) AS units_sold,SUM(oi.quantity*p.price) AS revenue
FROM products p JOIN order_items oi ON oi.product_id=p.product_id
GROUP BY p.product_id,p.name,p.category ORDER BY units_sold DESC,revenue DESC;

SELECT c.customer_id,c.name,c.city,COUNT(DISTINCT o.order_id) AS total_orders,SUM(oi.quantity*p.price) AS total_spend
FROM customers c JOIN orders o ON o.customer_id=c.customer_id JOIN order_items oi ON oi.order_id=o.order_id JOIN products p ON p.product_id=oi.product_id
GROUP BY c.customer_id,c.name,c.city ORDER BY total_spend DESC;

SELECT DATE_TRUNC('month',o.date)::date AS month,SUM(oi.quantity*p.price) AS monthly_revenue
FROM orders o JOIN order_items oi ON oi.order_id=o.order_id JOIN products p ON p.product_id=oi.product_id
GROUP BY DATE_TRUNC('month',o.date) ORDER BY month;

SELECT p.category,SUM(oi.quantity) AS units_sold,SUM(oi.quantity*p.price) AS revenue,
ROUND(100.0*SUM(oi.quantity*p.price)/SUM(SUM(oi.quantity*p.price)) OVER (),2) AS revenue_percentage
FROM products p JOIN order_items oi ON oi.product_id=p.product_id
GROUP BY p.category ORDER BY revenue DESC;

WITH last_order AS (SELECT MAX(date) AS max_date FROM orders)
SELECT c.customer_id,c.name,c.city,MAX(o.date) AS last_order_date
FROM customers c LEFT JOIN orders o ON o.customer_id=c.customer_id CROSS JOIN last_order
GROUP BY c.customer_id,c.name,c.city,last_order.max_date
HAVING MAX(o.date) IS NULL OR MAX(o.date)<last_order.max_date-INTERVAL '90 days'
ORDER BY last_order_date NULLS FIRST;

WITH customer_spend AS (
SELECT c.customer_id,c.name,SUM(oi.quantity*p.price) AS total_spend
FROM customers c JOIN orders o ON o.customer_id=c.customer_id JOIN order_items oi ON oi.order_id=o.order_id JOIN products p ON p.product_id=oi.product_id
GROUP BY c.customer_id,c.name)
SELECT customer_id,name,total_spend,DENSE_RANK() OVER(ORDER BY total_spend DESC) AS spending_rank FROM customer_spend ORDER BY spending_rank;

SELECT ROUND(SUM(order_total)/COUNT(*),2) AS average_order_value FROM (
SELECT o.order_id,SUM(oi.quantity*p.price) AS order_total
FROM orders o JOIN order_items oi ON oi.order_id=o.order_id JOIN products p ON p.product_id=oi.product_id GROUP BY o.order_id) t;

SELECT DATE_TRUNC('month',o.date)::date AS month,SUM(oi.quantity*p.price) AS revenue
FROM orders o JOIN order_items oi ON oi.order_id=o.order_id JOIN products p ON p.product_id=oi.product_id
GROUP BY DATE_TRUNC('month',o.date) ORDER BY revenue DESC LIMIT 1;

SELECT p.category,p.name AS product_name,SUM(oi.quantity) AS units_sold,SUM(oi.quantity*p.price) AS revenue
FROM products p JOIN order_items oi ON oi.product_id=p.product_id
GROUP BY p.category,p.product_id,p.name ORDER BY p.category,revenue DESC;

SELECT c.customer_id,c.name,c.city FROM customers c LEFT JOIN orders o ON o.customer_id=c.customer_id WHERE o.order_id IS NULL;

WITH monthly AS (
SELECT DATE_TRUNC('month',o.date)::date AS month,SUM(oi.quantity*p.price) AS revenue
FROM orders o JOIN order_items oi ON oi.order_id=o.order_id JOIN products p ON p.product_id=oi.product_id
GROUP BY DATE_TRUNC('month',o.date))
SELECT month,revenue,ROUND(100.0*(revenue-LAG(revenue) OVER(ORDER BY month))/NULLIF(LAG(revenue) OVER(ORDER BY month),0),2) AS revenue_growth_percentage
FROM monthly ORDER BY month;
