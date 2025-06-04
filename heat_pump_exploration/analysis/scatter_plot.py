from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    """Produces a scatter plot."""
    project_root = Path(__file__).resolve().parents[2]
    data_path = project_root / "data" / "heat_pump_suitability.csv"
    df = pd.read_csv(data_path)
    liverpool_df = df[df["lsoa_name"].str.contains("Liverpool", na=False)]
    plt.scatter(liverpool_df["HN_N_avg_score_weighted"], liverpool_df["ASHP_N_avg_score_weighted"])
    plt.xlabel("Heat Network score")
    plt.ylabel("Air source heat pump (ASHP) score")
    plt.title("Heat Network Score vs ASHP score")
    output_dir = project_root / "figures"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "scatter_plot.png"
    plt.savefig(output_path, dpi=300, bbox_inches="tight", pad_inches=0.1)
    plt.show()


if __name__ == "__main__":
    main()
