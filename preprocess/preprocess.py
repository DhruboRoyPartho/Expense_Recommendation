import pandas as pd

def preprocess_data(path):
    df = pd.read_csv(path, parse_dates=['date'])
    df['month'] = df['date'].dt.to_period('M')
    monthly_data = df.groupby(['user_id', 'month', 'category']).agg({'amount': 'sum'}).reset_index()
    pivot = monthly_data.pivot_table(index=['user_id', 'month'], columns='category', values='amount', fill_value=0)
    pivot['total_expense'] = pivot.sum(axis=1)
    return pivot.reset_index()