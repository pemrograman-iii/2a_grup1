# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:59:03 2019

@author: Aegis
"""
from matplotlib import pyplot as plt

x=[2,4,6]
y=[1,3,5]

#plt.plot(x,y)
#plt.show
#line

#plt.bar([1,3,5,7,9],[50,40,70,80,20],
#label="Lamborghini",color='Y',width=.5)
#plt.bar([2,4,6,8,10],[80,20,20,50,60],
#label="VW", color='C',width=.5)
#plt.legend()
#plt.xlabel('Days')
#plt.ylabel('Distance (kms)')
#plt.title('Information')
#plt.show()
#bar

#population_age = [40,80,11,22,16,9,10,15,22,55,62,45,21,22,102,95,85,55,110,120,70,80,75,65,54,39,32,41,46,44]
#bins = [0,10,20,30,40,50,60,70,80,90,100]
#plt.hist(population_age, bins, histtype='bar', rwidth=0.8)
#plt.xlabel('age groups')
#plt.ylabel('Number of people')
#plt.title('Histogram')
#plt.show()
#histogram

#x = [1,1.5,2,2.5,3,3.5,3.6]
#y = [7.5,8,8.5,9,9.5,10,10.5]
 
#x1=[8,8.5,9,9.5,10,10.5,11]
#y1=[3,3.5,3.7,4,4.5,5,5.2]
 
#plt.scatter(x,y, label='Pendapatan Tinggi Tapi Penyimpanan Rendah',color='C')
#plt.scatter(x1,y1,label='Pendapatan Rendah Tapi Penyimpanan Tinggi',color='M')
#plt.xlabel('Pensimpanan dalam ratusan')
#plt.ylabel('Pendapatan dalam ribuan')
#plt.title('Diagram Titik')
#plt.legend()
#plt.show()
#scatter

#poe = [1,2,3,4,5,6,7]
  
#molord =[7,8,6,8,7,9,10]
#dahar = [2,3,4,3,2,3,4]
#gawe =[7,8,7,2,2,6,0]
#ulin = [8,5,7,8,13,15,25]
  
#plt.plot([],[],color='m', label='Molord', linewidth=5)
#plt.plot([],[],color='c', label='Dahar', linewidth=5)
#plt.plot([],[],color='r', label='Gawe', linewidth=5)
#plt.plot([],[],color='k', label='Ulin', linewidth=5)
  
#plt.stackplot(poe, molord,dahar,gawe,ulin, colors=['m','c','r','k'])
  
#plt.xlabel('Hari')
#plt.ylabel('Berapa Lama')
#plt.title('Stack Plot')
#plt.legend()
#plt.show()
#stack plot

poe = [1,2,3,4,5,6,7]
 
sare =[7,8,6,11,7,8,9]
dahar = [2,3,4,3,2,7,5]
gawe =[7,8,7,2,2,4,2]
ulin = [8,5,7,8,13,7,15]
slices = [7,2,2,13]
activities = ['sare','dahar','gawe','ulin']
cols = ['c','m','r','b']
 
plt.pie(slices,
  labels=activities,
  colors=cols,
  startangle=0,
  shadow= True,
  explode=(0.1,0.1,0.1,0.1),
  autopct='%1.1f%%')
 
plt.title('Pie Plot')
plt.show()
#diagram Pie

#x = [1,2,3,4,5,6,7,8,9,10]
#y = [10,20,30,40,50,60,70,80,90,100]
#plt.subplot(221)#tinggi,lebar,urutan
#plt.plot(x, y)
#plt.subplot(222)
#plt.bar(x, y)
#plt.subplot(223)
#plt.hist(x, y)
#plt.subplot(224)
#plt.scatter(x, y)
#plt.show()
#subplot