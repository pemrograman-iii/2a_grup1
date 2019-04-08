# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:40:56 2019

@author: Dwi
"""

#plt.plot([1,2,3,4], [1,4,9,16])

#no3 
#Garis
x = (4,8,13,17,20)
y = (54, 67, 98, 78, 45)

import matplotlib.pyplot as plt
plt.plot([4,8,13,17,20],[54, 67, 98, 78, 45])
plt.show()

#Scatter
import matplotlib.pyplot as plt
x = [2,4,6,7,9,13,19,26,29,31,36,40,48,51,57,67,69,71,78,88]
y = [54,72,43,2,8,98,109,5,35,28,48,83,94,84,73,11,464,75,200,54]
plt.scatter(x,y)
plt.show()

#Histogram
import matplotlib.pyplot as plt
x = [2,4,6,5,42,543,5,3,73,64,42,97,63,76,63,8,73,97,23,45,56,89,45,3,23,2,5,78,23,56,67,78,8,3,78,34,67,23,324,234,43,544,54,33,223,443,444,234,76,432,233,23,232,243,222,221,254,222,276,300,353,354,387,364,309]
num_bins = 6
n, bins, patches = plt.hist(x, num_bins, facecolor = 'm')
plt.show()

#Pie chart
import matplotlib.pyplot as plt
 
days = [1,2,3,4,5]
 
Turu =[7,8,6,11,7]
Mangan = [2,3,4,3,2]
Kuli =[7,8,7,2,2]
Ulin = [8,5,7,8,13]
slices = [7,2,2,13]
activities = ['turu','mangan','kuli','ulin']
cols = ['c','m','r','b']
 
plt.pie(slices,
  labels=activities,
  colors=cols,
  startangle=90,
  shadow= True,
  explode=(0.1,0,0,0),
  autopct='%1.1f%%')
 
plt.title('Pie Plot')
plt.show()

#area plot
import matplotlib.pyplot as plt
days = [1,2,3,4,5]
  
sleeping =[7,8,6,11,7]
eating = [2,3,4,3,2]
working =[7,8,7,2,2]
playing = [8,5,7,8,13]
  
plt.plot([],[],color='m', label='Turu', linewidth=5)
plt.plot([],[],color='c', label='makan', linewidth=5)
plt.plot([],[],color='r', label='kuli', linewidth=5)
plt.plot([],[],color='k', label='ulin', linewidth=5)
  
plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])
  
plt.xlabel('x')
plt.ylabel('y')
plt.title('Blackpink in your area')
plt.legend()
plt.show()

#subplot
fig, ax = plt.subplots(3, 3, sharex='col', sharey='row')