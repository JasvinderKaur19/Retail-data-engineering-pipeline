-- Business analysis examples

-- Monthly sales
SELECT
    DATE_TRUNC('month', order_date) AS sales_month,
    SUM(net_sales) AS total_sales
FROM silver_sales
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY sales_month;

-- Top products
SELECT
    product_id,
    SUM(net_sales) AS total_sales,
    SUM(quantity) AS units_sold
FROM silver_sales
GROUP BY product_id
ORDER BY total_sales DESC
LIMIT 10;

-- Store performance
SELECT
    store_id,
    SUM(net_sales) AS total_sales,
    COUNT(DISTINCT sales_id) AS orders
FROM silver_sales
GROUP BY store_id
ORDER BY total_sales DESC;
