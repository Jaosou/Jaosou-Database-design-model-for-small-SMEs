import mysql.connector as mysql
import functionChoose

#! Connect Database
db = mysql.connect(
        host='localhost',
        port='3306',
        user='root',
        password='xxxxxxxxxxxxxxxxxxx',
        database='dbpython'
    )

#! CPU
def displayCPU(orderNumber):
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM dbpython.product_table
                    WHERE type_product_code = "CPU"''')
    result = cursor.fetchall()
    print("Choose CPU : \n=====================================================\n")
    i = 1
    for line in result:
        print(f"Choose {i} : {line[2]} : {line[5]} Bath\nSpec : {line[3]}\n")
        i+=1
    print("==============================================\n")
    listOrderDetail = functionChoose.ch_cpu(result,orderNumber)
    return listOrderDetail

#! Main
def displayMain(orderNumber):
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM dbpython.product_table
                    WHERE type_product_code = "Mainboard"''')
    result = cursor.fetchall()
    print("Choose CPU : \n=====================================================\n")
    i = 1
    for line in result:
        print(f"Choose {i} : {line[2]} : {line[5]} Bath\nSpec : {line[3]}\n")
        i+=1
    print("==============================================\n")
    listOrderDetail = functionChoose.ch_cpu(result,orderNumber)
    return listOrderDetail

#! VGA
def displayVGA(orderNumber):
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM dbpython.product_table
                    WHERE type_product_code = "VGA"''')
    result = cursor.fetchall()
    print("Choose CPU : \n=====================================================\n")
    i = 1
    for line in result:
        print(f"Choose {i} : {line[2]} : {line[5]} Bath\nSpec : {line[3]}\n")
        i+=1
    print("==============================================\n")
    listOrderDetail = functionChoose.ch_cpu(result,orderNumber)
    return listOrderDetail

#! Ram
def displayRAm(orderNumber):
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM dbpython.product_table
                    WHERE type_product_code = "Ram"''')
    result = cursor.fetchall()
    print("Choose CPU : \n=====================================================\n")
    i = 1
    for line in result:
        print(f"Choose {i} : {line[2]} : {line[5]} Bath\nSpec : {line[3]}\n")
        i+=1
    print("==============================================\n")
    listOrderDetail = functionChoose.ch_cpu(result,orderNumber)
    return listOrderDetail

#! SSD
def displaySSD(orderNumber):
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM dbpython.product_table
                    WHERE type_product_code = "SSD"''')
    result = cursor.fetchall()
    print("Choose CPU : \n=====================================================\n")
    i = 1
    for line in result:
        print(f"Choose {i} : {line[2]} : {line[5]} Bath\nSpec : {line[3]}\n")
        i+=1
    print("==============================================\n")
    listOrderDetail = functionChoose.ch_cpu(result,orderNumber)
    return listOrderDetail

#! PSW
def displayPSW(orderNumber):
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM dbpython.product_table
                    WHERE type_product_code = "PSW"''')
    result = cursor.fetchall()
    print("Choose CPU : \n=====================================================\n")
    i = 1
    for line in result:
        print(f"Choose {i} : {line[2]} : {line[5]} Bath\nSpec : {line[3]}\n")
        i+=1
    print("==============================================\n")
    listOrderDetail = functionChoose.ch_cpu(result,orderNumber)
    return listOrderDetail

#! Case
def displayCase(orderNumber):
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM dbpython.product_table
                    WHERE type_product_code = "Case"''')
    result = cursor.fetchall()
    print("Choose CPU : \n=====================================================\n")
    i = 1
    for line in result:
        print(f"Choose {i} : {line[2]} : {line[5]} Bath\nSpec : {line[3]}\n")
        i+=1
    print("==============================================\n")
    listOrderDetail = functionChoose.ch_cpu(result,orderNumber)
    return listOrderDetail