# Databricks notebook source
# Bronze Layer: ingest raw files into Delta tables
# Replace paths with your Azure Data Lake Storage paths.

from pyspark.sql import functions as F

SOURCE_PATH = "abfss://raw@<storage-account>.dfs.core.windows.net/"
BRONZE_PATH = "abfss://bronze@<storage-account>.dfs.core.windows.net/"

# Example: sales
sales_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(f"{SOURCE_PATH}/sales.csv")
)

sales_df = sales_df.withColumn("_ingestion_timestamp", F.current_timestamp())

(
    sales_df.write
    .format("delta")
    .mode("append")
    .save(f"{BRONZE_PATH}/sales")
)

# Repeat the same pattern for customers, products and stores.
