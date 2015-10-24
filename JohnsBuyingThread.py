__author__ = 'johnmichaelreed2'
import thread
import time


def buyingThreadAction():
    print("Running buying thread.")
    assert ()


def startBuyingThread():
    args = []
    try:
        thread.start_new_thread(buyingThreadAction, args)
    except:
        print("Error: unable to start thread")
