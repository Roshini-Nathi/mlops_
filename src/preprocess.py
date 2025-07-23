import pandas as pd
import os

def clean_data():
    # Load the raw data using tab delimiter
    try:
        df = pd.read_csv("data/raw/students.csv", delimiter="\t")
        print(f"✅ Raw columns: {list(df.columns)}")
    except FileNotFoundError:
        print("❌ File not found: data/raw/students.csv")
        return None
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return None

    # Drop missing values
    df.dropna(inplace=True)

    # Encode 'gender' column
    if "gender" in df.columns:
        df["gender"] = df["gender"].map({"Male": 1, "Female": 0})
    else:
        print("❌ 'gender' column not found in data!")
        return None

    # Save cleaned data
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/cleaned.csv", index=False)
    print("✅ Cleaned data saved to data/processed/cleaned.csv")

    return df