import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

#Importing the data
df = pd.read_csv(r'C:\Users\hp\Documents\Practice\Plotly\Plotly-Dashboards-with-Dash-master\Data\mpg.csv')

#Creating an data object
data = [go.Scatter(x=df['horsepower'],
                  y=df['mpg'],
                  text=df['name'],
                  mode='markers',
                  marker=dict(size=df['weight']/100,
                              color=df['cylinders'],
                              showscale=True))]
#Creating the layout
layout = go.Layout(title='Bubble Chart')

#creating a figure object
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='BubbleChart.html')
