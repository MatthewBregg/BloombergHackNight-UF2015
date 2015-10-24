__author__ = 'johnmichaelreed2'
import thread
import time

numEntries = 1000

# Only the polling thread can modify this.
records = {'AAPL': np.zeros(numEntries), 'ATVI': np.zeros(numEntries), 'EA': np.zeros(numEntries),
           'FB': np.zeros(numEntries), 'GOOG': np.zeros(numEntries), 'MSFT': np.zeros(numEntries),
           'SBUX': np.zeros(numEntries), 'SNY': np.zeros(numEntries), 'TSLA': np.zeros(numEntries),
           'TWTR': np.zeros(numEntries)}

# This is the current index in  the list of records. Only the polling thread can modify it.
currentIndex = 0


# Records past prices for all tickers
# Input: (rec) hash map <ticker,list_of_prices> and (pos) current position
# Output: current position
def record(rec: dict, pos

:int) -> int:
x = run("___", "____", "SECURITIES")
securities = x.split(" ")
securities.pop(0)
for i in range(0, len(securities)):
    if (securities[i] != '3.0E-4' and securities[i] != '0.005'):
        if (len(securities[i]) > 1 and len(securities[i]) < 5):
            price = rec[securities[i]]
            price[pos] = float(securities[i + 1])
pos = (pos + 1) % numEntries
return pos


def pollingThreadAction():
    print("Running polling thread.")
    while (True):
        # time.sleep(.001)
        record(records, currentIndex)
        ++currentIndex % numEntries


def startPollingThread():
    args = []
    try:
        thread.start_new_thread(pollingThreadAction, args)
    except:
        print("Error: unable to start polling thread")
