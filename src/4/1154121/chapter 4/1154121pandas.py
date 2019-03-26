# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:20:47 2019

@author: dezha
"""

import pandas
#Jawaban No. 3
def bukaModeListPandas():
    df = pandas.read_csv('hrdata.csv')
    print(df)

#Jawaban No. 4
def bukaModeDictPandas():
    df = pandas.read_csv('hrdata.csv', 
                index_col='Karyawan', 
                parse_dates=['Masuk'], 
                header=0, 
                names=['Karyawan', 'Masuk','Gaji', 'Jatah Cuti'])
    print(df)
#Jawaban No. 5
def ubahFormatTanggal():
    df = pandas.read_csv('hrdata.csv', parse_dates=['Masuk'])
    print(df)

#Jawaban No. 6
def ubahIndexKolom():
    df = pandas.read_csv('hrdata.csv')
    df.index = ['Row_1', 'Row_2','Row_3','Row_4','Row_5', 'Row_6']
    print(df)

#Jawaban No. 7
def ubahNamaKolom():
    df = pandas.read_csv('hrdata.csv')
    df.columns =['Col_1', 'Col_2', 'Col_3', 'Col_4'] 
    print(df)
    
def tulisCsvPandas():
    df = pandas.read_csv('hrdata.csv', 
            index_col='Karyawan', 
            parse_dates=['Masuk'], 
            header=0, 
            names=['Karyawan', 'Masuk','Gaji', 'Jatah Cuti'])
    df.to_csv('hrdata2.csv')