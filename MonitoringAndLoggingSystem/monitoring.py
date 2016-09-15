# monitoring_iakimenko.py
# author: IST411 Group 2
# 9/8/2016

import json
import md5

class Monitor:

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
