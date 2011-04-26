#!/usr/bin/env python
"""
remind.py - Phenny Listener Module
Copyright 2011, Luke Zapart
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import os, re, time, threading
import socket

HOST = 'localhost'        # Symbolic name meaning all available interfaces
PORT = 40037              # Arbitrary non-privileged port
CHANNEL = '#archfinch'

def setup(phenny): 
    def monitor(phenny): 
        time.sleep(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            while True:
                data = conn.recv(1024)
                phenny.msg(CHANNEL, data)
                if not data: break
            conn.close()

    targs = (phenny,)
    t = threading.Thread(target=monitor, args=targs)
    t.start()

def listen(phenny, input):
    pass

listen.commands = ['listen']

if __name__ == '__main__': 
   print __doc__.strip()
