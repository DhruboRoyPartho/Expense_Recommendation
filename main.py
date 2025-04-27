from preprocess.preprocess import preprocess_data
from models.train_model import train_model
from recommend.recommender import predict_next_expense, generate_recommendation
import pandas as pd
import json

# Load and preprocess data
df = preprocess_data('data/transactions.csv')

# Train model
train_model(df)

# Predict for last month of user_id
# Example: user 10 = increasing.
# Example: user 5 = great.
user_id = 11
latest = df[df['user_id'] == user_id].sort_values('month').iloc[-1]
latest_expense = latest['total_expense']

predicted = predict_next_expense(latest_expense)
recommendation = generate_recommendation(latest_expense, predicted)

# Save output
with open("output/results.json", "w") as f:
    json.dump(recommendation, f, indent=4)

print("Recommendation generated:")
print(json.dumps(recommendation, indent=4))
