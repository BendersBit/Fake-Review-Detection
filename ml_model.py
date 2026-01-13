import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv("reviews.csv")

# Spliting DataFrame before vectorizing bcs (this preserves correct indices)
df_train, df_test = train_test_split(df, test_size=0.3, random_state=42)

vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(df_train["ReviewText"])
X_test = vectorizer.transform(df_test["ReviewText"])
y_train = df_train["Fake"]
y_test = df_test["Fake"]

model = MultinomialNB()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

# Adding results to test set, then combine all rows
df_test = df_test.copy()
df_test["Predicted"] = predictions

df_with_predictions = pd.concat([df_train, df_test])
df_with_predictions.to_csv("reviews_with_predictions.csv", index=False)

print("Fake review detection completed!")
