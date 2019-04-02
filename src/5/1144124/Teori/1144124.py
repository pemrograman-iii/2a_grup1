import serial

def testArduino():
    ser = serial.Serial("COM5", 115200)
    print(ser.name)  

testArduino()