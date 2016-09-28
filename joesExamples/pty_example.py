import os, pty, serial

master, slave = pty.openpty()
print(master)
print(slave)
s_name = os.ttyname(slave)
ser = serial.Serial(s_name)

mystring = "Hello IST 411"
# Covert to bytes
b = mystring.encode('utf-8')

# To Write to the device
ser.write(b)
# To read from the device
bstring = os.read(master,1000)
print(bstring)
