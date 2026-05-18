import pandas as pd

# Load raw dataset
df = pd.read_csv("data/raw/bank_reviews_raw.csv")

print("Initial Dataset Shape:", df.shape)

# ---------------------------------------------------
# Remove duplicate reviews
# ---------------------------------------------------

before_duplicates = len(df)

df = df.drop_duplicates(subset=["review"])

after_duplicates = len(df)

duplicates_removed = before_duplicates - after_duplicates

print(f"Duplicate reviews removed: {duplicates_removed}")

# ---------------------------------------------------
# Remove missing values
# ---------------------------------------------------

before_missing = len(df)

df = df.dropna(subset=["review", "rating"])

after_missing = len(df)

missing_removed = before_missing - after_missing

print(f"Rows with missing values removed: {missing_removed}")

# ---------------------------------------------------
# Normalize date format
# ---------------------------------------------------

df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

# ---------------------------------------------------
# Keep only required columns
# ---------------------------------------------------

df = df[["review", "rating", "date", "bank", "source"]]

print("\nFinal Dataset Shape:", df.shape)

print("\nDataset Preview:")
print(df.head())

# ---------------------------------------------------
# Save cleaned dataset
# ---------------------------------------------------

df.to_csv("data/processed/bank_reviews_clean.csv", index=False)

print("\nCleaned dataset saved successfully.")