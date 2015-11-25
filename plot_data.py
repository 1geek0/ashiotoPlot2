from __future__ import print_function
from datetime import datetime
from boto.dynamodb2.table import *
import plotly.plotly as py
from operator import itemgetter

#DynamoDB Initialization
ashiotoTable = Table('ashioto2')
ashiotoQuery = ashiotoTable.query_2(timestamp__gt=1448445510,plotted__eq=0,index="plotted-timestamp-index")

#Plotly Initialization
#Stream Tokens
tokenGate1 = "vyhq3kud1x";
#tokenGate2 = "e6f22jh83j";
'''tokenGate3 = "kyavx2y466";
tokenGate4 = "wdwvwxi7pv";
tokenGate5 = "ysrav26msb";
tokenGate6 = "otpgoj9u6o";'''
#Setting up Streams
streamGate1 = py.Stream(tokenGate1)
#streamGate2 = py.Stream(tokenGate2)
'''streamGate3 = py.Stream(tokenGate3)
streamGate4 = py.Stream(tokenGate4)
streamGate5 = py.Stream(tokenGate5)
streamGate6 = py.Stream(tokenGate6)'''
#Opening Stream Gates
streamGate1.open()
#streamGate2.open()
'''streamGate3.open()
streamGate4.open()
streamGate5.open()
streamGate6.open()'''

#Gate Lists
listGate1 = []
listGate2 = []
listGate3 = []
listGate4 = []
listGate5 = []
listGate6 = []

#Iterate query results
for item in ashiotoQuery:
    gateID = int(item['gateID'])
    #Plotting to the respective GateIDs
    if gateID == 1:
        #Add to List
        listGate1.append(item)
    elif gateID == 2:
        #Add to List
        listGate2.append(item)
    elif gateID == 3:
        #Add to List
        listGate3.append(item)
    elif gateID == 4:
        #Add to List
        listGate4.append(item)
    elif gateID == 5:
        #Add to List
        listGate5.append(item)
    elif gateID == 6:
        #Add to List
        listGate6.append(item)
    else:
        #Saving Plotted value
        print('Debug Gate')

listGate1.sort(key=itemgetter('timestamp'))
listGate2.sort(key=itemgetter('timestamp'))
listGate3.sort(key=itemgetter('timestamp'))
listGate4.sort(key=itemgetter('timestamp'))
listGate5.sort(key=itemgetter('timestamp'))
listGate6.sort(key=itemgetter('timestamp'))
        
for item in listGate1:
    #Parsing all the values
    timestampUnix = int(item['timestamp'])-19800
    gateID = int(item['gateID'])
    count = int(item['outcount'])
    plotted = int(item['plotted'])
    
    #Get item for resetting plotted value
    plottedToSave = ashiotoTable.get_item(gateID=gateID,timestamp=timestampUnix+19800)
    
    #Converting unix timestamp to human datetime
    timestampHuman = datetime.fromtimestamp(timestampUnix).strftime('%Y-%m-%d %H:%M:%S')
    #Plotting Data
    streamGate1.write({'x':timestampHuman, 'y': count})
    #Saving Plotted value 1
    plottedToSave['plotted'] = 1
    plottedToSave.save()
    #Printing for debuging
    print("Plotted: " + str(count) + "\nTo: " + str(gateID) + "\nAt: " + str(timestampHuman) + "\n")
    
'''for item in listGate2:
    #Parsing all the values
    timestampUnix = int(item['timestamp'])-19800
    gateID = int(item['gateID'])
    count = int(item['outcount'])
    plotted = int(item['plotted'])
    
    #Get item for resetting plotted value
    plottedToSave = ashiotoTable.get_item(gateID=gateID,timestamp=timestampUnix+19800)
    
    #Converting unix timestamp to human datetime
    timestampHuman = datetime.fromtimestamp(timestampUnix).strftime('%Y-%m-%d %H:%M:%S')
    #Plotting Data
    streamGate2.write({'x':timestampHuman, 'y': count})
    #Saving Plotted value 1
    plottedToSave['plotted'] = 1
    plottedToSave.save()
    #Printing for debuging
    print("Plotted: " + str(count) + "\nTo: " + str(gateID) + "\nAt: " + str(timestampHuman) + "\n")

for item in listGate3:
    #Parsing all the values
    timestampUnix = int(item['timestamp'])-19800
    gateID = int(item['gateID'])
    count = int(item['outcount'])
    plotted = int(item['plotted'])
    
    #Get item for resetting plotted value
    plottedToSave = ashiotoTable.get_item(gateID=gateID,timestamp=timestampUnix+19800)
    
    #Converting unix timestamp to human datetime
    timestampHuman = datetime.fromtimestamp(timestampUnix).strftime('%Y-%m-%d %H:%M:%S')
    #Plotting Data
    streamGate3.write({'x':timestampHuman, 'y': count})
    #Saving Plotted value 1
    plottedToSave['plotted'] = 1
    plottedToSave.save()
    #Printing for debuging
    print("Plotted: " + str(count) + "\nTo: " + str(gateID) + "\nAt: " + str(timestampHuman) + "\n")

for item in listGate4:
    #Parsing all the values
    timestampUnix = int(item['timestamp'])-19800
    gateID = int(item['gateID'])
    count = int(item['outcount'])
    plotted = int(item['plotted'])
    
    #Get item for resetting plotted value
    plottedToSave = ashiotoTable.get_item(gateID=gateID,timestamp=timestampUnix+19800)
    
    #Converting unix timestamp to human datetime
    timestampHuman = datetime.fromtimestamp(timestampUnix).strftime('%Y-%m-%d %H:%M:%S')
    #Plotting Data
    streamGate4.write({'x':timestampHuman, 'y': count})
    #Saving Plotted value 1
    plottedToSave['plotted'] = 1
    plottedToSave.save()
    #Printing for debuging
    print("Plotted: " + str(count) + "\nTo: " + str(gateID) + "\nAt: " + str(timestampHuman) + "\n")

for item in listGate5:
    #Parsing all the values
    timestampUnix = int(item['timestamp'])-19800
    gateID = int(item['gateID'])
    count = int(item['outcount'])
    plotted = int(item['plotted'])
    
    #Get item for resetting plotted value
    plottedToSave = ashiotoTable.get_item(gateID=gateID,timestamp=timestampUnix)
    
    #Converting unix timestamp to human datetime
    timestampHuman = datetime.fromtimestamp(timestampUnix).strftime('%Y-%m-%d %H:%M:%S')
    #Plotting Data
    streamGate5.write({'x':timestampHuman, 'y': count})
    #Saving Plotted value 1
    plottedToSave['plotted'] = 1
    plottedToSave.save()
    #Printing for debuging
    print("Plotted: " + str(count) + "\nTo: " + str(gateID) + "\nAt: " + str(timestampHuman) + "\n")

for item in listGate6:
    #Parsing all the values
    timestampUnix = int(item['timestamp'])
    gateID = int(item['gateID'])
    count = int(item['outcount'])
    plotted = int(item['plotted'])
    
    #Get item for resetting plotted value
    plottedToSave = ashiotoTable.get_item(gateID=gateID,timestamp=timestampUnix)
    
    #Converting unix timestamp to human datetime
    timestampHuman = datetime.fromtimestamp(timestampUnix).strftime('%Y-%m-%d %H:%M:%S')
    #Plotting Data
    streamGate6.write({'x':timestampHuman, 'y': count})
    #Saving Plotted value 1
    plottedToSave['plotted'] = 1
    plottedToSave.save()
    #Printing for debuging
    print("Plotted: " + str(count) + "\nTo: " + str(gateID) + "\nAt: " + str(timestampHuman) + "\n")'''

#Closing Plotly Streams
streamGate1.close()
#streamGate2.close()
'''streamGate3.close()
streamGate4.close()
streamGate5.close()
streamGate6.close()'''