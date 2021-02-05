"""Line Chart practice in plotly"""
#importing the libraries
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

#Seeting the seed
np.random.seed(42)

#getting random x and y
x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)

#Creating the line chart object
trace0 = go.Scatter(x=x_values, y=y_values+5, mode='markers', name='markers')

trace1 = go.Scatter(x=x_values, y=y_values+2, mode='lines', name='mylines')

trace2 = go.Scatter(x=x_values, y=y_values, mode='lines+markers', name='myfav')

data = [trace0,trace1, trace2]

layout = go.Layout(title='Line Chart')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='LineChart.html')
