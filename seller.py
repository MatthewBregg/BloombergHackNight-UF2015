import RecordHistory


def getDeriveArray(input, days):
    input = input[len(input)-days:]
    accumulation = []
    for day in input:
        accumulation.append({})
           
    for key in input[0]:
        bidAc = 0
        askAc = 0
        worthAc = 0
        days = 0
        for day, accum_day in zip(input,accumulation):
            days += 1
            # print(days)
            accum_day[key] = {"bid":0,"ask":0,"net_worth":0}
            bidAc += day[key]["bid"]
            accum_day[key]["bid"] = bidAc/days

            askAc += day[key]["ask"]
            accum_day[key]["ask"] = askAc/days

            worthAc += day[key]["net_worth"]
            accum_day[key]["net_worth"] = worthAc/days
    return accumulation


logData = []

def getHighestItem(input,key):
    currentMax = {key:0}
    maxName = ""
    for name in input:
        print("checking"+name)
        if currentMax[key] < input[name][key]:
            currentMax = input[name]
            maxName = name

    return {maxName:currentMax}

def getLowestOwnedItem(input,key):
    currentMin = {key: float("Inf")}
    minName = ""
    for name in input:
        if not RecordHistory.hasStock(name):
            continue
        print("checking"+name)
        if currentMin[key] > input[name][key]:
            currentMin = {input[name]}
            minName = name

    return {minName:currentMin}


def calculateSale():
    # testdata = [
    #     {'AAPL': {"bid":10,"ask":15,"net_worth":5},
    #      'GOOGL':{"bid":1,"ask":5,"net_worth":7} },
    #     {'AAPL': {"bid":15,"ask":10,"net_worth":3},
    #      'GOOGL':{"bid":1,"ask":6,"net_worth":3}}]
    # print(getDeriveArray(testdata,len(testdata)))
    counter = 0
    while(True):
        counter+=1
        if counter < 6:
            continue

        logData.append(RecordHistory.record())
        #print(logData)
        firstDx = getDeriveArray(logData, 5)
     
        secondDx = getDeriveArray(firstDx, 5)
    
        bestItem = getHighestItem(secondDx[-1],"net_worth")

        worstItem = getLowestOwnedItem(secondDx[-1],"net_worth")
        print(secondDx[-1])
        print("Worst")
        print(worstItem)
        print("Best")
        print(bestItem)

        sellAllshares(worstItem)
        buyAllShares(bestItem)

calculateSale()
