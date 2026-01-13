import pandas as pd
import random

reviews = [
    "Excellent product, highly recommended!",
    "Worst purchase ever, don’t buy!",
    "Great value for money.",
    "Amazing product!!! Love it.",
    "Good quality, will buy again.",
    "Fake product, not as described.",
    "Very bad experience, disappointed.",
    "Awesome product, works perfectly.",
    "Terrible, waste of money.",
    "Perfect item, fast delivery."
]

data = []
for i in range(20):
    review = random.choice(reviews)
    label = random.choice([0, 1])  # 0 - Genuine, 1 - Fake
    data.append([i, review, label])

df = pd.DataFrame(data, columns=["ReviewID", "ReviewText", "Fake"])
df.to_csv("reviews.csv", index=False)
print("Dataset created successfully!")
