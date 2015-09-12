from __future__ import print_function
from datetime import datetime
from boto.dynamodb2.table import *
import plotly.plotly as py
from operator import itemgetter
import pytz

#Total
total = 0

#DynamoDB Initialization
ashiotoTable = Table('ashioto2')
i = 0
while i < 7:
    ashiotoQuery = ashiotoTable.query_2(gateID__eq=i,limit=1)
    for item in ashiotoQuery:
        total += int(item['outcount'])
    i+=1

#Plotly Initialization
#Stream Tokens
token = 'c1lqe6i693'
#Setting up Streams
stream = py.Stream(token)
#Opening Stream Gates
stream.open()
    
right_now = datetime.now(pytz.timezone('Asia/Calcutta'))
stream.write({'x':right_now,'y':total})


#Closing Plotly Streams
stream.close()