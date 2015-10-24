import RecordHistory


def getDeriveArray(input, days):
    input = input[len(input)-days:]
    print("input is")
    print(input)
    print("done")
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


def calculateSale():
    # testdata = [
    #     {'AAPL': {"bid":10,"ask":15,"net_worth":5},
    #      'GOOGL':{"bid":1,"ask":5,"net_worth":7} },
    #     {'AAPL': {"bid":15,"ask":10,"net_worth":3},
    #      'GOOGL':{"bid":1,"ask":6,"net_worth":3}}]
    # print(getDeriveArray(testdata,len(testdata)))
    for i in range(1,10):
        logData.append(RecordHistory.record())
        print(logData)
        firstDx = getDeriveArray(logData, 10)
        print("first dx")
        print(firstDx)
        secondDx = getDeriveArray(firstDx, 10)
        print("Second dx")
        print(secondDx)

calculateSale()
