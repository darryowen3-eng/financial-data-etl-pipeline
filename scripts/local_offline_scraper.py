import pandas as pd
import random
from datetime import datetime, timedelta

def generate_local_chaos(rows_count=500):
    currencies = ["USD", "ZMW", "EUR", "GBP", "ZAR", "INR", "CNY"]
    chaotic_dates = ["%d/%m/%Y", "%Y-%m-%d", "%B %d, %Y", "%m-%d-%y", "Timestamp: %Y%m%d"]
    null_variants = ["", "N/A", "NULL", "NaN", "None", "  "]
    
    dataset = []
    start_date = datetime(2026, 1, 1)

    for i in range(rows_count):
        # 1. Date Format Mayhem
        random_days = random.randint(0, 180)
        current_date = start_date + timedelta(days=random_days)
        
        dice_roll = random.random()
        if dice_roll < 0.10:
            date_str = random.choice(null_variants)
        elif dice_roll < 0.20:
            date_str = "00/00/0000"
        else:
            date_str = current_date.strftime(random.choice(chaotic_dates))

        # 2. String Font and Spacing Chaos
        base_curr = random.choice(currencies)
        spatial_chaos = random.choice(["   ", "", "\t", " \n "])
        case_chaos = random.choice([str.upper, str.lower, str.title])
        
        if random.random() < 0.08:
            currency = random.choice(null_variants)
        else:
            currency = f"{spatial_chaos}{case_chaos(base_curr)}{spatial_chaos}"

        # 3. Numeric Breakdown (Negatives & Text Mixed In)
        rate_val = random.uniform(1.5, 27.5)
        rate_dice = random.random()
        
        if rate_dice < 0.12:
            rate = f"-{rate_val:.4f}" # Impossible negative currency values
        elif rate_dice < 0.22:
            rate = random.choice(null_variants) # Missing entry cells
        elif rate_dice < 0.32:
            rate = f"{rate_val:.2f} ZMW/USD" # Numbers bound to text strings
        else:
            rate = f"   {rate_val:.4f}   " # Excessively padded floats

        dataset.append({
            "Transaction_Date": date_str,
            "Currency_Code": currency,
            "Exchange_Rate": rate
        })

    return dataset

if __name__ == "__main__":
    print("Generating local chaotic data...")
    chaos_data = generate_local_chaos(1000) # Creates 1000 messy rows instantly
    
    df = pd.DataFrame(chaos_data)
    df.to_csv("perfect_local_disaster.csv", index=False)
    print("Successfully saved 1000 messy rows to 'perfect_local_disaster.csv'!")

