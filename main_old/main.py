import csv
from mysql import connector
import order_data as order_data
import pandas as pd
import datetime
import main_old.function_at as function_at

def cal_bill(list_order_total) :
    print("===================== Bill ====================\n")
    print("Title\tPrice")
    sum = 0
    for i in list_order_total : 
        print(f"{i[0]}\t{i[1]}")
        sum = sum+int(i[1])
    print("\n--------------------------------")
    print(f"Price Total :\t{sum} Bath")
    print("--------------------------------\n")
    return sum

def cal_amount(list_order_total) :
    price_total = cal_bill(list_order_total)
    price_sum = function_at.delivery(price_total)
    money_received = int(input("Enter money received : "))
    print(f"Price total : {price_total} Bath\n")
    print("====================================")
    print(f"Change : {money_received-price_total} Bath")
    print("====================================")

with open("data_projrct.csv","a+",encoding="UTF-8",newline='') as f :
    wri_csv = csv.writer(f)
    wri_csv.writerow(["Title","Price","Time"])
    n = True
    i = 100000
    while n == True :
        print("\n=================================================\n")
        print(f"Order : {i}")
        print("What kind of product will I buy? : ")
        print("Choose 1 : Separate pieces\nChoose 2 : Set pieces\nChoose 3 : Promotion\n")    
        print("=================================================\n")
        list_order_total = []
        ch = int(input("Enter number for buy : "))
        if ch == 1 :
            i = 10
            while i>5 :
                print("\n=================================================\n")
                print("What to U want to buy? : ")
                print("Choose 1 : CPU\nChoose 2 : Mainboard\nChoose 3 : VGA\nChoose 4 : Ram\nChoose 5 : SSD\nChoose 6 : PSW\nChoose 7 : Case\nChoose 8 : For finish")
                print("=================================================\n")
                ch = int(input("Enter Number for choose 1 - 8 : "))
                if ch == 1 :
                    list_order = order_data.cpu()
                    list_order_total.append(list_order)
                    print(list_order_total)
                elif ch == 2 :
                    list_order = order_data.mainboard()
                    list_order_total.append(list_order)
                    print(list_order_total)
                elif ch == 3 :
                    list_order = order_data.VGA()
                    list_order_total.append(list_order)
                    print(list_order_total)
                elif ch == 4 :
                    list_order = order_data.ram()
                    list_order_total.append(list_order)
                    print(list_order_total)
                elif ch == 5 :
                    list_order = order_data.ssd()
                    list_order_total.append(list_order)
                    print(list_order_total)
                elif ch == 6 :
                    list_order = order_data.psw()
                    list_order_total.append(list_order)
                    print(list_order_total)
                elif ch == 7 :
                    list_order = order_data.case()
                    list_order_total.append(list_order)
                    print(list_order_total)
                elif ch == 8 :
                    break
                else :
                    print("Plese choose in range 1-8 : ")
        elif ch == 2 : 
            print("Choose 1 : Buy comset\nChoose 2 : for finish")
            ch = int(input("Number : "))
            if ch == 1 :
                cpu_order = order_data.cpu()
                mainboard_order = order_data.mainboard()
                vga_order = order_data.VGA()
                ram_order = order_data.ram()
                ssd_order = order_data.ssd()
                psw_order = order_data.psw()
                case_order = order_data.case()
                list_order_total = [cpu_order
                                    ,mainboard_order
                                    ,vga_order
                                    ,ram_order
                                    ,ssd_order
                                    ,psw_order
                                    ,case_order]
        elif ch == 3 :
            list_order_total = [["Intel Core i5-14600KF",12665,str(datetime.datetime.now())]]
            mainboard_order = order_data.mainboard()
            vga_order = order_data.VGA()
            ram_order = order_data.ram()
            ssd_order = order_data.ssd()
            psw_order = order_data.psw()
            list_order_total.append(["AERO COOL CS-1103 Black",915,str(datetime.datetime.now())])
        else :
            print("[Error] - Plese choose number between 1-3 :")
        print("\n=========================================")
        print("Finish for choose : ")
        print("=========================================\n")

        data = pd.DataFrame(list_order_total,columns=['Title name','Price','Date time'])
        data.to_excel('project_end.xlsx')
            
        function_at.wri_csv(list_order_total)
        function_at.connec_base(list_order_total)
        
        price_total = cal_bill(list_order_total)
        if price_total == 0 :
            pass
        else :
            cal_amount(list_order_total)   

