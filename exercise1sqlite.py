import sqlite3
conn=sqlite3.connect('northwind.db')
conn.text_factory = lambda x: str(x, 'cp1250')
for prod in conn.execute("SELECT 'Orders'.OrderID,'Products'.ProductID,'Products'.ProductName \
FROM 'Products' LEFT JOIN \
('Order Details' INNER JOIN 'Orders' ON 'Order Details'.OrderID = 'Orders'.OrderID) \
'Order Details' ON 'Products'.ProductID='Order Details'.ProductID  \
WHERE CustomerID='ALFKI' ORDER BY 'Orders'.OrderID"):
    print(prod)