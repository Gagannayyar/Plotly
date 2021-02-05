#Creating an scatter plot

#Importing libraries
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
#Set seed
np.random.seed(42)
#Getting some random x and y for scatter plot
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

#get our scatter object
data = [go.Scatter(x=random_x, y=random_y,mode='markers',marker=dict(
                                                                    size=12,
                                                                    color='rgb(51,204,153)',
                                                                    symbol='pentagon',
                                                                    line={"width":0})
                                                                    )]

#getting layout object
layout = go.Layout(title="Random Scatter Plot",
                    xaxis={'title':"Random X axis"},
                    yaxis=dict(title="Random Y axis"),
                    hovermode='closest')

#Creating the figure
fig = go.Figure(data=data, layout=layout)
#plotting our scatter plot
pyo.plot(fig, filename='scatter.html')
