# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:37:29 2019

@author: Aegis
"""

import serial

def ulang():
    ser = serial.Serial('COM6',9600)
    while(1):
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))

ulang()