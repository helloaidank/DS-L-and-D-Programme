import pandas as pd
from scipy import stats


def main() -> None:
    """Print some summary statistics about the dataframe."""
    print("Hello!")
    df = pd.read_csv("data/heat_pump_suitability.csv")
    print(df.head())

    # Calculate basic statistics on numeric columns using scipy
    numeric_columns = df.select_dtypes(include=["number"]).columns
    for column in numeric_columns:
        data = df[column].dropna()

        # Calculate mean, standard deviation, and z-scores
        mean = stats.tmean(data)
        std_dev = stats.tstd(data)
        z_scores = stats.zscore(data)

        print(f"\nStatistics for column '{column}':")
        print(f"Mean: {mean}")
        print(f"Standard Deviation: {std_dev}")
        print(f"First 5 Z-scores: {z_scores[:5]}")


if __name__ == "__main__":
    main()
