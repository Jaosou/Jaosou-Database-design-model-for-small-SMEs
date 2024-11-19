SELECT dbpython.customers_python.customer_number, dbpython.orders.customer_number, dbpython.customers_python.customer_fname,customer_lname,order_number
From customers_python
INNER JOIN orders ON customers_python.customer_number = orders.customer_number;