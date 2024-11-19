from mysql import connector
valus =  [[1,1],[2,2]]

# Database 
db = connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='Jaosou*2003',
    database='data_computer'
)
print(db)

cursor = db.cursor()
sql = '''
    INSERT INTO data_order ( name_order, price_order)
    VALUE(%s ,%s)
'''
cursor.executemany(sql, valus)
db.commit()
print(f"เพิมข้อมูล {str(cursor.rowcount)}  แถว")