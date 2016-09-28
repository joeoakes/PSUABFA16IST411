# xbee uses serial port communication to broadcast
# pty device is a pseudo-teletype 
# tty is a real teletype serial port
# to show your pty $ ps -ef | grep pts
# Create Virtual Serial Port
# sudo apt-get install socat
# Terminal 1
# socat -d -d pty,raw,echo=0 pty,raw,echo=0
# Terminal 2
# cat < /dev/pts/2
# Terminal 3
# echo "Test" > /dev/pts/3 

import serial
#ser = serial.Serial('/dev/ttyUSB0', 9600)
ser = serial.Serial('/dev/pty/19', 9600)
string = 'Hello from Raspberry Pi'
print(string)
ser.write('%s\n' % string)
while True:
    incoming = ser.readline().strip()
    print(incoming)
    ser.write('RPi Received: %s\n' % incoming)
