# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:17:26 2019

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
