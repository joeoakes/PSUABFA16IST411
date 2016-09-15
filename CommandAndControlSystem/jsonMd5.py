import md5
m = md5.new()
m.update('{"employees":[{"firstName":"John", "lastName":"Doe"},{"firstName":"Anna", "lastName":"Smith"},{"firstName":"Peter", "lastName":"Jones"}]}')
dstring = m.hexdigest()
print(dstring)

# Optimized no objects were needed to perform hash
print(md5.new('{"employees":[{"firstName":"John", "lastName":"Doe"},{"firstName":"Anna", "lastName":"Smith"},{"firstName":"Peter", "lastName":"Jones"}]}').hexdigest())

# Serialize python object into JSON
import json
basic_entry = {}
basic_entry['id'] = 256
basic_entry['title'] = 'the circle'
print(json.dumps(basic_entry))

# Serialize python object and perform hash all in one line
print(md5.new(json.dumps(basic_entry)).hexdigest())
