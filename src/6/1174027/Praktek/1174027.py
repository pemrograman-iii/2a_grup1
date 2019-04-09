# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 18:03:49 2019

@author: Aegis
"""

def tryExceptError():
    try:
        from p1174027_bar import batang as bar
    except SyntaxError:
        print("Terjadi kesalahan penulisan")

tryExceptError()