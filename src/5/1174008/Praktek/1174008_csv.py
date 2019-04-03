# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 18:34:12 2019

@author: PERSONAL
"""

import csv

def bacacsv():
    with open('uji.csv',mode='r') as csv_file:
        baca = csv.DictReader(csv_file)
        for row in baca:
            print(row['jarak'])

bacacsv()