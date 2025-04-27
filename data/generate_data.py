import random
import pandas as pd
from datetime import datetime, timedelta

CATEGORIES = ['Grocery', 'Rent', 'Dining', 'Transport', 'Entertainment', 'Bills', 'Shopping', 'Travel']
USER_COUNT = 20
MONTHS = 6

def random_date(month_offset):
    start = datetime.today().replace(day=1) - timedelta(days=30 * month_offset)
    end = start.replace(day=28)
    return start + (end - start) * random.random()

def generate_transactions():
    records = []
    for user_id in range(1, USER_COUNT + 1):
        for month in range(MONTHS):
            # Making 15–30 transactions per month
            num_transactions = random.randint(15, 30)
            
            # Generating small and large expenses to stay in range
            total_monthly_expense = 0
            monthly_records = []
            for _ in range(num_transactions):
                date = random_date(month)
                category = random.choice(CATEGORIES)

                # Control amount: mix small and large
                if category == 'Rent':
                    amount = round(random.uniform(5000, 10000), 2)
                else:
                    amount = round(random.uniform(200, 2000), 2)
                
                monthly_records.append([user_id, date.strftime("%Y-%m-%d"), category, amount])
                total_monthly_expense += amount

            # Normalize if over 25k or under 7k
            if total_monthly_expense > 25000 or total_monthly_expense < 7000:
                scale = random.uniform(7000, 25000) / total_monthly_expense
                for rec in monthly_records:
                    rec[3] = round(rec[3] * scale, 2)

            records.extend(monthly_records)
    
    return pd.DataFrame(records, columns=["user_id", "date", "category", "amount"])

if __name__ == "__main__":
    df = generate_transactions()
    df.to_csv("data/transactions.csv", index=False)
    print("Simulated data (10k–25k/month) saved to data/transactions.csv")
