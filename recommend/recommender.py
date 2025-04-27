import joblib

def predict_next_expense(latest_expense):
    model = joblib.load('models/expense_model.pkl')
    prediction = model.predict([[latest_expense]])[0]
    return round(prediction, 2)

def generate_recommendation(latest_expense, predicted):
    savings_tip = ""
    diff = predicted - latest_expense

    if diff > 0:
        savings_tip = f"Your expense might increase by {round(diff, 2)}. Try reducing costs in dining or shopping."
    else:
        savings_tip = "Great! Your expenses are expected to reduce. Keep saving!"

    budget_recommendation = {
        "Grocery": round(predicted * 0.15, 2),
        "Rent": round(predicted * 0.35, 2),
        "Dining": round(predicted * 0.10, 2),
        "Entertainment": round(predicted * 0.10, 2),
        "Savings": round(predicted * 0.30, 2),
    }

    return {
        "latest_total_expense": round(latest_expense, 2),
        "predicted_expense": predicted,
        "savings_tip": savings_tip,
        "recommended_budget": budget_recommendation
    }

