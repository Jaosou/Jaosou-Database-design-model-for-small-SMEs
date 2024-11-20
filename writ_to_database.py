import mysql.connector as mysql
import csv

def writ_database(list_order_data):
    db = mysql.connect(
        host='localhost',
        port='3306',
        user='root',
        password='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        database='dbpython'
    )
    print(db)
    cursor = db.cursor()
    sql = '''
        INSERT INTO product_table ( product_code, type_product_code, product_name, productDisciption, quantity_in_stock, price)
        VALUE(%s ,%s ,%s ,%s ,%s ,%s)
    '''
    cursor.executemany(sql, list_order_data)
    db.commit()
    print(f"Insert data {str(cursor.rowcount)} row\n")


with open("DataProduct.csv",newline='\n') as f:
    cpu_reader = csv.reader(f)
    i = 0
    list_data = []
    for line in cpu_reader:
        list_data.append(line)
    print(list_data)
    writ_database(list_data)


