
import md5
m = md5.new()
m.update('{"System ID":[{"systemID1":"Team 1 BS", "systemID2":"Team 2 CSS"},{"systemID3":"Team 3 EMS", "systemID4":"Team 4 DS"},{"systemID5":"Team 5 LS", "systemID6":"Team 6 SACS"}]}')
dstring = m.hexdigest()
print(dstring)

# Optimized no objects were needed to perform hash
print(md5.new('{"Command Codes":[{"AB":"Apply Brakes", "SL":"Signal Lights"},{"AG":"Apply Gas", "BL":"Brake Lights"},{"EL":"Emergency Lights", "HL":"Headlights"}]}').hexdigest())

# Serialize python object into JSON
import json
basic_entry = {}
basic_entry['id'] = 256
basic_entry['title'] = 'the circle'
print(json.dumps(basic_entry))

# Serialize python object and perform hash all in one line
print(md5.new(json.dumps(basic_entry)).hexdigest())
