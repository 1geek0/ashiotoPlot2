from boto.dynamodb2.table import *

#DynamoDB Initialization
ashiotoTable = Table('ashioto2')
ashiotoQuery = ashiotoTable.query_2(plotted__eq=1,index="plotted-index")

for item in ashiotoQuery:
    toSave = ashiotoTable.get_item(gateID=item['gateID'],timestamp=item['timestamp'])
    toSave['plotted'] = 0
    toSave.save()