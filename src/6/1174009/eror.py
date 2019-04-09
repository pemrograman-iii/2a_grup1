# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:08:21 2019

@author: Dwi
"""

def tryExceptError():
    try:
        from p1174009_titik import batang as bar
    except SyntaxError:
        print("Nah Loh Eror Hayu Benerin")

tryExceptError()