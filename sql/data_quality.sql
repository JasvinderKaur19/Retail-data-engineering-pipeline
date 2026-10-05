-- Example SQL data-quality checks

-- Duplicate transaction IDs
SELECT sales_id, COUNT(*) AS record_count
FROM sales
GROUP BY sales_id
HAVING COUNT(*) > 1;

-- Invalid quantities
SELECT *
FROM sales
WHERE quantity <= 0;

-- Missing customer IDs
SELECT *
FROM sales
WHERE customer_id IS NULL OR TRIM(customer_id) = '';

-- Invalid product references
SELECT s.*
FROM sales s
LEFT JOIN products p ON s.product_id = p.product_id
WHERE p.product_id IS NULL;
