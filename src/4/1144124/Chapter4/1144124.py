# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 18:45:27 2019

@author: Rahmatul Ridha
"""
#Membaca File CSV dengan Fungsi reader dengan library CSV
import csv

with open('teori.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row[0], row[1], row[2])
        
#Membaca File CSV dengan Fungsi DictReader dengan library CSV
import csv

with open('teori.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['npm'], row['nama'], row['kelas'])
        
#Menulis File CSV dengan Fungsi writer dengan library CSV    
import csv

with open('teori2.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['npm', 'nama', 'kelas'])
    csv_writer.writerow(['1144124', 'Anggreini Kharisma', 'D4TI2B'])
    csv_writer.writerow(['1144016', 'Dino Maulana Putra', 'D4TI2C'])

#Menulis File CSV dengan Fungsi DictWriter dengan library CSV
import csv

with open('teori3.csv', mode='w') as csv_file:
    fieldnames = ['npm', 'nama', 'kelas']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'npm': '1144002', 'nama': 'Anne Marie', 'kelas': 'D4TI2A'})
    writer.writerow({'npm': '1144065', 'nama': 'Lisa', 'kelas': 'D4TI2A'})
    
#Membaca File CSV dengan Fungsi read_csv dengan Library Pandas
import pandas

df = pandas.read_csv('teori.csv')
print(df)

#Menulis File CSV dengan Fungsi to_csv dengan Library Pandas
import pandas

df = pandas.read_csv('teori.csv')
df.to_csv('teori4.csv')
    