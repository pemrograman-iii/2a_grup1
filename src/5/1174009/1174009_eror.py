# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 18:03:49 2019

@author: Dwi
"""

import serial

def tryExceptError():
    try:
        ser = serial.Serial('COM6',9600)
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
    except TypeError:
        print("Terjadi ketidaksamaan type")

tryExceptError()