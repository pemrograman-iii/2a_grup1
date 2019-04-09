# In[1]: Jawaban No. 2
from matplotlib import pyplot as plt
 
x=[2, 4, 6]
y=[10, 11, 6]

plt.plot(x,y)

plt.show()

# In[2]: Bar Graph

from matplotlib import pyplot as plt

plt.bar([2012.7,2013.7,2014.7,2015.7,2016.7],[9000,9500,10000,15000,20000],
label="Samsung",color='b',width=.3)
plt.bar([2013,2014,2015,2016,2017],[20000,25000,30000,35000,40000],
label="Nokia",color='r',width=.3)
plt.bar([2013.3,2014.3,2015.3,2016.3,2017.3],[2000,2500,3000,3500,4000],
label="Iphone",color='g',width=.3)
plt.legend()
plt.xlabel('Tahun')
plt.ylabel('Jumlah Pengguna')
plt.title('Pengguna Ponsel Seluler Dari Tahun ke Tahun')
plt.show()

# In[3]: Histogram

import matplotlib.pyplot as plt
orang = [11,22,16,9,10,15,22,55,62,45,21,22,32,37,78,23,56,67,78,8,3,78,34,67,23,324,234,43,544,54,33,223]
umur = [0,10,20,30,40,50,60]
plt.hist(orang, umur, histtype='bar', rwidth=0.8)
plt.xlabel('Umur')
plt.ylabel('Jumlah Orang')
plt.title('Histogram')
plt.show()

# In[4]: Scatter Plot

import matplotlib.pyplot as plt
x = [1,1.5,2,2.5,3,3.5,3.6]
y = [7.5,8,8.5,9,9.5,10,10.5]
 
x1=[8,8.5,9,9.5,10,10.5,11]
y1=[3,3.5,3.7,4,4.5,5,5.2]
 
plt.scatter(x,y, label='pendapatan rendah simpanan tinggi',color='r')
plt.scatter(x1,y1,label='pendapatan tinggi simpanan rendah',color='g')
plt.xlabel('simpanan dalam ratusan')
plt.ylabel('pendapatan dalam ribuan')
plt.title('Scatter Plot')
plt.legend()
plt.show()

# In[5]: Area plot

import matplotlib.pyplot as plt
hari = [1,2,3,4,5]
  
kuliner =[7,8,6,11,7]
kuliah = [2,3,4,3,4]
bioskop =[7,8,7,2,5]
nongkrong = [8,5,7,8,13]
  
plt.plot([],[],color='c', label='Kuliner', linewidth=5)
plt.plot([],[],color='m', label='Kuliah', linewidth=5)
plt.plot([],[],color='y', label='Biokop', linewidth=5)
plt.plot([],[],color='k', label='Nongkrong', linewidth=5)
  
plt.stackplot(hari,kuliner,kuliah,bioskop,nongkrong, colors=['c','m','y','k'])
  
plt.xlabel('x')
plt.ylabel('y')
plt.title('Kegiatan Sehari-hari')
plt.legend()
plt.show()

# In[6]: Pie Plot

import matplotlib.pyplot as plt
 
days = [1,2,3,4,5]
 
kuliner =[7,8,6,11,7]
kuliah = [2,3,4,3,7]
bioskop =[7,8,7,2,4]
nongkrong = [2,5,3,4,6]
potong = [7,8,2,12]
kegiatan = ['Kuliner','Kuliah','Bioskop','Nongkrong']
kolom = ['c','m','y','g']
 
plt.pie(potong,
  labels=kegiatan,
  colors=kolom,
  startangle=90,
  shadow= True,
  explode=(0,0,0.2,0),
  autopct='%1.1f%%')
 
plt.title('Kegiatan Sehari-hari')
plt.show()

# In[7]: Line

from matplotlib import pyplot as plt
 
y = [4000,6000,10000,7000,14000,17000,20000]
x = [2013,2014,2015,2016,2017,2018,2019]
plt.plot(x,y)
plt.title('Pemakai Handphone Samsung')
plt.ylabel('Tahun')
plt.xlabel('Jumlah Pemakai Handphone Samsung')
plt.show()

# In[8]: Jawaban No. 4

from matplotlib import pyplot as plt

x = [2015,2016,2017,2018,2019]
y = [76,87,105,122,148]
x2 = [2015,2016,2017,2018,2019]
y2 = [78,97,114,134,146]
plt.plot(x,y,'r',label='Team Iron Man', linewidth=1)
plt.plot(x2,y2,'g',label='Team Aquaman',linewidth=1)
plt.title('Marvel')
plt.ylabel('Jumlah Pendukung')
plt.xlabel('Tahun')
plt.legend()
plt.grid(True,color='k')
plt.show()

# In[8]: Jawaban No. 5

import numpy as np
import matplotlib.pyplot as plt
 
t = np.arange(0.0, 9.0, 1)
s = [1,2,3,4,5,6,7,8,9]
 
for i in range(1, 10):
    plt.subplot(3,3,i)
    plt.xticks([]), plt.yticks([])
    plt.title('subplot(2,3,'+str(i)+')')
    plt.plot(t,s,'-y')
 
plt.show()

# In[5]: Jawaban No. 7

import matplotlib.pyplot as plt
orang = [13,19,26,29,31,36,40,48,51,57,67,69,71,78,88,111,115,80,75,65,54,44,43,42,48,50,29,14,68,21,22,34]
umur = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(orang, umur, histtype='bar', rwidth=0.8)
plt.xlabel('Umur')
plt.ylabel('Jumlah Orang')
plt.title('Histogram')
plt.show()