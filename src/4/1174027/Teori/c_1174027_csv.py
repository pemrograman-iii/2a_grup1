# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:40:00 2019

@author: Aegis
"""
import csv
import pandas

def bacacsvlist():
    with open('1174027.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f' {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t Orang Ini Memiliki NPM {row[0]} Bernama \ {row[1]} Berada Dikelas {row[2]}.')
                line_count += 1

def bacacsvdictionary():
    with open('1174027.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f' {", ".join(row)}')
                line_count += 1
            print(f'\t Orang Ini Memiliki NPM : {row["name"]} Bernama : {row["department"]} Berada Dikelas : {row["birthday month"]}.')
            line_count += 1

def nulis():
    with open('test-tulis.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        employee_writer.writerow(['Ucok', 'Tukang', 'November'])
        employee_writer.writerow(['Udin', 'Mandor', 'April'])

def bacalistpandas():
    df = pandas.read_csv('1174027.csv')
    print(df)
