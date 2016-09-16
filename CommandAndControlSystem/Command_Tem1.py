#Author: Matt Smith
#Command Python File
#This is essentially going to handle messages between Pi systems and pripority.

#Last Update: 9/15/2016

import md5 
import json

message = "Team 1 Is The Best"

class Command:

	def hashing(self, message):
		m = md5.new()
		m.update(message)
		dstring = m.hexdigest()
		print(dstring)

	def json(self):
		basic_entry = {}
		basic_entry['id'] = 256
		basic_entry['title'] = 'the circle'
		print(md5.new(json.dumps(basic_entry)).hexdigest())


hash = Command()
hash.hashing(message)
hash.json()

