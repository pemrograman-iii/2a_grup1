# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 19:06:40 2019

@author: PERSONAL
"""

import serial

def baca():
    ser = serial.Serial("COM6",115200)
    baca = ser.readline()
    print(baca)

baca()