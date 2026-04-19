import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# LOAD DATA
# -----------------------------

df = pd.read_csv("data/poll_data.csv")

# -----------------------------
# CREATE OUTPUT DIRECTORY
# -----------------------------

output_dir = "outputs/charts"
os.makedirs(output_dir, exist_ok=True)

# -----------------------------
# REUSABLE SAVE FUNCTION
# -----------------------------

def save_plot(filename):
    path = os.path.join(output_dir, filename)
    plt.savefig(path, bbox_inches="tight")
    print(f"Saved: {path}")

# -----------------------------
# 1. VOTE DISTRIBUTION (BAR CHART)
# -----------------------------

plt.figure(figsize=(6, 4))

vote_counts = df["option_selected"].value_counts()

sns.barplot(x=vote_counts.index, y=vote_counts.values)

plt.title("Poll Results - Vote Count")
plt.xlabel("Options")
plt.ylabel("Votes")

save_plot("vote_bar_chart.png")
plt.show()

# -----------------------------
# 2. PIE CHART (DISTRIBUTION)
# -----------------------------

plt.figure(figsize=(6, 6))

plt.pie(
    vote_counts.values,
    labels=vote_counts.index,
    autopct="%1.1f%%"
)

plt.title("Poll Distribution")

save_plot("vote_pie_chart.png")
plt.show()

# -----------------------------
# 3. REGION-WISE ANALYSIS (STACKED BAR)
# -----------------------------

region_data = pd.crosstab(df["region"], df["option_selected"])

region_data.plot(kind="bar", stacked=True, figsize=(8, 5))

plt.title("Region-wise Voting Pattern")
plt.xlabel("Region")
plt.ylabel("Votes")

save_plot("region_stacked_chart.png")
plt.show()

# -----------------------------
# 4. AGE GROUP ANALYSIS
# -----------------------------

plt.figure(figsize=(7, 4))

age_data = pd.crosstab(df["age_group"], df["option_selected"])

age_data.plot(kind="bar")

plt.title("Age Group vs Voting Preference")

save_plot("age_group_chart.png")
plt.show()

# -----------------------------
# 5. TIME TREND (OPTIONAL INSIGHT)
# -----------------------------

df["timestamp"] = pd.to_datetime(df["timestamp"])
df["date"] = df["timestamp"].dt.date

trend = df.groupby("date")["option_selected"].count()

plt.figure(figsize=(8, 4))
trend.plot()

plt.title("Daily Poll Participation Trend")
plt.xlabel("Date")
plt.ylabel("Responses")

save_plot("trend_chart.png")
plt.show()

# -----------------------------
# FINAL SUMMARY PRINT
# -----------------------------

print("\nAll charts generated and saved successfully.")