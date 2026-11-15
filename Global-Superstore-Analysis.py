
import pandas as pd

file_path = r"C:\Users\SANDRA SAJI\OneDrive\Desktop\Luminar\Data Analytics\global_superstore.xlsx"

df = pd.read_excel(file_path, engine="openpyxl")

print("Excel file loaded successfully!")
print(df.head())
print("Dataset Shape:", df.shape)

# ==========================================
# STEP 2: DATA CLEANING AND PREPROCESSING
# ==========================================

# Create a copy of the original dataset
df_clean = df.copy()

print("\n========== DATA CLEANING ==========")

# 1. Check duplicate records
duplicate_count = df_clean.duplicated().sum()

print("Duplicate rows:", duplicate_count)

# Remove duplicate records
df_clean = df_clean.drop_duplicates()

# 2. Remove unnecessary spaces from text columns
text_columns = df_clean.select_dtypes(
    include=["object", "str"]
).columns

for col in text_columns:
    df_clean[col] = df_clean[col].str.strip()

# 3. Convert date columns into datetime format
df_clean["Order Date"] = pd.to_datetime(
    df_clean["Order Date"], errors="coerce"
)

df_clean["Ship Date"] = pd.to_datetime(
    df_clean["Ship Date"], errors="coerce"
)

# 4. Convert numeric columns
numeric_columns = [
    "Sales",
    "Quantity",
    "Discount",
    "Profit",
    "Shipping Cost"
]

for col in numeric_columns:
    df_clean[col] = pd.to_numeric(
        df_clean[col], errors="coerce"
    )

# 5. Check missing values
print("\nMissing Values Before Handling:")
print(df_clean.isnull().sum())

# 6. Handle missing Postal Code values
# Keep missing postal codes because they may be unavailable
# for certain countries.

df_clean["Postal Code"] = df_clean["Postal Code"].fillna(
    0
)

# 7. Check missing values after handling
print("\nMissing Values After Handling:")
print(df_clean.isnull().sum())

# 8. Check cleaned dataset information
print("\n========== CLEANED DATASET ==========")

print("Total Rows:", df_clean.shape[0])
print("Total Columns:", df_clean.shape[1])

print("\nDataset Information:")
df_clean.info()

# 9. Display first five records
print("\nFirst 5 Cleaned Records:")
print(df_clean.head())

# 10. Save cleaned dataset
df_clean.to_csv(
    "global_superstore_cleaned.csv",
    index=False
)

df_clean.to_excel(
    "global_superstore_cleaned.xlsx",
    index=False
)

print("\nCleaned dataset saved successfully!")
