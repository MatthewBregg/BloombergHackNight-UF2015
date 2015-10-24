__author__ = 'Ryan'
import socket
from sklearn.externals import joblib
import time
import numpy as np
import random
import string


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
            rline = sfile.readline()
        return result 


def record():
    records =  {'AAPL': dict(), 'ATVI': dict(), 'EA': dict(),'FB': dict(), 'GOOG': dict(), 'MSFT': dict(), 'SBUX': dict(), 'SNY': dict(), 'TSLA': dict(),'TWTR': dict()}
    pos = 0
    result = run("___","____", "SECURITIES")
    securities = result.split(" ")
    securities.pop(0)

    dict_of_orders = dict()
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



def load_history(name):
    records = joblib.load(name + ".pkl")
    return records

rec44 = record()
