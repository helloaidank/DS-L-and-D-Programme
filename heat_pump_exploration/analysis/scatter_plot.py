import os

import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    """Produces a scatter plot."""
    df = pd.read_csv("data/heat_pump_suitability.csv")
    liverpool_df = df[df["lsoa_name"].str.contains("Liverpool", na=False)]
    plt.scatter(liverpool_df["HN_N_avg_score_weighted"], liverpool_df["ASHP_N_avg_score_weighted"])
    plt.xlabel("Heat Network score")
    plt.ylabel("Air source heat pump (ASHP) score")
    plt.title("Heat Network Score vs ASHP score")
    os.makedirs("figures", exist_ok=True)
    plt.savefig("figures/scatter_plot.png", dpi=300, bbox_inches="tight", pad_inches=0.1)
    plt.show()


if __name__ == "__main__":
    main()
