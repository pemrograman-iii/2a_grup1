# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 08:02:40 2019

@author: Aegis
"""
import pandas

def bacalistpandas():
    df = pandas.read_csv('1174027.csv')
    print(df)

def bacadictpandas():
    df = pandas.read_csv('1174027.csv')
    uji = pandas.DataFrame.from_dict(df)
    print(uji)
    
def standartanggal():
    df = pandas.read_csv('1174027.csv', parse_dates=['ttl'])
    print(df)

def changeindexcol():
    df = pandas.read_csv('1174027.csv', index_col='npm')
    print(df)

def renameatt():
    df = pandas.read_csv('1174027.csv',
            header=0, 
            names=['Nomor Induk Mahasiswa', 'Name','Class', 'Tanggal Lahir'])
    print(df)

def write():
    df = pandas.read_csv('hrdata.csv', 
            index_col='Employee', 
            parse_dates=['Hired'],
            header=0, 
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])
    df.to_csv('p_1174027_pandas_baru.csv')    