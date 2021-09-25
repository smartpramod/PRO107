import csv
import pandas as pd
import plotly.graph_objects as pgo

df=pd.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())

fig=pgo.Figure(pgo.Bar(
    x=df.groupby("level")["attempt"].mean(),
    y=['Level 1','level 2','Level 3','level 4'],
    orientation='v'
))
fig.show()