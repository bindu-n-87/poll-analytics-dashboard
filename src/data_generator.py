import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)

NUM_RESPONDENTS = 1000

age_groups = ["18-25", "26-35", "36-50", "50+"]
genders = ["Male", "Female", "Other"]
regions = ["North", "South", "East", "West"]
education = ["School", "Graduate", "Postgraduate"]
device = ["Mobile", "Desktop"]

questions = {
    "Q1": "Which product do you prefer?",
    "Q2": "Which feature matters most?"
}

options_q1 = ["Product A", "Product B", "Product C"]
options_q2 = ["Price", "Quality", "Brand"]


def choose_option(age, region, question_id):
    if question_id == "Q1":
        if age == "18-25":
            return np.random.choice(options_q1, p=[0.6, 0.3, 0.1])
        elif age == "26-35":
            return np.random.choice(options_q1, p=[0.4, 0.4, 0.2])
        elif age == "36-50":
            return np.random.choice(options_q1, p=[0.2, 0.5, 0.3])
        else:
            return np.random.choice(options_q1, p=[0.1, 0.3, 0.6])

    else:
        if region == "North":
            return np.random.choice(options_q2, p=[0.5, 0.3, 0.2])
        elif region == "South":
            return np.random.choice(options_q2, p=[0.3, 0.5, 0.2])
        elif region == "East":
            return np.random.choice(options_q2, p=[0.2, 0.4, 0.4])
        else:
            return np.random.choice(options_q2, p=[0.4, 0.3, 0.3])

def random_date():
    start = datetime(2025, 1, 1)
    end = datetime(2025, 4, 1)
    return start + timedelta(days=random.randint(0, (end - start).days))


data = []

for i in range(1, NUM_RESPONDENTS + 1):

    age = np.random.choice(age_groups)
    gender = np.random.choice(genders)
    region = np.random.choice(regions)
    edu = np.random.choice(education)
    dev = np.random.choice(device)

    for qid, qtext in questions.items():

        data.append({
            "respondent_id": i,
            "age_group": age,
            "gender": gender,
            "region": region,
            "education": edu,
            "device_type": dev,
            "question_id": qid,
            "question": qtext,
            "option_selected": choose_option(age, region, qid),
            "timestamp": random_date()
        })


df = pd.DataFrame(data)


df.to_csv("data/poll_data.csv", index=False)

print("Dataset generated successfully!")
print(df.head())
