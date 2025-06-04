# fmt: off
# ruff: noqa
import pandas as pd, numpy as np


def compute_correlations(   ):
  df= pd.read_csv("data/heat_pump_suitability.csv")
  liverpool = df[df["lsoa_name"].str.contains("Liverpool",na=False)]
  corr = liverpool[["HN_N_avg_score_weighted","ASHP_N_avg_score_weighted"]].corr().iloc[0,1]
  print( "Correlation between heat network and ASHP scores:", corr )


if __name__=="__main__":
 compute_correlations( )
