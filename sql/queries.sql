-- === Retail Sales Analysis : SQL Scripts ===
-- How to run in SQLite shell:
--   .read sql/queries.sql
-- these are the quries

-- Make outputs readable in sqlite shell (these are sqlite dot-commands)
.headers on
.mode column
.nullvalue NULL

-- 1. Monthly Sales
SELECT Month, SUM(TotalAmount) AS MonthlySales
FROM sales
GROUP BY Month;

-- 2. Top Month by Sales
SELECT Month, SUM(TotalAmount) AS MonthlySales
FROM sales
GROUP BY Month
ORDER BY MonthlySales DESC
LIMIT 1;

-- 3. Product-wise Sales
SELECT Product, SUM(TotalAmount) AS ProductSales
FROM sales
GROUP BY Product
ORDER BY ProductSales DESC;

-- 4. Month + Product Sales
SELECT Month, Product, SUM(TotalAmount) AS Sales
FROM sales
GROUP BY Month, Product
ORDER BY Month, Sales DESC;

-- 5. Top-Selling Product per Month (inner query)
SELECT Month, Product, MAX(Sales) AS TopSales
FROM (
    SELECT Month, Product, SUM(TotalAmount) AS Sales
    FROM sales
    GROUP BY Month, Product
)
GROUP BY Month;
