import pandas as pd

# -----------------------------
# LOAD DATA
# -----------------------------

df = pd.read_csv("data/poll_data.csv")

# -----------------------------
# BASIC ANALYSIS
# -----------------------------

vote_counts = df["option_selected"].value_counts()
vote_percent = df["option_selected"].value_counts(normalize=True) * 100

top_option = vote_counts.idxmax()

region_pref = df.groupby(["region", "option_selected"]).size().unstack()

age_pref = df.groupby(["age_group", "option_selected"]).size().unstack()

# -----------------------------
# INSIGHT GENERATION
# -----------------------------

print("\n==============================")
print("POLL RESULTS ANALYSIS REPORT")
print("==============================\n")

print("1. OVERALL WINNER")
print("------------------")
print("Most preferred option:", top_option)
print("\nVote distribution:")
print(vote_percent.round(2))

print("\n2. DEMOGRAPHIC INSIGHTS")
print("------------------------")

print("\nRegion-wise behavior:")
print(region_pref)

print("\nAge group behavior:")
print(age_pref)

print("\n3. KEY INSIGHTS")
print("----------------")

if vote_percent.max() > 50:
    print("- Clear majority preference observed.")
else:
    print("- No strong majority, competitive distribution.")

if "18-25" in df["age_group"].value_counts().index:
    print("- Young users are highly active in the poll.")

if "Desktop" in df.columns:
    print("- Device-based segmentation available for deeper analysis.")

print("\n4. BUSINESS INTERPRETATION")
print("---------------------------")
print("- Product strategy should focus on top option.")
print("- Marketing can be targeted based on region behavior.")
print("- Age-based segmentation can improve personalization.")

print("\n==============================")
print("END OF REPORT")
print("==============================")