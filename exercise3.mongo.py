from pymongo import MongoClient
client=MongoClient()
db=client.Northwind
order_ids=[]
order_prize=[]
for orders in db.orders.find({'CustomerID':'ALFKI'}):
    order_ids.append(orders['OrderID'])

for id in order_ids:
    sum=0
    for prod in db['order-details'].find({'OrderID':id}):
        prodID=prod['ProductID']
        prodtem=db.products.find_one({'ProductID':prodID})
        price=prodtem['UnitPrice']
        quan=prod['Quantity']
        disc=prod['Discount']
        sum=sum+price*quan*(1-disc)
    order_prize.append((id,sum))
for i in range(len(order_prize)):
    print(order_prize[i])
client.close()



