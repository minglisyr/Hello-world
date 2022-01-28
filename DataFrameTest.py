# This is a testcase for DataFrame in Pandas
from operator import index
import pandas as pd
df=pd.read_csv('StudentsPerformance.csv')
df_pivot = round(df.pivot_table(index='gender',columns='race/ethnicity',values=['math score', 'reading score','writing score']),2)
df_pivot.to_excel('SP_PivotTable.xlsx')