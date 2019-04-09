from matplotlib import pyplot as plt

def tryExceptError():
    try:
        a=[1,2,3,4]
        y=[5,2,4,6]        
        plt.plot(x,y)        
        plt.show()        
    except SyntaxError:
        print("Kesalahan terdapat pada penulisan syntax")
    except NameError:
        print("Variable tersebut tidak ada")
    except TypeError:
        print("Tipe data yang dimasukkan salah")
    except:
        print("Terjadi sebuah kesalahan")
        
tryExceptError()