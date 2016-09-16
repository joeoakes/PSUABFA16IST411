# Author: Joe Oakes
# Date: 9/14/2016
# Course: IST 440W
# Purpose: Show how to hash python objects 
# Version: 1.0

import md5
m = md5.new()
m.update('{"employes":[{"firstName":"John", "lastName":"Doe"},{"firstName":"Anna", "lastName":"Smith"},{"firstName":"Peter", "lastName":"Jones"}]}')
dstring = m.hexdigest()
print(dstring)

# More optimized
print(md5.new('{"employees":[{"firstName":"John", "lastName":"Doe"},{"firstName":"Anna", "lastName":"Smith"},{"firstName":"Peter", "lastName":"Jones"}]}').hexdigest())

import json
basic_entry = {}
basic_entry['id'] = 256
basic_entry['title'] = 'the circle'
jstring = json.dumps(basic_entry)
basic_entry = json.loads(jstring)
print(basic_entry['title'])

print(md5.new(json.dumps(basic_entry)).hexdigest())
