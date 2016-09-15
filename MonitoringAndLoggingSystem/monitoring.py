# monitoring.py
# author: IST411 Group 2
# 9/8/2016

import json
import md5
import logging.py

#This class is in charge of monitoring the communications between modules in
#the automobile and checking them for health or other patterns. This module
#also has the capability to intermittedly request status updates from other
#modules and to send alerts if something isn't working correctly
class Monitor:


	def __init__(self):
	
	
	#This method sends a ping to the destination subsystem as a status
	#request to see that the subsystem is still functioning and healthy
	def PingSystem(self, destination_id):


	#This method sets the last time the subsystem in question broadcasted 
	#a message. This is vital to reset this time for the watchdog to work
	def SetLastHeardFrom(self, origin_id):


	#This method returns the last time the subsystem in question broadsted
	#a message. 
	def GetLastHeardFrom(self, subsystem_id):
	
	
	#This method sends out an error message to warn the driver that a 
	#subsystem is unresponsive if it hasn't sent a status update over 
	#a set period of time
	def ThrowUnresponsiveError(self, subsystem_id):


#This class is used to store the actual messages coming in to the monitoring
#device. 
class Message:

	def __init__(self, origin_id, destination_id, health_code, timestamp, time_to_live, checksum):
		self.origin_id = origin_id
		self.destination_id = destination_id
		self.health_code = health_code
		self.timestamp = timestamp
		self.ttl = time_to_live
		self.checksum = checksum

	def RecieveCommand(self):

	def RecieveHealth(self, health_code):
		self.health_code = health_code
	
	def PingSystem(destination_id)
	
	
	#This method creates a logfile for the current message
	def SendToLog(self):
	

	#This method builds a json representation of the monitored data
	#and calculates the md5 checksum of the serialized json
	#Returns calculated checksum
	def CalculateChecksum(self):
		message = {}
		message['origin_id'] = self.origin_id
		message['destination_id'] = self.destination_id
		message['health_code'] = self.health_code
		message['timestamp'] = self.timestamp
		message['time_to_live'] = self.ttl
		message['checksum'] = self.checksum
		json_message = json.dumps(message)
		calc_checksum = md5.new(json_message).hexdigest()
		return calc_checksum

	#This method verifies that the checksum sent in the original
	#message matches the one that is calculated in CalculateChecksum()
	#Returns boolean value
	def VerifyChecksum(self):
		calc_checksum = CalculateChecksum()
		if calc_checksum == self.checksum:
			print('Message recieved correctly')
			return True
		else:
			print('Message corrupted')
			return False
