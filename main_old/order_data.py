import csv
import choose


def cpu():
    with open("CPU.csv",newline='\n') as f:
        cpu_reader = csv.reader(f)
        i = 0
        print("Choose CPU : \n=====================================================\n")
        for line in cpu_reader :
            print(f"Choose {i} : {line[0]} : {line[1]} Bath\nSpec : {line[2]}\n")
            i+=1
        print("==============================================\n")
        list_order_name,list_order_price,date_time = choose.ch_cpu()
        list_order = [list_order_name,list_order_price,date_time]
        return list_order 



def mainboard():
    with open("mainboard.csv",newline='\n') as f:
        mainboard_reader = csv.reader(f)
        i=0 
        print("Mainboard : \n=====================================================\n")
        for line in mainboard_reader :
            print(f"Choose {i} : {line[0]} : {line[1]} Bath\nSpec : {line[2]}\n")
            i +=1
        print("==============================================\n")
        list_order_name,list_order_price,date_time = choose.ch_mainboard()
        list_order = [list_order_name,list_order_price,date_time]
        return list_order


def VGA():
    with open("VGA.csv",newline='\n') as f:
        VGA_reader = csv.reader(f)
        i = 0
        print("VGA : \n=====================================================\n")
        for line in VGA_reader :
            print(f"Choose {i} : {line[0]} : {line[1]} Bath\nSpec : {line[2]}\n")
            i +=1
        print("==============================================\n")
        list_order_name,list_order_price,date_time = choose.ch_VGA()
        list_order = [list_order_name,list_order_price,date_time]
        return list_order


def ram():
    with open("ram.csv","r") as f:
        ram_reader = csv.reader(f)
        i = 0
        print("Ram : \n=====================================================\n")
        for line in ram_reader :
            print(f"Choose {i} : {line[0]} : {line[1]} Bath\nSpec : {line[2]}\n")
            i +=1
        print("==============================================\n")
        list_order_name,list_order_price,date_time = choose.ch_ram()
        list_order = [list_order_name,list_order_price,date_time]
        return list_order


def ssd():
    with open("ssd.csv","r") as f:
        ssd_reader = csv.reader(f)
        i = 0
        print("SSD : \n=====================================================\n")
        for line in ssd_reader :
            print(f"Choose {i} : {line[0]} : {line[1]} Bath\nSpec : {line[2]}\n")
            i += 1
        print("==============================================\n")
        list_order_name,list_order_price,date_time = choose.ch_ssd()
        list_order = [list_order_name,list_order_price,date_time]
        return list_order


def psw():
    with open("PWS.csv","r") as f:
        psw_reader = csv.reader(f)
        i = 0
        print("PSW : \n=====================================================\n")
        for line in psw_reader :
            print(f"Choose {i} : {line[0]} : {line[1]} Bath\nSpec : {line[2]}\n")
            i += 1        
        print("==============================================\n")
        list_order_name,list_order_price,date_time = choose.ch_PSW()
        list_order = [list_order_name,list_order_price,date_time]
        return list_order


def case():
    with open("case.csv","r") as f:
        case_reader = csv.reader(f)
        i = 0
        print("Case : \n=====================================================\n")
        for line in case_reader :
            print(f"Choose {i} : {line[0]} : {line[1]} Bath\nSpec : {line[2]}\n")
            i += 1
        print("==============================================\n")
        list_order_name,list_order_price,date_time = choose.ch_case()
        list_order = [list_order_name,list_order_price,date_time]
        return list_order

