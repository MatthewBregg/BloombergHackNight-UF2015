__author__ = 'Ryan'
import socket
from sklearn.externals import joblib
import time
import numpy as np


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

#Records past prices for all tickers
#Input: (rec) hash map <ticker,list_of_prices> and (pos) current position
#Output: current position
def record(rec:dict,pos:int) -> int:
    x = run("___","____", "SECURITIES")
    securities = x.split(" ")
    securities.pop(0)
    for i in range(0,len(securities)):
        if(securities[i] != '3.0E-4' and securities[i] != '0.005'):
            if(len(securities[i]) > 1 and len(securities[i]) < 5):
                price = rec[securities[i]]
                price[pos] = float(securities[i+1])
    pos = (pos+1) % 1000
    return pos
records =  {'AAPL': np.zeros(1000), 'ATVI': np.zeros(1000), 'EA': np.zeros(1000),'FB': np.zeros(1000), 'GOOG': np.zeros(1000), 'MSFT': np.zeros(1000), 'SBUX': np.zeros(1000), 'SNY': np.zeros(1000), 'TSLA': np.zeros(1000),'TWTR': np.zeros(1000)}
pos = 0
pos = record(records,pos)