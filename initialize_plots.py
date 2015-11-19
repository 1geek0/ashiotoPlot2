import plotly.plotly as py # plotly library
from plotly.graph_objs import Scatter, Layout, Figure, Data, Stream, YAxis

#Titles
titleGate1 = "Gate 1";
titleGate2 = "Gate 2";
'''titleGate3 = "Kothawde Trading";
titleGate4 = "Laxminarayan Ghat";
titleGate5 = "Gharpure Ghat";
titleGate6 = "Panchavati Karanja";'''

#Stream Tokens
tokenGate1 = "xuua0p9vnr";
tokenGate2 = "e6f22jh83j";
'''tokenGate3 = "kyavx2y466";
tokenGate4 = "wdwvwxi7pv";
tokenGate5 = "ysrav26msb";
tokenGate6 = "otpgoj9u6o";'''
tokenGates = [tokenGate1,tokenGate2]#,tokenGate3,tokenGate4,tokenGate5,tokenGate6]

#Streams
streamGate1 = Stream(token=tokenGate1)
streamGate2 = Stream(token=tokenGate2)
'''streamGate3 = Stream(token=tokenGate3)
streamGate4 = Stream(token=tokenGate4)
streamGate5 = Stream(token=tokenGate5)
streamGate6 = Stream(token=tokenGate6)'''

#Traces
traceGate1 = Scatter(x=[],y=[],stream=streamGate1,yaxis='y')
traceGate2 = Scatter(x=[],y=[],stream=streamGate2,yaxis='y')
'''traceGate3 = Scatter(x=[],y=[],stream=streamGate3,yaxis='y')
traceGate4 = Scatter(x=[],y=[],stream=streamGate4,yaxis='y')
traceGate5 = Scatter(x=[],y=[],stream=streamGate5,yaxis='y')
traceGate6 = Scatter(x=[],y=[],stream=streamGate6,yaxis='y')'''


#Layout
name='Innofest Hyderabad 2015'
layout = Layout(title=name)

#Data
data = Data([traceGate1])#,traceGate2,traceGate3,traceGate4,traceGate5,traceGate6])

#Figure
fig = Figure(data=data,layout=layout)

#Plot
print(py.plot(fig,filename=name))