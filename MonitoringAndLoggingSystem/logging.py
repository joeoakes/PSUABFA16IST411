
# logging.py
# author: IST411 Group 2
# 9/8/2016

class Log:
	
	def __init__(self, origin_id, log_code, log_subject, log_message, timestamp, time_to_live, checksum,log_type)
		self.origin_id = origin_id
		self.log_code = log_code
		self.log_subject = log_subject
		self.log_message = log_message
		self.log_timestamp = timestamp
		self.log_ttl = time_to_live
		self.log_checksum = checksum
		self.log_type = log_type
		
	def displayLog(self)
		print "ID: ", self.origin_id, "Code: ", self.log_code, "Subject: ", self.log_subject, "Message: ", self.log_message, "Time: ", self.log_timestamp, "Checksum: ", self.log_checksum

	#This method stores the log in a database for future use
	def WriteToDB(self):
