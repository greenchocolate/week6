import pymongo
from pymongo import MongoClient
client=MongoClient()
db=client.Northwind
order_ids=[]
product=[]
for orders in db.orders.find({'CustomerID':'ALFKI'}):
    order_ids.append(orders['OrderID'])

for id in order_ids:
    c=0
    for prod in db['order-details'].find({'OrderID':id}):
        c+=1
        prodID=prod['ProductID']
        prodna=db.products.find_one({'ProductID':prodID})
        prodname=prodna['ProductName']
        if c==1:
            temp=(id,prodID,prodname)
        elif c==2:
            product.append(temp)
            product.append((id,prodID,prodname))
        else:
            product.append((id, prodID, prodname))
for i in range(len(product)):
    print(product[i])
client.close()