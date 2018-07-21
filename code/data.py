#!/usr/bin/env python
data_file = "/home/iz4vve/Projects/personal/dseclub-clustering/data/time_series_bonds.xlsx"
sheet_name = "d"
index = "date"

# START OMIT
import pandas as pd

data = pd.read_excel(data_file, sheet_name=sheet_name).set_index(index)
# END OMIT

data.columns = [f"X{i:03d}" for i in range(1, data.shape[1] + 1)]

print(data.head())

