# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 00:23:42 2019

@author: JONVITER
"""
import csv
import pandas

def bacacsvlist():
    with open('1154016.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f' {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t NPM {row[0]} Bernama \ {row[1]} Belajar dikelas {row[2]}.')
                line_count += 1

def bacacsvdictionary():
    with open('1154016.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f' {", ".join(row)}')
                line_count += 1
            print(f'\t NPM : {row["name"]} Nama : {row["department"]} Belajar Dikelas : {row["birthday month"]}.')
            line_count += 1

def nulis():
    with open('test-tulis.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        
        employee_writer.writerow(['Astuti', 'Ibu rumah tangga', 'April'])

def bacalistpandas():
    df = pandas.read_csv('1154016.csv')
    print(df)