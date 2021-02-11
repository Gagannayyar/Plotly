"""Create Histogram"""

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

#Importing the DataFrame
df = pd.read_csv(r'C:\Users\hp\Documents\Practice\Plotly\Plotly-Dashboards-with-Dash-master\Data\mpg.csv')

#Creating the data object
data = [go.Histogram(x=df['mpg'], xbins=dict(start=min(df['mpg']), end=max(df['mpg']), size=2))]

#Creating an Layout
layout = go.Layout(title='Histogram')

#Creating an fig
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='Histogram.html')
