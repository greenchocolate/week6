#STEPBYSTEP
#1. start mongod: type mongod in console
#2. run mongo-import-win.bat in (new) console
#3. from pymongo import MongoClient
#client=MongoClient()
#db=client.Northwind
#for cust in db.customers.find({'CustomerID':'ALFKI'}):
    #do something
    #this works yes
import pymongo
from pymongo import MongoClient
client=MongoClient()
db=client.Northwind
order_ids=[]
product=[]
for orders in db.orders.find({'CustomerID':'ALFKI'}):
    order_ids.append(orders['OrderID'])

for id in order_ids:
    for prod in db['order-details'].find({'OrderID':id}):
        prodID=prod['ProductID']
        prodna=db.products.find_one({'ProductID':prodID})
        prodname=prodna['ProductName']
        product.append((id,prodID,prodname))
for i in range(len(product)):
    print(product[i])
client.close()