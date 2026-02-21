import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Create models folder if not exists
if not os.path.exists("models"):
    os.makedirs("models")

# Load dataset
data = pd.read_csv("dataset/data/crop_recommendation_5000.csv")

X = data.drop("label", axis=1)
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

pickle.dump(model, open("models/crop_model.pkl", "wb"))

print("Model trained and saved successfully!")