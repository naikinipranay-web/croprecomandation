import pandas as pd
import numpy as np
import os

# Create data folder if not exists
os.makedirs("data", exist_ok=True)

np.random.seed(42)  # fixed dataset every time

# Crop base values (20 crops)
crops = {
    "rice": (90,40,40,25,85,6.5,220),
    "maize": (22,32,18,28,65,6.5,100),
    "chickpea": (40,60,75,19,58,7.5,70),
    "mungbean": (12,26,17,29,75,6.3,110),
    "banana": (100,55,50,27,88,6.2,215),
    "apple": (30,42,46,22,70,6.7,160),
    "cotton": (82,40,41,30,73,6.4,180),
    "coffee": (60,32,30,26,62,5.7,145),
    "mango": (35,45,50,27,70,6.5,200),
    "orange": (40,50,45,26,68,6.0,170),
    "papaya": (50,60,55,28,75,6.3,210),
    "grapes": (30,38,35,24,65,6.8,90),
    "watermelon": (28,42,30,29,72,6.2,95),
    "muskmelon": (32,48,35,28,70,6.4,100),
    "pomegranate": (45,55,40,26,60,6.5,150),
    "lentil": (35,58,70,20,55,7.2,65),
    "blackgram": (18,30,20,30,80,6.4,120),
    "pigeonpeas": (25,45,25,27,68,6.6,130),
    "kidneybeans": (30,50,30,22,60,6.8,85),
    "coconut": (80,95,60,28,90,5.8,250)
}

rows = []
rows_per_crop = 250  # 20 crops × 250 = 5000 rows

for crop, base in crops.items():
    for _ in range(rows_per_crop):
        N = round(np.random.normal(base[0], 5),2)
        P = round(np.random.normal(base[1], 5),2)
        K = round(np.random.normal(base[2], 5),2)
        temp = round(np.random.normal(base[3], 2),2)
        humidity = round(np.random.normal(base[4], 3),2)
        ph = round(np.random.normal(base[5], 0.3),2)
        rainfall = round(np.random.normal(base[6], 15),2)

        rows.append([N,P,K,temp,humidity,ph,rainfall,crop])

df = pd.DataFrame(rows, columns=[
    "N","P","K","temperature","humidity","ph","rainfall","label"
])

df.to_csv("data/crop_recommendation_5000.csv", index=False)

print("✅ 5000 rows dataset saved in data/crop_recommendation_5000.csv")