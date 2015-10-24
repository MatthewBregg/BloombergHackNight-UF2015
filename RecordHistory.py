__author__ = 'Ryan'
import socket
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn.externals import joblib
import time
import numpy as np
import random
import string

def sellAllShares(tickers,record):
    for ticker in tickers:
        stock,shares = hasStock(ticker)
        if(stock):
            my_cash = getCash()
            price = record[ticker]['bid'] - 1
            result = run("___","____", "ASK " + ticker + " " + str(price) + " " + str(shares))
            print("SELL : " + ticker + " " +  str(price) + " " + str(shares))

def sellAllSharesMod(ticker,record,prev_tic,offset):
    stock,shares = hasStock(ticker)
    if(stock):
        if(prev_tic == ticker):
            offset += 0.01
        else:
            offset = 1
        my_cash = getCash()
        price = record[ticker]['bid'] - offset
        result = run("___","____", "ASK " + ticker + " " + str(price) + " " + str(shares))
        print("SELL : " + ticker + " " +  str(price) + " " + str(shares) + " OFFSET : " + str(offset) )
    return ticker,offset
        

def buyAllShares(ticker,record):
        my_cash = getCash()
        stock,shares = hasStock(ticker)
        if(my_cash > 100):
            price = float(record[ticker]['ask']) + 1
            shares = int(my_cash*0.7/price)
            result = run("___","____", "BID " + ticker + " " + str(price) + " " + str(shares)) 
            print("BUY : " + ticker + " "+   str(price) + " " + str(shares))     


import random
def sellRandom(record,tickers):
    if(len(tickers) == 0):
        return
    i = random.randint(0,len(tickers)-1)
    print(str(i) + " : " + str(len(tickers)))
    stock,shares = hasStock(tickers[i])
    if(stock):
        my_cash = getCash()
        shares = random.randint(1,shares)
        price = record[tickers[i]]['bid'] - 1
        result = run("___","____", "ASK " + tickers[i] + " " + str(price) + " " + str(shares))
        print("SELL : " + tickers[i] + " " +  str(price) + " " + str(shares))

def buyRandom(record,tickers,toSell):
    i = random.randint(0,len(tickers)-1)
    print(str(i) + " : " + str(len(tickers)))
    stock,shares = hasStock(tickers[i])
    my_cash = getCash()
    if(my_cash > 100):
        price = float(record[tickers[i]]['ask']) + 1
        limit = random.uniform(0.1, 0.4)
        shares = int(my_cash*round(limit, 10)/price)
        result = run("___","____", "BID " + tickers[i] + " " + str(price) + " " + str(shares)) 
        print("BUY : " + tickers[i] + " "+   str(price) + " " + str(shares))
        toSell.append(tickers[i])
    return toSell


def hasStock(ticker):
    result = run("___","____", "MY_SECURITIES")
    securities = result.split(" ")
    securities.pop(0)
    for i in range(0,len(securities)):
            if(securities[i] == ticker and float(securities[i+1]) > 0):
                return True,float(securities[i+1])            
    return False,0

def getCash():
    result = run("___","____", "MY_CASH")
    securities = result.split(" ")
    return float(securities[1])


def run(user, password, *commands):
    HOST, PORT = "codebb.cloudapp.net", 17429


    data=user + " " + password + "\n" + "\n".join(commands) + "\nCLOSE_CONNECTION\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.connect((HOST, PORT))
        sock.sendall(bytes(data, "utf-8"))
        sfile = sock.makefile()
        rline = sfile.readline()
        result =""
        while rline:
            result += rline.strip() + " "
            #print(result)
            rline = sfile.readline()
        return result 

def train(history):
    regressors = dict()
    for key in history.keys():
        regressors[key] = ExtraTreesRegressor(n_estimators=200,min_samples_split=1,random_state=0,n_jobs=8)
    for key in history.keys():
        regressors[key].fit(history[key]['time'],history[key]['net_worth'])
        regressors[key].score(history[key]['time'],history[key]['net_worth'])
    joblib.dump(records, "regression.pkl")


def record():
    records = dict()
    tickers = list()
    pos = 0
    result = run("___","____", "SECURITIES")
    securities = result.split(" ")
    securities.pop(0)
    for i in range(0,len(securities)):
        if(securities[i].isalnum()):
            name = securities[i]
            tickers.append(name)
            records[name] = dict()
    for key in records.keys():
        result = run("___","____", "ORDERS " + key)
        result = result.split(" ")
        records[key]['bid'] = float(result[3])
        records[key]['ask'] = float(result[7]) 
    for i in range(0,len(securities)):
        if(securities[i].isalnum()):
            name = securities[i]
            net_worth = securities[i+1];
            records[name]['net_worth'] = float(net_worth)                  
    #joblib.dump(records, "history.pkl")
    return records

def history_net_worth():
    records =  {'AAPL': dict(), 'ATVI': dict(), 'EA': dict(),'FB': dict(), 'GOOG': dict(), 'MSFT': dict(), 'SBUX': dict(), 'SNY': dict(), 'TSLA': dict(),'TWTR': dict()}
    pos = 0
    for key in records.keys():
        records[key]['time'] = []
        records[key]['net_worth'] = []
    while(True):
        result = run("___","____", "SECURITIES")
        securities = result.split(" ")
        securities.pop(0)
        for i in range(0,len(securities)):
            if(securities[i].isalnum()):
                name = securities[i]
                net_worth = securities[i+1];
                records[name]['net_worth'].append(float(net_worth))
                records[name]['time'].append(float(pos))
        pos += 1
        print(pos)
        #time.sleep(0.5)
        if(pos % 100 == 0):                               
            joblib.dump(records, "history_nw.pkl")

def history():
    records =  {'AAPL': dict(), 'ATVI': dict(), 'EA': dict(),'FB': dict(), 'GOOG': dict(), 'MSFT': dict(), 'SBUX': dict(), 'SNY': dict(), 'TSLA': dict(),'TWTR': dict()}
    pos = 0
    result = run("___","____", "SECURITIES")
    securities = result.split(" ")
    securities.pop(0)
    for key in records.keys():
        records[key]['bid'] = []
        records[key]['ask'] = []
        records[key]['net_worth'] = []
    while(True):
        dict_of_orders = dict()
        for key in records.keys():
            result = run("___","____", "ORDERS " + key)
            result = result.split(" ")
            records[key]['bid'].append(float(result[3]))
            records[key]['ask'].append(float(result[7])) 
        for i in range(0,len(securities)):
            if(securities[i].isalnum()):
                name = securities[i]
                net_worth = securities[i+1];
                records[name]['net_worth'].append(float(net_worth))
        pos += 1
        print(pos)
        if(pos > 10):                               
            joblib.dump(records, "history.pkl")
            pos = 0



def load_history(name):
    records = joblib.load(name + ".pkl")
    return records

#history_net_worth()
#r = load_history("history_nw")
#result = run("___","____", "BID GOOG 1000 1")
#print(hasStock('GOOG'))
#print(hasStock('EA'))
#print(getCash())

#buyAllShares('GOOG',r)
#old_cash = getCash()
#toSell = []
#while(True):
#    new_cash = getCash()
#    print("MY CASH : " + str(new_cash))
#    r,t = record()
#    toSell = buyRandom(r,t,toSell)
#    sellRandom(r,toSell)
#    old_cash = new_cash