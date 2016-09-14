import json
from decimal import Decimal
 
#JSON TO PYTHON OBJECTimport json
from decimal import Decimal

#JSON to PYTHON OBJECT
json_data = '{"name": "Nick", "city": "Philly"}'
python_obj = json.loads(json_data)
print('JSON to PYTHON OBJECT')
print python_obj["name"]
print python_obj["city"]

#PYTHON OBJECT TO JSON
import json
from decimal import Decimal
 
d = {}
d["Name"] = "Nick"
d["Country"] = "Philly"
 
print json.dumps(d, ensure_ascii=False)


