# Customer Shopping Behavior Data Cleaning & Transformation

## Overview
This project focuses on cleaning and transforming a raw customer shopping behavior dataset using Python and Pandas. The goal was to prepare the dataset for further analysis and reporting by handling missing values, standardizing column names, and creating meaningful derived columns.

## Tools & Technologies Used
- Python
- Pandas
-  VS Code

## Data Cleaning & Transformation Performed
- Loaded raw CSV dataset using Pandas
- Handled missing values in `Review Rating` using median values grouped by product category
- Standardized column names by:
  - converting to lowercase
  - replacing spaces with underscores
- Renamed complex column names for better readability
- Created customer age groups using `qcut()`
- Created a new feature to track purchase frequency in days using mapping logic
- Performed null-value validation checks after cleaning

## Key Concepts Used
- Pandas DataFrames
- GroupBy & Transform
- Lambda Functions
- Feature Engineering
- Data Cleaning
- Data Transformation

## Files Included
- Raw Dataset (`customer_shopping_behavior.csv`)
- Python Cleaning Script
- Processed Dataset (optional)

## Objective
The objective of this project was to simulate a real-world data preprocessing workflow and prepare clean, analysis-ready data for visualization and business insights generation.
