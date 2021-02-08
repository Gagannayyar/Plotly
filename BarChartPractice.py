import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

#Importing the data
df = pd.read_csv(r'C:\Users\hp\Documents\Practice\Plotly\Plotly-Dashboards-with-Dash-master\Data\mocksurvey.csv')

#Reset index

df.set_index(df.columns[0], inplace=True)

#Creating data object
data = [go.Bar(x=df[response], y=df.index, orientation='h', name=response) for response in df.columns]

#Creating Layout
layout = go.Layout(title="Survey", barmode='stack')

#Creating Figure
fig = go.Figure(data=data, layout=layout)

#Creating the Figure
pyo.plot(fig, filename="BarChartPractice.html")
