import sqlite3
conn=sqlite3.connect('northwind.db')
conn.text_factory = lambda x: str(x, 'cp1250')
d={}
temp={}
for prod in conn.execute("SELECT 'Orders'.OrderID,'Products'.ProductID, 'Products'.ProductName FROM 'Products' LEFT JOIN ('Order Details' INNER JOIN 'Orders' ON 'Order Details'.OrderID = 'Orders'.OrderID) 'Order Details' ON 'Products'.ProductID='Order Details'.ProductID  WHERE CustomerID='ALFKI' ORDER BY 'Orders'.OrderID"):
    if (prod[0] in d):
        if (d[prod[0]]==1):
            print(temp[prod[0]])
            print(prod)
            d[prod[0]]+=1
        else:
            print(prod)
    else:
        d[prod[0]]=1
        temp[prod[0]]=prod
