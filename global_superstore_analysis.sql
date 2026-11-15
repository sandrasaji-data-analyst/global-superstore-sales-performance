CREATE DATABASE global_superstore;

USE global_superstore;

SELECT *
FROM global_superstore_cleaned;

#Top 10 customers
SELECT
    `Customer Name`,
    SUM(Sales) AS Total_Sales
FROM global_superstore_cleaned
GROUP BY `Customer Name`
ORDER BY Total_Sales DESC
LIMIT 10;

#category has the most orders
SELECT 
    Category, COUNT(`Order ID`) AS Total_Orders
FROM
    global_superstore_cleaned
GROUP BY Category
ORDER BY Total_Orders DESC;

#Countries are present
SELECT DISTINCT Country
FROM  global_superstore_cleaned
ORDER BY Country;

#Orders with sales above 500
SELECT *
FROM global_superstore_cleaned
WHERE Sales > 500;

#Sales by year
SELECT
    YEAR(`Order Date`) AS Order_Year,
    SUM(Sales) AS Total_Sales
FROM global_superstore_cleaned
GROUP BY YEAR(`Order Date`)
ORDER BY Order_Year;

#Category has the most orders
SELECT
    Category,
    COUNT(`Order ID`) AS Total_Orders
FROM global_superstore_cleaned
GROUP BY Category
ORDER BY Total_Orders DESC;


