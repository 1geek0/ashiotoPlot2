from __future__ import print_function
from boto.dynamodb2.table import *
from datetime import datetime

#DynamoDB Initialization
ashiotoTable = Table('ashioto2')

setExit=False

gate = 1
while gate <= 6:
    last = 0
    increased = 0
    x = 1
    writeFile = open('/home/geek/ashiotoPlot2/bars/hourly_chart_'+str(gate)+'.csv', 'a+')
    print('time,increased,absolute', file=writeFile)
    first_query = ashiotoTable.query_2(gateID__eq=gate,limit=1)
    for item in first_query:
        timestamp_to_look_for=item['timestamp']
    
    while x <= 50:
        ashiotoQuery = ashiotoTable.query_2(gateID__eq=gate,timestamp__lte=timestamp_to_look_for,limit=1,reverse=True)    
        for item in ashiotoQuery:
            timestampUnix = int(item['timestamp'])-19800
            current = int(item['outcount'])
            if current != last:
                increased = current-last
                last = int(item['outcount'])
                #Converting unix timestamp to human datetime
                timestampHuman = datetime.fromtimestamp(timestampUnix).strftime('%Y-%m-%d %H:%M:%S')
                toPrint = str(timestampHuman) + "," + str(increased) + ',' + str(current)
                print(toPrint, file=writeFile)
                print(increased)
        x+=1
        timestamp_to_look_for+=3600
    gate+=1