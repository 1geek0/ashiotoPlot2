import plotly.plotly as py
from plotly.graph_objs import *

tokenC = 'c1lqe6i693'
stream = Stream(token=tokenC)
name = "Parvani 2 Hourly"
trace = Bar(x=[],y=[],stream=stream)
layout = Layout(title=name)
data = Data([trace])
fig = Figure(data=data,layout=layout)
py.plot(fig,filename=name)