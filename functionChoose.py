def ch_cpu(result,orderNumber):
    ch = int(input(f"Enter number in range(1-{len(result)}) : "))
    count = int(input("How much : "))
    i = 0
    status = "pending"
    listOrderDetail = []
    for line in result:
        if i == ch:
            listOrderDetail = [orderNumber,line[0],count,line[5]]
        else :
            pass
        i+=1
    return listOrderDetail