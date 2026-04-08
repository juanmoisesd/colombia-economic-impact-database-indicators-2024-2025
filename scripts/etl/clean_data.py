import sys
import pandas as pd
import os

def clean_data(input_file, output_file):
    print(f"Reading {input_file}...")
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found. Creating placeholder.")
        df = pd.DataFrame(columns=["indicator", "value", "year"])
    else:
        df = pd.read_csv(input_file)

    # Perform cleaning transformations here
    print("Cleaning data...")
    df_clean = df.drop_duplicates()

    print(f"Saving to {output_file}...")
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df_clean.to_csv(output_file, index=False)
    print("ETL process complete.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python clean_data.py <input_file> <output_file>")
    else:
        clean_data(sys.argv[1], sys.argv[2])
