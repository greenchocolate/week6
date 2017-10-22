"""SELECT city, sum(salary) AS "Total Salary"
FROM employees
WHERE state = 'CA'
GROUP BY city;"""

import sqlite3
conn=sqlite3.connect('northwind.db')
conn.text_factory = lambda x: str(x, 'cp1250')
for prod in conn.execute\
("SELECT 'Orders'.OrderID,\
sum('Products'.UnitPrice*'Order Details'.Quantity*(1-'Order Details'.Discount)) \
FROM 'Products' LEFT JOIN\
('Order Details' INNER JOIN 'Orders' ON 'Order Details'.OrderID = 'Orders'.OrderID) \
'Order Details' ON 'Products'.ProductID='Order Details'.ProductID  WHERE CustomerID='ALFKI' \
GROUP BY 'Orders'.OrderID ORDER BY 'Orders'.OrderID"):
    print(prod)