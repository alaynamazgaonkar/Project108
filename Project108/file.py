import plotly.figure_factory as ff
import pandas as pd

pf=pd.read_csv("data.csv")
rating=pf['Avg Rating']

fig=ff.create_distplot([rating],['result'])
fig.show()