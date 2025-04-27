import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

def train_model(df):
    df = df.sort_values(['user_id', 'month'])
    X, y = [], []

    for _, user_df in df.groupby('user_id'):
        expenses = user_df['total_expense'].tolist()
        for i in range(len(expenses) - 1):
            X.append([expenses[i]])  # previous month
            y.append(expenses[i + 1])  # next month

    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, 'models/expense_model.pkl')
    print("Model trained and saved.")
