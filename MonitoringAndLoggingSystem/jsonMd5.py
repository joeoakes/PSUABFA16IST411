#Author: Chaitali Patel
#Date: 09/15/16
#Course: IST 440W


import md5
m = md5.new()
m.update('{"System ID":[{"systemID1":"Team 1 Breaking System", "systemID2":"Team 2 Drivetrain System"},{"systemID3":"Team 3 Climate Control System", "systemID4":"Team 4 Lighting System"},{"systemID5":"Team 5 Energy Management System", "systemID6":"Team 6 Safety & Access Control System"}]}')
dstring = m.hexdigest()
print(dstring)

# Optimized no objects were needed to perform hash
print(md5.new('{"Command Codes":[{"AB":"Apply Brakes", "SL":"Signal Lights"},{"AG":"Apply Gas", "BL":"Brake Lights"},{"EL":"Emergency Lights", "HL":"Headlights"}]}').hexdigest())

# Serialize python object into JSON
import json
