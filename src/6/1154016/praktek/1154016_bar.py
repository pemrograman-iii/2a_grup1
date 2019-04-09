from matplotlib import pyplot as plt

def bar():

    hasil = 1154016 % 3 + 2
    
    for i in range(1, hasil+1):
        plt.subplot(2,2,i)
        plt.bar([2012.7,2013.7,2014.7,2015.7,2016.7,2017.7],[9000,9500,10000,15000,20000,25000],
        label="Mac",color='b',width=.3)
        plt.bar([2013,2014,2015,2016,2017,2018],[20000,25000,30000,35000,40000,45000],
        label="Windows",color='r',width=.3)
        plt.bar([2013.3,2014.3,2015.3,2016.3,2017.3,2018.3],[2000,2500,3000,3500,4000,4500],
        label="Linux",color='g',width=.3)
        plt.legend()
        plt.xlabel('Tahun')
        plt.ylabel('Jumlah Pengguna')
        plt.title('Pengguna OS Dari Tahun ke Tahun')
        plt.subplots_adjust(wspace=1, hspace=.7)
        
    plt.show()
    