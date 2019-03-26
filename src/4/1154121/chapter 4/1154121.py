# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 18:45:27 2019

@author: vanerz
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
    csv_writer.writerow(['1174002', 'Steve Rodger', 'D4TI2C'])
    csv_writer.writerow(['1174003', 'Robert Downey Junior', 'D4TI2B'])

#Menulis File CSV dengan Fungsi DictWriter dengan library CSV
import csv

with open('teori3.csv', mode='w') as csv_file:
    fieldnames = ['npm', 'nama', 'kelas']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'npm': '1174009', 'nama': 'Alan Walker', 'kelas': 'D4TI2A'})
    writer.writerow({'npm': '1174010', 'nama': 'Hardwell', 'kelas': 'D4TI2A'})
    
#Membaca File CSV dengan Fungsi read_csv dengan Library Pandas
import pandas

df = pandas.read_csv('teori.csv')
print(df)

#Menulis File CSV dengan Fungsi to_csv dengan Library Pandas
import pandas

df = pandas.read_csv('teori.csv')
df.to_csv('teori4.csv')
    
#Fungsi Try Except 
def bacaCsvPandas():
    try:
        df = pandas.read_csv('teori.csv')
        print(dt)
    except SyntaxError:
        print("Kesalahan penulisan syntax")
    except NameError:
        print("Variable tersebut tidak ada")
    except TypeError:
        print("Tipe data salah")
    except:
        print("Terjadi sebuah kesalahan")

bacaCsvPandas()