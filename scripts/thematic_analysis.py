import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

# ---------------------------------------------------
# Load dataset
# ---------------------------------------------------

df = pd.read_csv("data/processed/reviews_with_sentiment.csv")

print("Dataset loaded successfully.")
print(df.shape)

# ---------------------------------------------------
# Load spaCy model
# ---------------------------------------------------

nlp = spacy.load("en_core_web_sm")

# ---------------------------------------------------
# Text preprocessing function
# ---------------------------------------------------

def preprocess_text(text):

    doc = nlp(str(text).lower())

    tokens = []

    for token in doc:

        if (
            not token.is_stop
            and not token.is_punct
            and not token.is_space
            and len(token.text) > 2
        ):
            tokens.append(token.lemma_)

    return " ".join(tokens)

# ---------------------------------------------------
# Clean review text
# ---------------------------------------------------

print("\nPreprocessing review text...")

df["clean_review"] = df["review"].apply(preprocess_text)

# ---------------------------------------------------
# TF-IDF keyword extraction
# ---------------------------------------------------

print("\nExtracting keywords using TF-IDF...")

vectorizer = TfidfVectorizer(
    max_features=100,
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(df["clean_review"])

keywords = vectorizer.get_feature_names_out()

# ---------------------------------------------------
# Print top keywords
# ---------------------------------------------------

print("\nTop Keywords:\n")

for keyword in keywords[:50]:
    print(keyword)

# ---------------------------------------------------
# Theme Mapping Function
# ---------------------------------------------------

def identify_theme(review):

    review = review.lower()

    # Login Issues
    if any(word in review for word in [
        "login", "password", "signin", "sign"
    ]):
        return "Account Access Issues"

    # Transfer Problems
    elif any(word in review for word in [
        "transfer", "transaction", "send money"
    ]):
        return "Transaction Performance"

    # OTP Problems
    elif any(word in review for word in [
        "otp", "code", "verification"
    ]):
        return "OTP & Verification Issues"

    # Performance Problems
    elif any(word in review for word in [
        "crash", "slow", "freeze", "loading"
    ]):
        return "App Performance"

    # UI Feedback
    elif any(word in review for word in [
        "ui", "design", "interface", "easy"
    ]):
        return "UI & User Experience"

    # Feature Requests
    elif any(word in review for word in [
        "fingerprint", "feature", "update"
    ]):
        return "Feature Requests"

    else:
        return "Other"

# ---------------------------------------------------
# Apply theme classification
# ---------------------------------------------------

print("\nIdentifying themes...")

df["identified_theme"] = df["review"].apply(identify_theme)

# ---------------------------------------------------
# Theme Distribution
# ---------------------------------------------------

print("\nTheme Distribution:\n")

print(df["identified_theme"].value_counts())

# ---------------------------------------------------
# Save final dataset
# ---------------------------------------------------

output_path = "data/processed/final_thematic_dataset.csv"

df.to_csv(output_path, index=False)

print(f"\nFinal dataset saved to: {output_path}")