# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:12:32 2019

@author: PERSONAL
"""

def tryExceptError():
    try:
        from p1174008_bar import batang as bar
    except SyntaxError:
        print("Terjadi Kesalahan Penulisan")

tryExceptError()