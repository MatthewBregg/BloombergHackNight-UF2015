import clientpy3
import time
import subprocess
import platform

#From http://stackoverflow.com/questions/2084508/clear-terminal-in-python
def clear():
    subprocess.Popen( "cls" if platform.system() == "Windows" else "clear", shell=True)


while(True):
        print("Cash is : " + str(clientpy3.run("___","____","MY_CASH")))
        print("Securities are : "
              + str(clientpy3.run("___","____","MY_SECURITIES")))
        print("My orders are are : " + str(clientpy3.run("___","____","MY_ORDERS")))
        clientpy3.run("___","____","CLOSE_CONNECTION");
        time.sleep(1)
        clear()

