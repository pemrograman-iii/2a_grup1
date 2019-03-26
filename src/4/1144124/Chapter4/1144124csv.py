# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:38:47 2019

@author: rahmatul ridha
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

def tulisCsv():
    with open('teori6.csv', mode='w') as csv_file:
        fieldnames = ['npm', 'nama', 'kelas', 'tanggal lahir']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'npm': '1144124', 'nama': 'Justin', 'kelas': 'D4TI3C', 'tanggal lahir': '05/05/1995'})
        writer.writerow({'npm': '1144003', 'nama': 'Jisoo', 'kelas': 'D4TI3B', 'tanggal lahir': '06/06/1996'})
