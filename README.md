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
