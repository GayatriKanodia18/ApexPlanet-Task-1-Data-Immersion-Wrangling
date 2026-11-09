# ApexPlanet Task 1 - Data Immersion & Wrangling

## Project Overview

This project was completed as part of the ApexPlanet internship.

The objective of Task 1 was to perform data immersion, data quality assessment, data cleaning, data transformation, and preparation of an analysis-ready dataset.

## Dataset

The project uses a sales dataset containing customer, product, transaction, and sales information.

### Dataset Variables

The dataset contains the following variables:

- Order_ID
- Order_Date
- Customer_ID
- Customer_Name
- Age
- Gender
- City
- Product
- Category
- Quantity
- Unit_Price
- Total_Sales

## Data Quality Assessment

The following quality checks were performed:

- Missing Age values: 21
- Missing City values: 14
- Repeated Order_ID values: 9
- Completely duplicate rows: 0
- Age below 18: 0
- Age above 100: 0
- Zero Quantity values: 0
- Negative Quantity values: 0
- Zero Unit Price values: 0
- Negative Unit Price values: 0
- Zero Total Sales values: 0
- Negative Total Sales values: 0

Repeated Order_ID values were investigated and retained because they represented different transaction records.

## Data Cleaning

The following cleaning operations were performed:

- Missing Age values were replaced using the median Age of 41.
- Missing City values were replaced with `Unknown`.
- Completely duplicate rows were removed.
- Order dates were standardized to `YYYY-MM-DD`.
- Text fields were trimmed to remove unnecessary spaces.
- Gender values were standardized.
- Numeric columns were converted to appropriate numeric data types.

## Data Transformation

A new feature was created:

- `Sales_Per_Unit` = `Total_Sales / Quantity`

The final Python-cleaned dataset contains 1,000 rows and 13 columns.

## Python Implementation

Python and Pandas were used for data cleaning and transformation.

The Python script is available in:

`Python_Script/ApexPlanet_Task1_Data_Cleaning.py`

## Project Structure

```text
ApexPlanet-Task-1-Data-Immersion-Wrangling
│
├── Cleaned_Dataset
│   ├── ApexPlanet_Task1_Cleaned_Dataset.xlsx
│   └── ApexPlanet_Task1_Cleaned_Dataset_Python.xlsx
│
├── Data_Dictionary
│   └── ApexPlanet_Task1_Data_Dictionary.xlsx
│
├── Documentation
│   ├── ApexPlanet_Task1_Cleaning_Transformation_Log.xlsx
│   ├── ApexPlanet_Task1_Data_Immersion_Wrangling_Documentation.docx
│   └── ApexPlanet_Task1_Data_Quality_Assessment.xlsx
│
├── Original_Dataset
│   └── ApexPlanet_DataAnalytics_Dataset.xlsx
│
└── Python_Script
    └── ApexPlanet_Task1_Data_Cleaning.py
