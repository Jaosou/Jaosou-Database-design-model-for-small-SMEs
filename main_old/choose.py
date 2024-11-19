import csv
from mysql import connector
import datetime


def ch_cpu(result):
    ch = int(input("Enter number in range(1-6) : "))
    count = int(input("How much : "))
    i = 0
    status = "pending"
    listOrderDetail = []
    for line in result:
        if i == ch:
            listOrderDetail.append[line[0],count]
        else :
            pass
        i+=1
    return listOrderDetail


def ch_mainboard():
    with open("mainboard.csv",newline='\n') as f:
        ch_mainboard_reader = csv.reader(f)
        i = 0
        ch = int(input("Enter number in range(1-6) : "))
        for line in ch_mainboard_reader:
            if i == ch:
                list_order_name = line[0]
                list_order_price = line[1]
                date_time = datetime.datetime.now()
            else :
                pass
            i+=1
        return list_order_name,list_order_price,str(date_time)


def ch_VGA():
    with open("VGA.csv",newline='\n') as f:
        ch_VGA_reader = csv.reader(f)
        i = 0
        ch = int(input("Enter number in range(1-8) : "))
        for line in ch_VGA_reader:
            if i == ch:
                list_order_name = line[0]
                list_order_price = line[1]
                date_time = datetime.datetime.now()
            else :
                pass
            i+=1
        return list_order_name,list_order_price,str(date_time)


def ch_ram():
    with open("ram.csv",newline='\n') as f:
        ch_ram_reader = csv.reader(f)
        i = 0
        ch = int(input("Enter number in range(1-7) : "))
        for line in ch_ram_reader:
            if i == ch:
                list_order_name = line[0]
                list_order_price = line[1]
                date_time = datetime.datetime.now()
            else :
                pass
            i+=1
        return list_order_name,list_order_price,str(date_time)


def ch_ssd():
    with open("ssd.csv",newline='\n') as f:
        ch_ssd_reader = csv.reader(f)
        i = 0
        ch = int(input("Enter number in range(1-7) : "))
        for line in ch_ssd_reader:
            if i == ch:
                list_order_name = line[0]
                list_order_price = line[1]
                date_time = datetime.datetime.now()
            else :
                pass
            i+=1
        return list_order_name,list_order_price,str(date_time)


def ch_PSW():
    with open("PWS.csv",newline='\n') as f:
        ch_psw_reader = csv.reader(f)
        i = 0
        ch = int(input("Enter number in range(1-7) : "))
        for line in ch_psw_reader:
            if i == ch:
                list_order_name = line[0]
                list_order_price = line[1]
                date_time = datetime.datetime.now()
            else :
                pass
            i+=1
        return list_order_name,list_order_price,str(date_time)


def ch_case():
    with open("case.csv",newline='\n') as f:
        ch_case_reader = csv.reader(f)
        i = 0
        ch = int(input("Enter number in range(1-6) : "))
        for line in ch_case_reader:
            if i == ch:
                list_order_name = line[0]
                list_order_price = line[1]
                date_time = datetime.datetime.now()
            else :
                pass
            i+=1
        return list_order_name,list_order_price,str(date_time)