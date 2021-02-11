import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np
import pandas as pd

#Importing the dataf
df = pd.read_csv(r'C:\Users\hp\Documents\Practice\Plotly\Plotly-Dashboards-with-Dash-master\Data\iris.csv')

#Converting to list for input as data and labels
hist_data = []
group_label = []

for i in df['class'].unique():
    hist_data.append(list(df[df['class'] == i]['petal_length']))
    group_label.append(i)


#group_label = ['x1', 'x2', 'x3', 'x4']

fig = ff.create_distplot(hist_data, group_label, bin_size=[0.2, 0.1, 0.3, 0.4])

pyo.plot(fig, filename='Displot.html')
