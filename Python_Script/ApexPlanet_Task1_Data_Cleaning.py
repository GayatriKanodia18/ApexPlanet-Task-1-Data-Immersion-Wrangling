import pandas as pd

# ============================================================
# APEXPLANET TASK 1 - DATA IMMERSION & WRANGLING
# ============================================================

# -----------------------------
# FILE PATHS
# -----------------------------

input_file = "../Original_Dataset/ApexPlanet_DataAnalytics_Dataset.xlsx"
output_file = "../Cleaned_Dataset/ApexPlanet_Task1_Cleaned_Dataset_Python.xlsx"


# -----------------------------
# LOAD DATASET
# -----------------------------

df = pd.read_excel(input_file)

print("Original dataset shape:", df.shape)


# -----------------------------
# DATA QUALITY CHECK
# -----------------------------

print("\nMissing values before cleaning:")
print(df.isnull().sum())

print("\nCompletely duplicate rows before cleaning:")
print(df.duplicated().sum())


# -----------------------------
# DATA CLEANING
# -----------------------------

# 1. Fill missing Age values with median Age
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)

print("\nMedian Age used for missing values:", median_age)


# 2. Fill missing City values with "Unknown"
df["City"] = df["City"].fillna("Unknown")


# 3. Remove completely duplicate rows
#    Note: Repeated Order_ID values are NOT removed because
#    they represent different transaction records.
df = df.drop_duplicates()


# -----------------------------
# DATA TRANSFORMATION
# -----------------------------

# 4. Standardize Order_Date format
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)

df["Order_Date"] = df["Order_Date"].dt.strftime("%Y-%m-%d")


# 5. Standardize text fields
text_columns = [
    "Gender",
    "City",
    "Product",
    "Category"
]

for column in text_columns:
    df[column] = (
        df[column]
        .astype(str)
        .str.strip()
    )


# 6. Standardize Gender values
df["Gender"] = df["Gender"].str.title()


# -----------------------------
# DATA VALIDATION
# -----------------------------

# Convert numeric columns to numeric data types
df["Age"] = pd.to_numeric(
    df["Age"],
    errors="coerce"
)

df["Quantity"] = pd.to_numeric(
    df["Quantity"],
    errors="coerce"
)

df["Unit_Price"] = pd.to_numeric(
    df["Unit_Price"],
    errors="coerce"
)

df["Total_Sales"] = pd.to_numeric(
    df["Total_Sales"],
    errors="coerce"
)


# -----------------------------
# FEATURE ENGINEERING
# -----------------------------

# Create a new feature showing sales generated per unit
df["Sales_Per_Unit"] = (
    df["Total_Sales"] / df["Quantity"]
)


# -----------------------------
# FINAL DATA VALIDATION
# -----------------------------

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nCompletely duplicate rows after cleaning:")
print(df.duplicated().sum())

print("\nFinal dataset shape:", df.shape)


# -----------------------------
# SAVE FINAL CLEANED DATASET
# -----------------------------

df.to_excel(
    output_file,
    index=False
)

print("\nCleaning and transformation completed successfully.")
print("Output file:", output_file)