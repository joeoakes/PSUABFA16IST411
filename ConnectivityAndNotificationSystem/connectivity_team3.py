import bluetooth
import socket
import threading
import queue
import bluetooth
import time

class ConnectToServer:

	def __init__(self, input_queue, output_queue):
        	threading.Thread.__init__(self)
        	self.input_queue = input_queue
        	self.output_queue = output_queue
		self.HOST = ''
        	self.PORT = 8888
        	self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        	self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        	try:
            		self.s.bind((self.HOST, self.PORT))
		except socket.error, msg:
            		print "Binding socket failed, error message: " + msg[1]

	target_name = "My Phone"
	target_address = None

	data_sent = False

	while True:
		nearby_devices = bluetooth.discover_devices()

		for bdaddr in nearby_devices:
			if target_name == bluetooth.lookup_name( bdaddr ):
				target_address = bdaddr
           			 break
		if (target_address is not None) and (not data_sent):
'''print "found target bluetooth device with address ", target_address 
 send_data()'''
			data_sent = True
		else:
'''print "could not find target bluetooth device nearby"
to mark 'connection dropped''''
			data_sent = False
		time.sleep(1)

def BACKUP_CONNECTION(self,connection):
#function for a back up connection in the even the first connection fails 
