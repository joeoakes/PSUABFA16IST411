import hashlib
import md5
m = md5.new()
m.update('{"employees":[{"firstName":"John", "lastName":"Doe"},{"firstName":"Anna", "lastName":"Smith"},{"firstName":"Peter", "lastName":"Jones"}]}')
dstring = m.hexdigest()
print(dstring)

