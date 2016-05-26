#!/usr/bin/python

import serial
import time
import socket
from datetime import datetime
from time import gmtime, strftime

def getNetworkIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('www.google.com', 0))
    return s.getsockname()[0]

def main():
    s = serial.Serial('/dev/ttyACM0', 115200, timeout=.1)
    time.sleep(2)

    while True:
        ip_string = "IP:" + getNetworkIp()
        hostname_string = socket.gethostname()
        t = strftime("%Y-%m-%d\\%H:%M:%S", gmtime())
        s.write(hostname_string + '\\' + ip_string + '\\' + t)
        time.sleep(1)
        print s.read(3)

    s.close()

if __name__ == '__main__':
    main()
