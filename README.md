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
├── report/
├── scripts/
├── src/
├── tests/
├── .github/workflows/
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Task 3: PostgreSQL Database Engineering

## Objective

Design and implement a relational PostgreSQL database to persistently store cleaned and processed banking app review data.

---

# Database Setup

Database used:

- PostgreSQL 18

Database name:

- bank_reviews

Administration tool:

- pgAdmin 4

---

# Database Schema

Two relational tables were created:

## 1. banks

Stores metadata about each banking application.

| Column Name | Description             |
| ----------- | ----------------------- |
| bank_id     | Primary Key             |
| bank_name   | Bank name               |
| app_name    | Mobile application name |

---

## 2. reviews

Stores processed review and sentiment data.

| Column Name      | Description                   |
| ---------------- | ----------------------------- |
| review_id        | Primary Key                   |
| bank_id          | Foreign Key referencing banks |
| review_text      | Customer review text          |
| rating           | Review rating (1–5)           |
| review_date      | Date of review                |
| sentiment_label  | Sentiment classification      |
| sentiment_score  | Model confidence score        |
| identified_theme | Extracted business theme      |
| source           | Review source                 |

---

# SQL Schema File

Database schema implementation:

```text
scripts/schema.sql
```

---

# Data Insertion Pipeline

Processed review data was inserted into PostgreSQL using:

```text
scripts/load_to_postgres.py
```

Libraries used:

- SQLAlchemy
- psycopg2-binary

---

# Verification Queries

The following validation checks were performed successfully:

## Total Reviews Verification

Verified that all processed reviews were inserted into the database.

Result:

- 1838 reviews inserted successfully.

---

## Reviews Per Bank

| Bank   | Reviews |
| ------ | ------- |
| CBE    | 608     |
| BOA    | 613     |
| Dashen | 617     |

---

## Average Rating Per Bank

Average ratings were computed directly from PostgreSQL using SQL aggregation queries.

---

## Null Value Checks

Verified that critical columns such as review_text and rating contain no missing values.

Result:

- 0 missing critical values detected.

---

# Verification Screenshots

Screenshots of PostgreSQL schema creation and query verification are available in:

```text
reports/screenshots/
```

---

# Task 4: Insights and Recommendations

## Objective

Generate business-actionable insights from customer reviews to help Ethiopian banks improve mobile banking services, customer retention, and competitive positioning.

---

# Early Business Insights

## Common Customer Satisfaction Drivers

- Easy account access
- Fast digital transactions
- Convenient mobile banking experience

---

## Common Customer Pain Points

- Slow transfer processing
- Login and OTP verification failures
- App crashes and performance instability

---

# Planned Visualizations

The final analysis includes:

- Sentiment distribution by bank
- Rating distribution analysis
- Theme frequency analysis
- Theme comparison across banks
- Sentiment trend analysis over time

---

# Ethical Considerations

Potential biases in the review dataset include:

- Negativity bias from dissatisfied users
- Sampling bias from Google Play-only reviews
- Limited multilingual review representation
- Possible temporal bias due to review availability limitations

---

# Future Improvements

Potential future enhancements include:

- Multilingual sentiment analysis
- Advanced topic modeling using LDA
- Real-time review monitoring pipeline
- AI-powered customer complaint classification
- Dashboard deployment for stakeholders
