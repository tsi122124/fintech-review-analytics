import pandas as pd
from transformers import pipeline

# --------------------------------------------
# Load cleaned dataset
# --------------------------------------------

df = pd.read_csv("data/processed/bank_reviews_clean.csv")

print("Dataset Loaded Successfully")
print(df.shape)

# --------------------------------------------
# Load sentiment analysis pipeline
# --------------------------------------------

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

print("\nModel Loaded Successfully")

# --------------------------------------------
# Function for sentiment classification
# --------------------------------------------

def analyze_sentiment(review):

    try:
        result = classifier(review[:512])[0]

        label = result["label"]
        score = result["score"]

        # Add neutral category manually
        if score < 0.60:
            label = "NEUTRAL"

        return pd.Series([label, score])

    except Exception:
        return pd.Series(["UNKNOWN", 0])

# --------------------------------------------
# Apply sentiment analysis
# --------------------------------------------

print("\nRunning sentiment analysis...")

df[["sentiment_label", "sentiment_score"]] = df["review"].apply(analyze_sentiment)

# --------------------------------------------
# Save results
# --------------------------------------------

output_path = "data/processed/reviews_with_sentiment.csv"

df.to_csv(output_path, index=False)

print("\nSentiment analysis completed successfully.")

print("\nSentiment Distribution:")
print(df["sentiment_label"].value_counts())

print(f"\nFile saved to: {output_path}")