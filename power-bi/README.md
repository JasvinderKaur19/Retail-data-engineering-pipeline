# Power BI Dashboard

Dashboard preview: `dashboard_screenshots/retail_sales_dashboard_preview.png`

## Power BI-ready data
The `gold_exports/` folder contains cleaned Gold-layer exports for the report.

## Recommended visuals
- Total Sales
- Orders
- Units Sold
- Average Order Value
- Monthly Sales Trend
- Sales by Category
- Top Stores by Sales
- Top Products

## Suggested DAX
```DAX
Total Sales = SUM(Sales[net_sales])
Orders = DISTINCTCOUNT(Sales[sales_id])
Units Sold = SUM(Sales[quantity])
Average Order Value = DIVIDE([Total Sales], [Orders])
```

A `.pbix` file itself must be created/saved by Power BI Desktop. This folder contains the data, model guidance, DAX measures, and dashboard preview needed to recreate it.
