# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:38:47 2019

@author: Rahmatul Ridha
"""

import csv

#Jawaban No. 1
def bukaModeListCsv():
    with open('teori.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])

#Jawaban No. 2            
def bukaModeDictCsv():
    with open('teori.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'], row['nama'], row['kelas'])

#Jawaban No. 8
def buatBacaCsv():
    