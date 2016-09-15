# monitoring_iakimenko.py
# author: Ivan Iakimenko
# 9/8/2016

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

	def SaveTODatabase(self):
		
