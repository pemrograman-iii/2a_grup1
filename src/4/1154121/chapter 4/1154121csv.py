# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:29:21 2019

@author: tomy prawoto
"""
import csv

#Jawaban No. 1
def bukaModeListCsv():
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])

#Jawaban No. 2            
def bukaModeDictCsv():
    with open('data.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['Nama'], row['Umur'], row['Alamat'])

def tulisCsv():
    with open('data.csv', mode='w') as csv_file:
        fieldnames = ['Nama', 'Umur', 'Alamat']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'Nama': 'tomy', 'Umur': '21', 'Alamat': 'borma'})
        writer.writerow({'Nama': 'tiara', 'Umur': '22', 'Alamat': 'cimahi'})
        
bukaModeDictCsv()