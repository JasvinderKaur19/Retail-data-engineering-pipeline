# Databricks notebook source
# Demonstration of an incremental loading pattern using a watermark.

from pyspark.sql import functions as F

SOURCE_PATH = "abfss://raw@<storage-account>.dfs.core.windows.net/"
TARGET_PATH = "abfss://silver@<storage-account>.dfs.core.windows.net/sales"

# In production, store the watermark in a control table.
last_watermark = "2025-06-30"

new_data = (
    spark.read.option("header", True).csv(f"{SOURCE_PATH}/sales.csv")
    .withColumn("order_date", F.to_date("order_date", "yyyy-MM-dd"))
    .filter(F.col("order_date") > F.lit(last_watermark))
)

print(f"Records selected for incremental processing: {new_data.count()}")

# After validation/transformation, use Delta MERGE in a production pipeline
# to insert new records and update changed records.
