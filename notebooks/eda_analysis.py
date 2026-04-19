import pandas as pd
import numpy as np

df = pd.read_csv("data/poll_data.csv")

print("Dataset Shape:", df.shape)
print("\nFirst 5 rows:\n", df.head())

print("\nMissing Values:\n", df.isnull().sum())

df.drop_duplicates(inplace=True)

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

print("\nData Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe(include="all"))

vote_counts = df["option_selected"].value_counts()
vote_percent = df["option_selected"].value_counts(normalize=True) * 100

summary = pd.DataFrame({
    "Votes": vote_counts,
    "Percentage": vote_percent
})

print("\nVote Distribution:\n", summary)

print("\nAge Group Distribution:\n", df["age_group"].value_counts())
print("\nRegion Distribution:\n", df["region"].value_counts())
print("\nGender Distribution:\n", df["gender"].value_counts())

age_vs_vote = pd.crosstab(df["age_group"], df["option_selected"])
region_vs_vote = pd.crosstab(df["region"], df["option_selected"])
edu_vs_vote = pd.crosstab(df["education"], df["option_selected"])

print("\nAge vs Vote:\n", age_vs_vote)
print("\nRegion vs Vote:\n", region_vs_vote)
print("\nEducation vs Vote:\n", edu_vs_vote)

df["date"] = df["timestamp"].dt.date
daily_trend = df.groupby("date")["option_selected"].count()

print("\nDaily Response Trend:\n", daily_trend.head())

top_option = vote_counts.idxmax()
most_active_region = df["region"].value_counts().idxmax()
most_active_age = df["age_group"].value_counts().idxmax()

print("\nFINAL INSIGHTS")
print("----------------------")
print("Most Preferred Option:", top_option)
print("Most Active Region:", most_active_region)
print("Most Active Age Group:", most_active_age)
