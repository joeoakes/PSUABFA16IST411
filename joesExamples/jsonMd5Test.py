# Author: Joe Oakes
# Date: 9/14/2016
# Course: IST 440W
# Purpose: Show how to hash python objects 

import md5
m = md5.new()
m.update('{"employees":[{"firstName":"John", "lastName":"Doe"},{"firstName":"Anna", "lastName":"Smith"},{"firstName":"Peter", "lastName":"Jones"}]}')
dstring = m.hexdigest()
print(dstring)

# More optimized
print(md5.new('{"employees":[{"firstName":"John", "lastName":"Doe"},{"firstName":"Anna", "lastName":"Smith"},{"firstName":"Peter", "lastName":"Jones"}]}').hexdigest())

import json
basic_entry = {}
basic_entry['id'] = 256
basic_entry['title'] = 'the circle'
print(json.dumps(basic_entry))

print(md5.new(json.dumps(basic_entry)).hexdigest())
