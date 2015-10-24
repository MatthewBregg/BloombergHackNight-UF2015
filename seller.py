import RecordHistory


def getDeriveArray(input, days):
    input = input[len(input)-days:]
    accumulation = []
    for day in input:
        accumulation.append({})
           
    for key in input[0]:
        bidAcP = 0 
        askAcP = 0 
        worthAcP =0 
        days = 0
        for day, accum_day in zip(input,accumulation):
            days += 1
            # print(days)
            accum_day[key] = {"bid":0,"ask":0,"net_worth":0}
#            print("doing the deriving thing")
#            print(str(bidAcP) + " " + str(askAcP) + " " + str(worthAcP))
            accum_day[key]["bid"] = day[key]["bid"] - bidAcP
            accum_day[key]["ask"] = day[key]["ask"] - askAcP
            accum_day[key]["net_worth"] = day[key]["net_worth"] - worthAcP
            bidAcP = day[key]["bid"]
            askAcP = day[key]["ask"]
            worthAcP = day[key]["net_worth"]
    return accumulation[1:]


logData = []

def getHighestItem(input,key):
    currentMax = {key:0}
    maxName = ""
    for name in input:
        #print("checking"+name)
        if currentMax[key] < input[name][key]:
            currentMax = input[name]
            maxName = name

    return maxName

def getLowestOwnedItem(input,key):
    currentMin = {key: float("Inf")}
    minName = ""
    for name in input:
        stock,shares = RecordHistory.hasStock(name)
        if not stock:
            continue
        #print("checking"+name)
        if currentMin[key] > input[name][key]:
            currentMin = input[name]
            minName = name

    return minName

def getAverage(input):
    assert(len(input) > 0)
    counter = 0
    average = input[0]
    for key in average:
        average[key]["bid"] = 0
        average[key]["ask"] = 0
        average[key]["net_worth"] = 0
        
    for day in input:
        counter+=1
        for key in day:
            average[key]["bid"] += day[key]["bid"] 
            average[key]["ask"] += day[key]["ask"]
            average[key]["net_worth"] += day[key]["net_worth"]
    
    for key in average:
        average[key]["bid"] /= counter
        average[key]["ask"] /= counter
        average[key]["net_worth"] /= counter
    return average

def calculateSale():
    # testdata = [
    #     {'AAPL': {"bid":10,"ask":15,"net_worth":5},
    #      'GOOGL':{"bid":1,"ask":5,"net_worth":7} },
    #     {'AAPL': {"bid":15,"ask":10,"net_worth":3},
    #      'GOOGL':{"bid":1,"ask":6,"net_worth":3}}]
    # print(getDeriveArray(testdata,len(testdata)))
    counter = 0
    offset = [1,1,1]
    prev_tic = ["","",""]
    while(True):
        counter+=1
        currentRecord = RecordHistory.record()
        logData.append(currentRecord)
        if counter < 11:
            continue
        print("MY CASH : " + str(RecordHistory.getCash()))
        historyLength = min(counter,100)
        #print(logData)
        firstDx = getDeriveArray(logData, historyLength)
        #print("first dx")
        #print(firstDx)
        #WARNING, each time it is redireved, must go one less than previous call.
        #Will not work in this case if you do 
        #firstDx = getDeriveArray(logData, 5)
        #secondDx = getDeriveArray(firstDx, 5)
        #As in the second call, the 5 must be no greater than 4!!!!!
        #This is because the derivative array received is one less than the input array!!!
        secondDx = getDeriveArray(firstDx, historyLength-1)
        #print("second dx")
        #print(secondDx)
        average = getAverage(secondDx)
        #print("average")
        #print(average)
        bestItem = getHighestItem(average,"bid")
        RecordHistory.buyAllShares(bestItem,currentRecord)
        for i in  range(0,3):
            worstItem = getLowestOwnedItem(average,"ask")
            if(worstItem == ''):
                break
            else:
                prev_tic[i],offset[i] = RecordHistory.sellAllSharesMod(worstItem,currentRecord,prev_tic[i],offset[i])
                average.pop(worstItem,None)
        #record
        #for i in  range(0,3):
        
        print("Worst")
        print(worstItem)
        print("Best")
        print(bestItem)
        

calculateSale()
