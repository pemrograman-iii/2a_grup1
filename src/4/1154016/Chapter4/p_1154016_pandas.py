# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 00:45:13 2019

@author: JONVITER
"""

import pandas

def bacalistpandas():
    df = pandas.read_csv('1154016.csv')
    print(df)

def bacadictpandas():
    df = pandas.read_csv('1154016.csv')
    uji = pandas.DataFrame.from_dict(df)
    print(uji)
    
def standartanggal():
    df = pandas.read_csv('1154016.csv', parse_dates=['date'])
    print(df)

def changeindexcol():
    df = pandas.read_csv('1154016.csv', index_col='npm')
    print(df)

def renameatt():
    df = pandas.read_csv('1154016.csv',
            header=0, 
            names=['Nomor Induk Mahasiswa', 'Name','Class', 'Angkatan'])
    print(df)

def write():
    df = pandas.read_csv('hrdata.csv', 
            index_col='Employee', 
            parse_dates=['Hired'],
            header=0, 
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])
    df.to_csv('p_1154016_pandas_baru.csv')    