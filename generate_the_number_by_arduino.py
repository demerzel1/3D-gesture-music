# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 09:33:33 2017

read the port and generate the file.

@author: Bruce Feynman
"""
def main():
    import serial
    addr = 'COM3'
    baudrate = 9600
    timeout = 1

    dev = serial.Serial()
    
    dev.baudrate = baudrate
    dev.port = addr
    dev.timeout = timeout
    dev.open()
    dev.readline()
    cnt=1
    notes=[]
    while cnt<=10:
        '''
        s=bytes(dev.read(1)).decode('ascii')
        dev.read(2)
        print(s)
        '''
        s=bytes(dev.readline()).decode('ascii')
        if not s=='':
            cnt=cnt+1
            a=int(s)
            notes.append(a)
    dev.close()
    return notes


