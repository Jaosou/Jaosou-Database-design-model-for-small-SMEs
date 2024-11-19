import csv

'''list_data = [["Intel Core i9-13900","21700","24 cores 32 threads || Base Clock : 2.0 GHz  ||  Boots Clock : 5.6 GHz (Intel UHD Graphics 770)",1,2],
             ["Intel Core i9-13900","21700","24 cores 32 threads || Base Clock : 2.0 GHz  ||  Boots Clock : 5.6 GHz (Intel UHD Graphics 770)",1,2],
             ["Intel Core i9-13900","21700","24 cores 32 threads || Base Clock : 2.0 GHz  ||  Boots Clock : 5.6 GHz (Intel UHD Graphics 770)",1,2],
             ["Intel Core i9-13900","21700","24 cores 32 threads || Base Clock : 2.0 GHz  ||  Boots Clock : 5.6 GHz (Intel UHD Graphics 770)",1,2],
             ["Intel Core i9-13900","21700","24 cores 32 threads || Base Clock : 2.0 GHz  ||  Boots Clock : 5.6 GHz (Intel UHD Graphics 770)",1,2],
             ["Intel Core i9-13900","21700","24 cores 32 threads || Base Clock : 2.0 GHz  ||  Boots Clock : 5.6 GHz (Intel UHD Graphics 770)",1,2],
             ["Intel Core i9-13900","21700","24 cores 32 threads || Base Clock : 2.0 GHz  ||  Boots Clock : 5.6 GHz (Intel UHD Graphics 770)",1,2],
             ["Intel Core i9-13900","21700","24 cores 32 threads || Base Clock : 2.0 GHz  ||  Boots Clock : 5.6 GHz (Intel UHD Graphics 770)",1,2],
             ["Intel Core i9-13900","21700","24 cores 32 threads || Base Clock : 2.0 GHz  ||  Boots Clock : 5.6 GHz (Intel UHD Graphics 770)",1,2],
             ["Intel Core i9-13900","21700","24 cores 32 threads || Base Clock : 2.0 GHz  ||  Boots Clock : 5.6 GHz (Intel UHD Graphics 770)",1,2],
             ["Intel Core i9-13900","21700","24 cores 32 threads || Base Clock : 2.0 GHz  ||  Boots Clock : 5.6 GHz (Intel UHD Graphics 770)",1,2],
             ["Intel Core i9-13900","21700","24 cores 32 threads || Base Clock : 2.0 GHz  ||  Boots Clock : 5.6 GHz (Intel UHD Graphics 770)",1,2],
             ["Intel Core i9-13900","21700","24 cores 32 threads || Base Clock : 2.0 GHz  ||  Boots Clock : 5.6 GHz (Intel UHD Graphics 770)",1,2],]


with open("CPU.csv",'r', newline='') as data :
    cpu_reader = csv.reader(data)

    for line in cpu_reader :
        print(line[1])

with open("order.csv","a+", newline='') as dataw:
    cpu_writer = csv.writer(dataw)
    for i in range (0,len(list_data)):
        cpu_writer.writerow(list_data[i])'''

with open("order.csv","a+", newline='') as dataw:
    list_data = []
    n = int(input("Enter Low : "))
    print("========================================")
    for n in range(0,n):
        id_data = int(input("Enter Id data : "))
        title = str(input("Enter title data : "))
        price_data = int(input("Enter price data : "))
        note_data =  str(input("Enter note data : "))
        day = str(input("Enter day data : "))
        list_order = [id_data,title,price_data,note_data,day]
        list_data.append(list_order)
        cpu_writer = csv.writer(dataw)
        print("======================================")
    
    cpu_writer.writerows(list_data)