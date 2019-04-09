# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:47:37 2019

@author: Aegis
"""

from matplotlib import pyplot as coba

print(1174027%3+2)

def batang():
    x = [2,4,6,8,10,12,14]
    y = [15,30,45,60,75,90,105]

    x1 = [10,7,18,9,30]
    y1 = [4,9,12,7,7]

    x2 = [70,60,50,40,30,20,10]
    y2 = [10,20,30,40,50,60,70]

    coba.subplot(221)
    coba.bar(x,y)
    coba.subplot(222)
    coba.bar(x1,y1)
    coba.subplot(223)
    coba.bar(x2,y2)
    coba.show()