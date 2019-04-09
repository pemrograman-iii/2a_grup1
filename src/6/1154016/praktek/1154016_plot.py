from matplotlib import pyplot as plt

def plot():

    hasil = 1154016 % 3 + 2
    
    x = [2014,2015,2016,2017,2018,2019]
    y = [76,87,105,122,148,170]
    x2 = [2014,2015,2016,2017,2018,2019]
    y2 = [78,97,114,134,146,167]
    
    for i in range(1, hasil+1):
        plt.subplot(2,2,i)
        plt.plot(x,y,'b',label='Team Captain America', linewidth=1)
        plt.plot(x2,y2,'r',label='Team Iron Man',linewidth=1)
        plt.title('Civil Wars')
        plt.ylabel('Jumlah Pendukung')
        plt.xlabel('Tahun')
        plt.legend()
        plt.grid(True,color='k')
        plt.subplots_adjust(wspace=.4, hspace=.7)
    
    plt.show()
    
