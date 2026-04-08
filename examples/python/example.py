import pandas as pd
import os

def main():
    print("Loading data dictionary...")
    if os.path.exists("data_dictionary.csv"):
        df = pd.read_csv("data_dictionary.csv")
        print(df)
    else:
        print("data_dictionary.csv not found.")

if __name__ == "__main__":
    main()
