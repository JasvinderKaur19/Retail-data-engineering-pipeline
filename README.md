# Retail Sales Data Engineering Pipeline

## Overview

An end-to-end data engineering project that demonstrates how retail sales data can be ingested, cleaned, transformed, validated, and prepared for business intelligence reporting using a cloud-oriented data platform architecture.

The project follows a simple Bronze/Silver/Gold (Medallion) approach and includes an incremental-loading pattern and data-quality checks.

## Architecture

CSV Source  
→ Azure Data Factory  
→ Azure Data Lake Storage  
→ Databricks / PySpark  
→ Delta Lake  
→ SQL / Synapse Analytics  
→ Power BI

See `docs/architecture.txt` for the architecture overview.

## Technologies

- Azure Data Factory
- Azure Data Lake Storage
- Azure Databricks
- PySpark / Spark
- Delta Lake
- SQL
- Power BI
- Git / GitHub

## Project Features

- Batch data ingestion
- Bronze/Silver/Gold data architecture
- Data cleansing and transformation
- Data validation
- Duplicate and invalid-record checks
- Incremental loading pattern using a watermark
- Business-ready Gold datasets
- SQL analysis
- Power BI-ready output

## Repository Structure

```text
data/
  raw/                  Source datasets
  sample/               Small sample datasets

azure-data-factory/
  pipelines/            Pipeline templates
  datasets/             Dataset templates
  linked-services/      Configuration placeholders

databricks/
  01_bronze_ingestion.py
  02_silver_transformation.py
  03_gold_aggregation.py
  04_data_quality.py
  05_incremental_loading.py

sql/
  create_tables.sql
  data_quality.sql
  analytical_queries.sql

power-bi/
  dashboard_screenshots/

docs/
  architecture.txt
```

## Data Quality

The sample sales data intentionally contains a small number of issues so the project can demonstrate validation and cleansing.

Examples include:

- Duplicate transaction IDs
- Missing customer IDs
- Invalid quantities
- Invalid dates
- Invalid product references

The `04_data_quality.py` notebook demonstrates how these checks can be automated.

## Incremental Loading

The `05_incremental_loading.py` notebook demonstrates a watermark-based incremental loading approach.

In a production environment, the watermark would normally be maintained in a control table or metadata store and used by the orchestration pipeline to process only new or changed records.

## Azure Setup

The repository contains templates rather than Azure credentials.

To reproduce the cloud pipeline:

1. Create an Azure resource group.
2. Create an Azure Data Lake Storage Gen2 account.
3. Create Bronze, Silver and Gold containers/folders.
4. Create an Azure Data Factory instance.
5. Configure linked services securely.
6. Create datasets and a pipeline based on the templates.
7. Create an Azure Databricks workspace.
8. Run the notebooks in sequence.
9. Connect the Gold layer to SQL/Synapse and Power BI.

**Never commit Azure keys, passwords, connection strings, access tokens or other secrets to GitHub.**

## Resume Project Description

**Retail Sales Data Engineering Pipeline — Azure Data Factory, Databricks, Data Lake, PySpark, Delta Lake, SQL**

- Built an end-to-end data pipeline to ingest retail sales data into Azure Data Lake and process it using Azure Data Factory and Databricks.
- Used PySpark to clean, validate, transform, and enrich datasets using a Bronze/Silver/Gold architecture.
- Implemented data-quality checks and a watermark-based incremental loading pattern to improve processing efficiency and data reliability.
- Prepared curated datasets for SQL analysis and Power BI reporting.

## Disclaimer

This project is a personal portfolio project using synthetic retail data. Azure configuration files are templates and contain no credentials or production data.
