import pandas as pd
import numpy as np

def main():
    raw = pd.read_csv("data/yelp.csv")
    # Extract 20000 random samples from the dataset
    sample = raw.sample(n=20000, random_state=42)

    # Save the sample to a new CSV file
    sample.to_csv("data/yelp_sample.csv", index=False)
    
if __name__ == "__main__":
    main()