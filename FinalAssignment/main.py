import pandas as pd
import matplotlib.pyplot as plt
from colorspacious import cspace_converter
import numpy as np
data = pd.read_csv("liquor.csv")

df= pd.DataFrame(data)
bs=df.groupby(by="zip_code")['bottles_sold'].sum()

zip_codes=df["zip_code"].unique()
df2= df['sale_dollars']/df.groupby('zip_code')['sale_dollars'].transform('sum')
gp= df.sort_values('bottles_sold',ascending=False).drop_duplicates(['zip_code'])

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
 print(gp[["zip_code","item_description","bottles_sold"]])
 print(df2)
 print(bs)
 print(zip_codes)
 plt.scatter(x=zip_codes,y=bs,c=np.random.rand(len(zip_codes),3))
 plt.show()

