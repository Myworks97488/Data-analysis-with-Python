# pip install pandas
# pip install pandas-profiling
import pandas as pd
from pandas_profiling import profileReport

df = pd.read_csv('Dataset .csv')
print(df)