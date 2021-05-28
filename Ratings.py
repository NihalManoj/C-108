import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv("Ratings.csv")
fig = ff.create_distplot([df["AvgRating"].tolist()], ["Ratings"], show_hist = False)
fig.show()