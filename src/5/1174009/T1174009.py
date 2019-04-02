# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:59:03 2019

@author: Aegis
"""

import serial

def baca():
    ser = serial.Serial("COM6",115200)
    baca = ser.readline()
    print(baca)

baca()