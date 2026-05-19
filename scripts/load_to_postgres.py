import pandas as pd
from sqlalchemy import create_engine

# ---------------------------------------------------
# PostgreSQL Connection Configuration
# ---------------------------------------------------

username = "postgres"
password = "1221"
host = "localhost"
port = "5432"
database = "bank_reviews"

# ---------------------------------------------------
# Create Database Engine
# ---------------------------------------------------

engine = create_engine(
    f"postgresql://{username}:{password}@{host}:{port}/{database}"
)

# ---------------------------------------------------
# Load Final Processed Dataset
# ---------------------------------------------------

df = pd.read_csv(
    "data/processed/final_thematic_dataset.csv"
)

print("Dataset loaded successfully!")
print(df.shape)

# ---------------------------------------------------
# Create Banks DataFrame
# ---------------------------------------------------

banks_df = pd.DataFrame({
    "bank_name": [
        "Commercial Bank of Ethiopia",
        "Bank of Abyssinia",
        "Dashen Bank"
    ],
    "app_name": [
        "CBE Mobile Banking",
        "BOA Mobile Banking",
        "Dashen Super App"
    ]
})

# ---------------------------------------------------
# Insert Banks Table
# ---------------------------------------------------

banks_df.to_sql(
    "banks",
    engine,
    if_exists="append",
    index=False
)

print("Banks table inserted!")

# ---------------------------------------------------
# Create Bank ID Mapping
# ---------------------------------------------------

bank_mapping = {
    "CBE": 1,
    "BOA": 2,
    "Dashen": 3
}

df["bank_id"] = df["bank"].map(bank_mapping)

# ---------------------------------------------------
# Select Needed Columns
# ---------------------------------------------------

reviews_df = df[
    [
        "bank_id",
        "review",
        "rating",
        "date",
        "sentiment_label",
        "sentiment_score",
        "identified_theme",
        "source"
    ]
].copy()

# ---------------------------------------------------
# Rename Columns to Match SQL Schema
# ---------------------------------------------------

reviews_df.columns = [
    "bank_id",
    "review_text",
    "rating",
    "review_date",
    "sentiment_label",
    "sentiment_score",
    "identified_theme",
    "source"
]

# ---------------------------------------------------
# Insert Reviews Table
# ---------------------------------------------------

reviews_df.to_sql(
    "reviews",
    engine,
    if_exists="append",
    index=False
)

print("Reviews inserted successfully!")
print("Database loading complete!")