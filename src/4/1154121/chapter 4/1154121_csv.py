# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:15:04 2019

@author: dezha
"""

import csv
#Jawaban No. 1
def bukaModeListCsv():
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Nama kolom {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} memiliki jabatan {row[1]}, dan tinggal di {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')
#Jawaban No. 2            
def bukaModeDictCsv():
    