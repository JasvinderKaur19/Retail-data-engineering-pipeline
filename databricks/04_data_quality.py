# Databricks notebook source
# Data quality checks and rejected-record identification.

from pyspark.sql import functions as F

BRONZE_PATH = "abfss://bronze@<storage-account>.dfs.core.windows.net/"
sales = spark.read.format("delta").load(f"{BRONZE_PATH}/sales")

checks = {
    "null_sales_id": sales.filter(F.col("sales_id").isNull()).count(),
    "null_customer_id": sales.filter(
        F.col("customer_id").isNull() | (F.trim(F.col("customer_id")) == "")
    ).count(),
    "invalid_quantity": sales.filter(F.col("quantity").cast("int") <= 0).count(),
    "invalid_product_id": sales.filter(F.col("product_id").isNull()).count(),
    "duplicate_sales_id": (
        sales.groupBy("sales_id").count()
        .filter(F.col("count") > 1).count()
    )
}

for check, value in checks.items():
    print(f"{check}: {value}")

# In a production implementation, failed checks could trigger
# an alert or route invalid records to a quarantine/rejected zone.
