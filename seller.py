import RecordHistory


def getDeriveArray(input, days):
    accumulation = []
    for day in input:
        accumulation.append({})
           
    for key, value in input[0]:
        bidAc = 0
        askAc = 0
        worthAc = 0
        days = 0
        for day, accum_day in zip(input,accumulation):
            ++days
            bidAc += day[key]["bid"]
            accum_day[key]["bid"] = bidAc/days

            askAc += day[key]["ask"]
            accum_day[key]["ask"] = askAc/days

            worthAc += day[key]["worth"]
            accum_day[key]["worth"] = worthAc/days
    return accumulation


logData = []
def calculateSale():
    logData.append(RecordHistory.record())
    print(logData)
    firstDx = getDeriveArray(logData, 10)
    print(firstDx)
    secondDx = getDeriveArray(firstDx, 10)


calculateSale()
