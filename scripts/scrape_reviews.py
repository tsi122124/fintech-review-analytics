from google_play_scraper import reviews, Sort
import pandas as pd

# Ethiopian Banking Apps
apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank, app_id in apps.items():

    print(f"Scraping reviews for {bank}...")

    result, _ = reviews(
        app_id,
        lang="en",
        country="et",
        sort=Sort.NEWEST,
        count=800
    )

    print(f"Collected {len(result)} reviews for {bank}")

    for review in result:
        all_reviews.append({
            "review": review["content"],
            "rating": review["score"],
            "date": review["at"],
            "bank": bank,
            "source": "Google Play"
        })

# Convert to DataFrame
df = pd.DataFrame(all_reviews)

print("\nDataset Preview:")
print(df.head())

print(f"\nTotal Reviews Collected: {len(df)}")

# Save raw dataset
df.to_csv("data/raw/bank_reviews_raw.csv", index=False)

print("\nRaw dataset saved successfully.")