"""Bar Chart using plotly and pandas dataframe"""

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

#Importing the data
df = pd.read_csv(r'C:\Users\hp\Documents\Practice\Plotly\Plotly-Dashboards-with-Dash-master\Data\2018WinterOlympics.csv')

#Creating an bar object
trace1 = [go.Bar(x=df['NOC'], y=df['Gold'], name='Gold',marker={'color':'#FFD700'})]

trace2 = go.Bar(x=df['NOC'], y=df['Silver'], name="Silver", marker={'color':'#9EA0A1'})

trace3 = go.Bar(x=df['NOC'], y=df['Bronze'], name="Bronze", marker={'color':'#CD7F32'})

#data = [trace1, trace2, trace3]

#Creating the layout
layout = go.Layout(title='Medals', barmode='stack')

#Creating the figure object
fig = go.Figure(data=trace1, layout=layout)

#Show The visual
pyo.plot(fig, filename="BarChartPandas.html")
