# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 00:36:59 2019

@author: Tomy Prawoto
"""

#Ketrampilan Pemrograman
#No.1
def printNPM(npm):
    
    npm = list(str(npm))
    
    angka1 = {"0":" ###### ", "1":"  ##", "2":" ####### ", "3":" ####### ", "4":"     ###", "5":"########", "6":" ####### ", "7":"#########", "8":" ####### ", "9":" #######"}
    angka2 = {"0":"###  ###", "1":"####", "2":"##    ###", "3":"##    ###", "4":"   #####", "5":"##      ", "6":"###      ", "7":"     ### ", "8":"###   ###", "9":"##    ###"}
    angka3 = {"0":"###  ###", "1":" ###", "2":"     ### ", "3":"    #### ", "4":" ###  ##", "5":"####### ", "6":"######## ", "7":"    ###  ", "8":" ### ### ", "9":"##    ###"}
    angka4 = {"0":"###  ###", "1":" ###", "2":"    ###  ", "3":"    #### ", "4":"########", "5":"     ###", "6":"###   ###", "7":"   ###   ", "8":" ### ### ", "9":" ########"}
    angka5 = {"0":"###  ###", "1":" ###", "2":"  ####   ", "3":"##    ###", "4":"     ###", "5":"##   ###", "6":"###   ###", "7":"  ###    ", "8":"###   ###", "9":"      ###"}
    angka6 = {"0":" ###### ", "1":" ###", "2":"#########", "3":" ####### ", "4":"     ###", "5":" ###### ", "6":" ####### ", "7":" ###     ", "8":" ####### ", "9":" ####### "}
              
    hasil1 = []
    hasil2 = []
    hasil3 = []
    hasil4 = []
    hasil5 = []
    hasil6 = []
              
    for x in npm:
        hasil1.append(angka1[x])
        hasil2.append(angka2[x])
        hasil3.append(angka3[x])
        hasil4.append(angka4[x])
        hasil5.append(angka5[x])
        hasil6.append(angka6[x])
    
    print(*hasil1, sep=' ')
    print(*hasil2, sep=' ')
    print(*hasil3, sep=' ')
    print(*hasil4, sep=' ')
    print(*hasil5, sep=' ')
    print(*hasil6, sep=' ')
    

#No 2
def perulangan(npm):
    hitung = 0
    while(hitung < 21):
        print("Halo, "+str(npm)+" apa kabar?")
        hitung = hitung +1


#No 3
def printNPMTigaDijit(npm):
    ulang = 1
    sampai = list(map(int, npm[4:7]))
    sampai = sum(sampai)    
    while(ulang <= sampai):
        print("Halo, "+str(npm[-3:])+" apa kabar?")
        ulang += 1
    

#No 4
def perulangan_3_digit_terakhir(npm):
    npm = str(npm)
    bil = npm[-3]  
    print("Halo, "+bil+" apa kabar?")

#No 5
def down(npm):
    for i in npm:
        print (i)


#No 6
def penjumlahan(npm):
    jumlah = 0
    for i in npm:
        jumlah += int(i)
    print(str(jumlah)+" Adalah hasil penjumlahan")


#No 7
def perkalian(npm):
    jumlah = 0
    for i in npm:
        jumlah *= int(i)
    print(str(jumlah)+" Adalah hasil perkalian")


#No 8
def genap():
    npm = [1,1,5,4,1,2,1]
    for i in npm:
        if (i % 2) == 0:
            print("Bilangan Genapnya : "+str(i))

#No 9 
def ganjil():
    npm = [1,1,5,4,1,2,1]
    for i in npm:
        if (i%2)==1:
            print("Bilangan Ganjilnya : "+str(i))

#No 10
def prima(npm):
    npm = str(npm)
    bil = npm[2]
    num = int(bil)
    if num > 1:
        for i in range(2,num):
            if (num%i)==0:
                print("Bukan Bilangan Prima")
                break
            else:
                print("Bilangan Primanya :"+str(num))
    else:
        print("Tidak Ada Bilangan Prima")