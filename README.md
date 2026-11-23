# Global Livestock & Meat Export Market Explorer

## The Concept

Major European meat and dairy processors (like Ireland's Dawn Meats or ABP Food Group) constantly track global import/export trends to decide where to ship products.

## What It Does

An exploratory data analysis (EDA) using real, public agricultural trade data from the **FAO (Food and Agriculture Organization)**.

## Tools Used

`Pandas`, `NumPy`, `Seaborn`

## Where To Get The Data

Download a free CSV of global beef, poultry, or milk production by country from **FAOSTAT Data Portal**.

## Key Tasks To Code:

1. Cleans the raw FAO dataset (removes missing values, standardizes country names, and filters for the last 10 years).
2. Calculates the **Year-over-Year (YoY) percentage growth** in poultry and dairy production for European countries vs. the Middle East.
3. Builds a **heatmap** `Seaborn` to visualize the top 10 producing nations over the decade.  
