# monitoring.py
# author: IST411 Group 2
# 9/8/2016

import json
import md5
import logging.py
import datetime

#This class is in charge of monitoring the communications between modules in
#the automobile and checking them for health or other patterns. This module
#also has the capability to intermittedly request status updates from other
#modules and to send alerts if something isn't working correctly
class Monitor:
	
	#stores dictionary of subsystem IDs for message interpretation
	subsys_ids = {'Braking':'BR','Climate Control':'CC', 'Energy Management':'EM', 'Command':'CO', 'Control':'CN', 'Monitoring':'MN','Logging':'LG', 'COnnectivity':'CT', 'Notification':'NT', 'Drivetrain':'DT', 'Lighting':'LT', 'Safety and Access':'SA'}
	
	#stores last time subsystems sent out message to comm. bus
	subsys_last_heard = {}
	
	#time in milliseconds for watchdog to ask for subsystem status
	timeout_warning = 2000

	#time in milliseconds for watchdog to declare subsystem unresponsive
	timeout_critical = 5000
	
	#This method initializes Monitor instance, setting the "last_heard" 
	#times for each subsystem to the time when the monitor was started
	def __init__(self):
		self.start_monitor_time = datetime.datetime.now()
		for subsys in subsys_ids:
			subsys_last_heard[subsys] = start_monitor_time

	#This method takes a serial json representation of a message that is 
	#intercepted on the communication bus and attempts to turn it into a
	#local message object. If successful, returns object and also updates
	#the "lastHeardFrom" time for the subsystem from which the message 
	#originated from.
	def CreateNewMessage(self, recieved_message):
		try:
			#Convert from serial/JSON to message variables
			#Make new message object with variables
			#Call SetLastHeardFrom() to update time of last
			#communication with subsystem
			#Return new message object
		except SerialToJSONConversionError
			print('The serial message was corrupted')
			print('and resulted in an incomplete message object') 
	
	
	#This method sends a ping to the destination subsystem as a status
	#request to see that the subsystem is still functioning and healthy
	def PingSystem(self, destination_id):


	#This method sets the last time the subsystem in question broadcasted 
	#a message. This is vital to reset this time for the watchdog to work
	def SetLastHeardFrom(self, origin_id):


	#This method returns the last time the subsystem in question broadsted
	#a message. 
	def GetLastHeardFrom(self, subsystem_id):


	#This method compares the last time each subsystem has communicated
	#with the current system time. If the difference is greater than a
	#set time limit, the method calls PingSystem(subsystem_id) in an 
	#attempt to see if everything is still functioning properly. If even
	#more time passes, this method calls ThrowUnresponsiveError()
	def CheckWatchdog(self):
	
	
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

	
	#This method creates a logfile for the current message
	def SendToLog(self, log_type):
	

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
