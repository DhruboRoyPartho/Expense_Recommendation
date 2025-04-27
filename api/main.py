# Method: POST
# Route: localhost:8000/recommend and body will be { "user_id": 1 }
# Run: uvicorn api.main:app --reload

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from preprocess.preprocess import preprocess_data
from models.train_model import train_model
from recommend.recommender import predict_next_expense, generate_recommendation
import pandas as pd
import json

app = FastAPI()

# Loading and preprocessing data once when app starts
df = preprocess_data('data/transactions.csv')
train_model(df)

# Pydantic model for request
class UserRequest(BaseModel):
    user_id: int

@app.post("/recommend")
def get_recommendation(user: UserRequest):
    user_data = df[df['user_id'] == user.user_id]
    if user_data.empty:
        raise HTTPException(status_code=404, detail="User not found")

    latest = user_data.sort_values('month').iloc[-1]
    latest_expense = latest['total_expense']
    
    predicted = predict_next_expense(latest_expense)
    recommendation = generate_recommendation(latest_expense, predicted)

    # Saving output (Optional)
    with open("output/results.json", "w") as f:
        json.dump(recommendation, f, indent=4)

    return recommendation
