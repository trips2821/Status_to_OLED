#!/usr/bin/python

import serial
import time
import socket
from subprocess import Popen,PIPE
import re, dbus, gtk, glib, sys, os

def checkCurrentSsid():
    ssidpat = re.compile('ESSID:"([^"]*)"')
    iwconf = Popen(['iwconfig'], stdout=PIPE).communicate()[0]
    if ssidpat.search(iwconf):
        ssid = ssidpat.search(iwconf).groups()[0]
        print "ssid ....... " +ssid

	return ssid

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
        ssid = checkCurrentSsid()
        s.write(ssid + '\\' + hostname_string + '\\' + ip_string)
        time.sleep(10)
        print s.read(3)

    s.close()

if __name__ == '__main__':
    main()
