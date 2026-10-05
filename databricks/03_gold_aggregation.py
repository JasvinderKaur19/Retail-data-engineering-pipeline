# Databricks notebook source
# Gold Layer: business-ready datasets for reporting.

from pyspark.sql import functions as F

SILVER_PATH = "abfss://silver@<storage-account>.dfs.core.windows.net/"
GOLD_PATH = "abfss://gold@<storage-account>.dfs.core.windows.net/"

sales = spark.read.format("delta").load(f"{SILVER_PATH}/sales")

# Daily sales summary
daily_sales = (
    sales.groupBy("order_date")
    .agg(
        F.sum("net_sales").alias("total_sales"),
        F.sum("quantity").alias("units_sold"),
        F.countDistinct("sales_id").alias("orders")
    )
)

daily_sales.write.format("delta").mode("overwrite").save(
    f"{GOLD_PATH}/gold_sales_daily"
)

# Product performance
product_sales = (
    sales.groupBy("product_id")
    .agg(
        F.sum("net_sales").alias("total_sales"),
        F.sum("quantity").alias("units_sold"),
        F.countDistinct("sales_id").alias("orders")
    )
)

product_sales.write.format("delta").mode("overwrite").save(
    f"{GOLD_PATH}/gold_product_performance"
)

# Store performance
store_sales = (
    sales.groupBy("store_id")
    .agg(
        F.sum("net_sales").alias("total_sales"),
        F.sum("quantity").alias("units_sold"),
        F.countDistinct("sales_id").alias("orders")
    )
)

store_sales.write.format("delta").mode("overwrite").save(
    f"{GOLD_PATH}/gold_store_performance"
)
