# Databricks notebook source
# Silver Layer: clean, validate and transform raw data.

from pyspark.sql import functions as F
from pyspark.sql.window import Window

BRONZE_PATH = "abfss://bronze@<storage-account>.dfs.core.windows.net/"
SILVER_PATH = "abfss://silver@<storage-account>.dfs.core.windows.net/"

sales = spark.read.format("delta").load(f"{BRONZE_PATH}/sales")

# Standardize data types
sales = (
    sales
    .withColumn("order_date", F.to_date("order_date", "yyyy-MM-dd"))
    .withColumn("quantity", F.col("quantity").cast("int"))
    .withColumn("unit_price", F.col("unit_price").cast("double"))
    .withColumn("discount", F.col("discount").cast("double"))
)

# Remove duplicate transaction IDs
sales = sales.dropDuplicates(["sales_id"])

# Basic validation / filtering
sales_clean = (
    sales
    .filter(F.col("sales_id").isNotNull())
    .filter(F.col("order_date").isNotNull())
    .filter(F.col("customer_id").isNotNull() & (F.trim(F.col("customer_id")) != ""))
    .filter(F.col("product_id").isNotNull())
    .filter(F.col("quantity") > 0)
    .filter(F.col("unit_price") > 0)
)

# Derived business metric
sales_clean = sales_clean.withColumn(
    "net_sales",
    F.round(F.col("quantity") * F.col("unit_price") * (1 - F.col("discount")), 2)
)

(
    sales_clean.write
    .format("delta")
    .mode("overwrite")
    .save(f"{SILVER_PATH}/sales")
)
