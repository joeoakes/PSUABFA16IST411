import json
import hashlib

'''
Team 3
Ver: 2
Description: This class stores all of the properties of a message developed by Ivan. This will be the main messaging system across all the systems that need to be developed. You can think of it as a standard but there will be improvements over time for sure.
'''

class Message:
    def __init__(self, car_id, origin_id, destination_id, health_code, timestamp, time_to_live, payload, checksum='0'):
        self.car_id = car_id
        self.origin_id = origin_id
        self.destination_id = destination_id
        self.health_code = health_code
        self.timestamp = timestamp
        self.ttl = time_to_live
        self.payload = payload

        if checksum=='0':
            self.checksum = self.CalculateChecksum()
        else:
            self.checksum = checksum

#Returns string JSON representation of current message object based on message formatting standard
    def ConvertToJSON(self):
        contents={'CID':self.car_id,'OID':self.origin_id,'DID':self.destination_id, 'HC':self.health_code, 'TS':self.timestamp, 'TTL':self.ttl, 'CKS':self.checksum}
        contents['PLD']=self.payload
        return json.dumps(contents)
#Returns a md5 checksum based on current payload
    def CalculateChecksum(self):
        return hashlib.md5(self.payload.encode()).hexdigest()

#Returns a boolean based on whether supplied checksum matches self generated value
    def CompareChecksum(self):
        return self.checksum == self.CalculateChecksum()
