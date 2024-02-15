import Widgets.pcdStudio
import serial


ser = serial.Serial(port='COM8', baudrate=9600)
print(ser.readline(16))

#Widgets.pcdStudio.test()


