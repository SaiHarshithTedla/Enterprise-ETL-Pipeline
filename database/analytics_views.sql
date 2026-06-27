-- ============================================================
-- RetailX Analytics Views
-- ============================================================

---------------------------------------------------------------
-- 1. Monthly Sales
---------------------------------------------------------------

CREATE OR REPLACE VIEW vw_monthly_sales AS
SELECT
    DATE_TRUNC('month', o.order_date) AS month,
    SUM(oi.quantity * p.price) AS total_sales,
    COUNT(DISTINCT o.order_id) AS total_orders
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY DATE_TRUNC('month', o.order_date)
ORDER BY month;


---------------------------------------------------------------
-- 2. Top Selling Products
---------------------------------------------------------------

CREATE OR REPLACE VIEW vw_top_products AS
SELECT
    p.product_id,
    p.product_name,
    p.category,
    SUM(oi.quantity) AS units_sold,
    SUM(oi.quantity * p.price) AS revenue
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY
    p.product_id,
    p.product_name,
    p.category
ORDER BY revenue DESC;


---------------------------------------------------------------
-- 3. Category Sales
---------------------------------------------------------------

CREATE OR REPLACE VIEW vw_category_sales AS
SELECT
    p.category,
    SUM(oi.quantity * p.price) AS revenue,
    SUM(oi.quantity) AS quantity_sold
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY revenue DESC;


---------------------------------------------------------------
-- 4. Payment Method Distribution
---------------------------------------------------------------

CREATE OR REPLACE VIEW vw_payment_distribution AS
SELECT
    payment_method,
    COUNT(*) AS total_orders
FROM orders
GROUP BY payment_method
ORDER BY total_orders DESC;


---------------------------------------------------------------
-- 5. Top Customers
---------------------------------------------------------------

CREATE OR REPLACE VIEW vw_top_customers AS
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.city,
    c.state,
    SUM(oi.quantity * p.price) AS total_spent
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name,
    c.city,
    c.state
ORDER BY total_spent DESC;