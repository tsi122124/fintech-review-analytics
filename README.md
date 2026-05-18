# Fintech Review Analytics

## Project Overview

This project analyzes Google Play Store reviews from Ethiopian banking applications to uncover customer sentiment, recurring issues, and opportunities for product improvement.

Banks analyzed:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

---

# Task 1: Data Collection and Preprocessing

## Objective

Collect and preprocess mobile banking application reviews into a clean dataset ready for NLP and analytics workflows.

---

# Data Collection Methodology

Reviews were scraped using the Python library:

- google-play-scraper

Source:

- Google Play Store

Fields collected:

- Review text
- Rating (1–5)
- Review date
- Bank name
- Source

---

# Reviews Collected

| Bank   | Reviews |
| ------ | ------- |
| CBE    | 608     |
| BOA    | 613     |
| Dashen | 617     |

Total cleaned reviews:

- 1838

---

# Preprocessing Steps

The following preprocessing operations were performed:

- Removed duplicate reviews
- Removed rows with missing review text or ratings
- Standardized dates to YYYY-MM-DD format
- Retained only required columns

Final dataset columns:

- review
- rating
- date
- bank
- source

---

# Task 2: Sentiment and Thematic Analysis

## Objective

Analyze customer sentiment and identify recurring themes from Ethiopian banking app reviews using NLP techniques.

---

# Sentiment Analysis

The project uses the transformer model:

- distilbert-base-uncased-finetuned-sst-2-english

The model classifies reviews into:

- POSITIVE
- NEGATIVE
- NEUTRAL

Each review also receives a confidence score.

---

# NLP Preprocessing

The following preprocessing steps were applied:

- Lowercasing
- Tokenization
- Stopword removal
- Lemmatization
- Punctuation removal

Libraries used:

- spaCy
- scikit-learn

---

# Thematic Analysis

TF-IDF and keyword matching were used to identify recurring business themes.

Themes identified include:

Other 1368
Transaction Performance 119
UI & User Experience 119
Feature Requests 91
App Performance 70
Account Access Issues 56
OTP & Verification Issues 15

---

# Outputs Generated

Generated datasets:

- reviews_with_sentiment.csv
- final_thematic_dataset.csv

# Project Structure

```text
fintech-review-analytics/
│
├── data/
├── notebooks/
├── scripts/
├── src/
├── tests/
├── .github/workflows/
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Limitations

- Google Play may limit accessible review history
- Reviews may contain emotional or biased language
- Reviews are primarily English-language reviews
- Duplicate reviews may exist before preprocessing
