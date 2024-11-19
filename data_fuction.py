import mysql.connector as mysql
import time
import datetime

#! Connect Database
db = mysql.connect(
        host='localhost',
        port='3306',
        user='root',
        password='Jaosou*2003',
        database='dbpython'
    )

cursor = db.cursor()
print(db)
cursor.execute("SELECT * FROM customers_python")
result = cursor.fetchall()

#! writ to database 
def writCusDatabase(cusData):
    cursor = db.cursor()
    sql = '''
        INSERT INTO customers_python ( customer_number, customer_fname, customer_lname, phone, address1, city, country, post_number)
        VALUE(%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s)
    '''
    cursor.execute(sql, cusData)
    db.commit()
    print(f"Data recording completed\n")

#! record data of a customer
def recordData(IdData,inData):
    if int(IdData) >= 100:
        cusNumber = int(IdData) + 1
    else :
        cusNumber = 100
    phoneNumber = int(input("Enter phone number : "))
    address1 = str(input("Enter Address : "))
    city = str(input("Enter City : "))
    coun = str(input("Enter county : "))
    postNumber = int(input("Enter Post number : "))
    print(cusNumber)
    cusData = [cusNumber,inData[0],inData[1],phoneNumber,address1,city,coun,postNumber]
    writCusDatabase(cusData)
    return cusNumber

#! Create new account
def createNewCus(i,result,line,inData):
    if inData == [line[1],line[2]]:
            return line[0]
    if i == len(result):
            lastID = line[0]
            cusNumber = recordData(lastID,inData)
            return cusNumber

#! Seaching data
def readAndSeachData(inData):
    global result
    if len(result) <= 0:
        recordData(100,inData)
        lastid = 100
        return 100
    else:
        i = 0
        while i< len(result):
            """ print(i)
            print(result) """
            dataCus = result[i]
            if inData == [dataCus[1],dataCus[2]]:
                idCus = dataCus[0]
                return idCus
                break
            else :
                """ print(dataCus) """
                lastID = dataCus[0]
            i+=1
        lastid = lastID
        """ print(lastid) """
        newNumber = recordData(lastid,inData)
        return newNumber

#! Writ Order
def writOrder(order,detail):
    cursor = db.cursor()
    sql = '''
        INSERT INTO orders ( order_number, order_date, delivery, status, comment, customer_number)
        VALUE(%s ,%s ,%s ,%s ,%s ,%s)
    '''

    sqlDetail = '''
        INSERT INTO order_detail_table ( order_number, product_code, quantity_ordered, price_each)
        VALUE(%s ,%s ,%s ,%s)
'''
    cursor.execute(sql, order)
    cursor.executemany(sqlDetail,detail)
    db.commit()
    print(f"Data recording completed\n")

#! Seach OrderNumber
def seachOrderNumber():
    cursor.execute("SELECT * FROM orders")
    result  = cursor.fetchall()
    if len(result) == 0:
        orderNumber = 100000
        return orderNumber
    else :
        i = 0
        while i < len(result):
            dataOrder = result[i]
            orderID = dataOrder[0]+1
            print(orderID)
            i+=1
        return orderID
