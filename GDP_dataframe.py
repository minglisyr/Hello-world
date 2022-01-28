# This is a testcase for Pandas operation
import pandas as pd
df=pd.read_csv('gdp.csv')
df_pivot=df.pivot_table(index='year', columns='country', values='popshare')
df_pivot.to_csv('GDP_pivot.csv')
df_pivot_comp=df_pivot[['Afghanistan','Australia','Brazil','Canada','China','Denmark','France','India','Japan','United Kingdom','United States']]
df_pivot_comp.to_csv('GDP_pivot_comp.csv')
df_pivot_comp.plot(kind='line').legend(loc='best')
import matplotlib.pyplot as plt
plt.savefig('plot-1.png')