__author__ = 'johnmichaelreed2'
import thread
import time
import JohnsPollingThread

def buyingThreadAction():
    print("Running buying thread.")
    #ASK <ticker> <price> <shares> - place a new ask.
    #Output format: ASK_OUT DONE or ERROR Not Enough Shares Owned
    # def run(user, password, *commands):
    while(True):
        for(x in range(0, 10)):
            print("Hi")


def startBuyingThread():
    args = []
    try:
        thread.start_new_thread(buyingThreadAction, args)
    except:
        print("Error: unable to start thread")
