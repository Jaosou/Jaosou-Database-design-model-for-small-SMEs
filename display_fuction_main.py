import data_fuction
import os
import orderDatanew
import datetime
import time

#! Create Bill
def cal_bill(list_order_total) :
    print("===================== Bill ====================\n")
    print("Title\tPrice")
    sum = 0
    for i in list_order_total : 
        print(f"{i[1]}\t{i[3]}")
        sum = sum+int(i[3])
    print("\n--------------------------------")
    print(f"Price Total :\t{sum} Bath")
    print("--------------------------------\n")
    return sum

#!Customer display
def displayCustomer():
    n = True
    while n == True:
        orderNumber = data_fuction.seachOrderNumber()
        orderData = []
        orderDetailData = []
        print("============== Hi! Customer ==============\n")
        fname = str(input("Enter Frist name : "))
        lname = str(input("Enter Last name : "))
        cusNumber = data_fuction.readAndSeachData([fname,lname])
        print("==========================================\n")

        print("============== Hi New Order ==============")
        print(f"Order Number : {orderNumber}")
        print("Choose 1 : Separate pieces\nChoose 2 : Set pieces\nChoose 3 : Promotion\n")
        ch = int(input("What kind of product will I buy? : "))
        print("==========================================\n")
        if ch == 1 :
            i = 10
            while True :
                print("\n=================================================\n")
                print("What to U want to buy? : ")
                print("Choose 1 : CPU\nChoose 2 : Mainboard\nChoose 3 : VGA\nChoose 4 : Ram\nChoose 5 : SSD\nChoose 6 : PSW\nChoose 7 : Case\nChoose 8 : For finish")
                print("=================================================\n")
                ch = int(input("Enter Number for choose 1 - 8 : "))
                if ch == 1:
                    orderDetailData.append(orderDatanew.displayCPU(orderNumber))
                elif ch == 2:
                    orderDetailData.append(orderDatanew.displayMain(orderNumber))
                elif ch == 3:
                    orderDetailData.append(orderDatanew.displayVGA(orderNumber))
                elif ch == 4:
                    orderDetailData.append(orderDatanew.displayRAm(orderNumber))
                elif ch == 5:
                    orderDetailData.append(orderDatanew.displaySSD(orderNumber))
                elif ch == 6:
                    orderDetailData.append(orderDatanew.displayPSW(orderNumber))
                elif ch == 7:
                    orderDetailData.append(orderDatanew.displayCase(orderNumber))
                elif ch == 8 :
                    break
                else :
                    print("Plese choose in range :")
        elif ch == 2 : 
            print("Choose 1 : Buy comset\nChoose 2 : for finish")
            ch = int(input("Number : "))
            if ch == 1 :
                orderDetailData = [orderDatanew.displayCPU(orderNumber)
                                    ,orderDatanew.displayMain(orderNumber)
                                    ,orderDatanew.displayVGA(orderNumber)
                                    ,orderDatanew.displayRAm(orderNumber)
                                    ,orderDatanew.displaySSD(orderNumber)
                                    ,orderDatanew.displayPSW(orderNumber)
                                    ,orderDatanew.displayCase(orderNumber)]
        elif ch == 3 :
            orderDetailData = [["i5_14600KF ",1,12665]
                                ,orderDatanew.displayMain(orderNumber)
                                ,orderDatanew.displayVGA(orderNumber)
                                ,orderDatanew.displayRAm(orderNumber)
                                ,orderDatanew.displaySSD(orderNumber)
                                ,orderDatanew.displayPSW(orderNumber)
                                ,["ae_black",1,915]]
        else :
            print("[Error] - Plese choose number between 1-3 :")
        print("\n=========================================")
        print("Finish for choose : ")
        print("=========================================\n")
        print(orderDetailData)
        cal_bill(orderDetailData)
        orderData = [orderNumber,str(datetime.datetime.today()),500,"Pending","",cusNumber]
        print(orderData)
        data_fuction.writOrder(orderData,orderDetailData)
        orderNumber+=1
        time.sleep(5)
        os.system('cls')
displayCustomer()