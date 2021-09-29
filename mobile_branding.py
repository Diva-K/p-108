import plotly.figure_factory as ff
import pandas as pd
import csv

df=pd.read_csv("data2.csv")
fig=ff.create_distplot([df["Avg Rating"].to_list()],["Average rating"],show_hist=False)
fig.show()