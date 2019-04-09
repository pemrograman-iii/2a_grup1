# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:46:15 2019

@author: Dwi
"""

from matplotlib import pyplot as plt

print(1174009%3+2)

def pie_chart(): 
    aktivity = [1,6,2,4]
    game = [14,1,9]
    txt = [9,2,9,17]
    siapa = ['damcong','dugong','serik','epik']
    dimana = ['rumah','kampus','kosan']
    apa = ['makan','skip','kelas','mudik']
    cols = ['y','c','m','b']

    plt.subplot(221)
    plt.pie(aktivity,
             labels=siapa,
             colors=cols,
             startangle=0,
             shadow= True,
             explode=(0.2,0,0,0),
             autopct='%1.1f%%')
    plt.title('Pie Chart Siapa')
    
    plt.subplot(222)
    plt.pie(game,
             labels=dimana,
             colors=cols,
             startangle=90,
             shadow=True,
             explode=(.3,0.1,0),
             autopct='%1.1f%%')
    plt.title('Pie Chart Dimana')
    
    plt.subplot(223)
    plt.pie(txt,
             labels=apa,
             colors=cols,
             startangle=90,
             shadow=True,
             explode=(.1,0,0,0),
             autopct='%1.1f%%')
    plt.title('Pie Chart Apa')
    plt.show()