-- Gold-layer analytical tables
CREATE TABLE gold_sales_daily (
    order_date DATE,
    total_sales DECIMAL(18,2),
    units_sold INT,
    orders INT
);

CREATE TABLE gold_product_performance (
    product_id VARCHAR(20),
    total_sales DECIMAL(18,2),
    units_sold INT,
    orders INT
);

CREATE TABLE gold_store_performance (
    store_id VARCHAR(20),
    total_sales DECIMAL(18,2),
    units_sold INT,
    orders INT
);
