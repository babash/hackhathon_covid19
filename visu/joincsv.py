import json
import csv
import pandas as pd

a = pd.read_csv("./csv/covid_stress.csv")
b = pd.read_csv("./csv/hospit_formatted.csv")
b = b.dropna(axis=1)
merged = pd.merge(a, b,  how='left', on = ['region','date'])
merged.to_csv("./csv/output.csv", index=False)

dpt = pd.read_csv("./csv/departements-region.csv")

merged_dpt = pd.merge(merged, dpt, on = ['region'])
merged_dpt.to_csv("./csv/final.csv", index=False)
