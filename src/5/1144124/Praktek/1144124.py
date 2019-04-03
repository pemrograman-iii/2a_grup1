import serial

def tryExceptError():
    try:
        ser = serial.Serial('COM5',9600)
        print(sre.readline().decode("utf-8").strip('\n').strip('\r'))
    except SyntaxError:
        print("Kesalahan penulisan syntax")
    except:
        print("Terjadi sebuah kesalahan")
        
tryExceptError()
