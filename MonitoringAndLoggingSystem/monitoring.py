# monitoring.py
# author: IST411 Group 2
# 9/8/2016

import json
import datetime
from Message import Message
import threading
import time
import queue

subsys_ids = {'brs':'Braking System','clc':'Climate Control System', 'ems':'Energy Management System', 'ccs':'Command and Control System', 'mls':'Monitoring and Logging System', 'cns':'Connectivity and Notification System', 'dts':'Drivetrain System', 'lts':'Lighting System', 'sac':'Safety and Access Control System'}

#This class is in charge of monitoring the communications between modules in
#the automobile and checking them for health or other patterns. This module
#also has the capability to intermittedly request status updates from other
#modules and to send alerts if something isn't working correctly
class Monitor:
    
    #stores last time subsystems sent out message to comm. bus
    subsys_last_heard = {}
    
    #time in milliseconds for watchdog to ask for subsystem status
    timeout_warning = 2000
    
    #time in milliseconds for watchdog to declare subsystem unresponsive
    timeout_critical = 5000


    #This method initializes Monitor instance, setting the "last_heard" 
    #times for each subsystem to the time when the monitor was started
    def __init__(self):
        self.start_monitor_time = datetime.datetime.now()
        for subsys in subsys_ids:
            self.subsys_last_heard[subsys] = self.start_monitor_time

        

        exitFlag = 0
        
        #Method converts json string to a message object. Needs to add error handling for impropper json formatting
        def ConvertFromJSON(json_string):
            contents = json.loads(json_string)
            return Message(contents['CID'], contents['OID'], contents['DID'], contents['HC'], contents['TTL'], contents['PLD'], contents['TS'], contents['CKS'])

        #Threading setup
        class myThread (threading.Thread):
            def __init__(self, threadID, name, q):
                threading.Thread.__init__(self)
                self.threadID = threadID
                self.name = name
                self.q = q
            def run(self):
                print ("Starting " + self.name)
                process_data(self.name, self.q)
                print ("Exiting " + self.name)

        def process_data(threadName, q):
            while not exitFlag:
                queueLock.acquire()
                if not workQueue.empty():
                    object = ConvertFromJSON(q.get())
                    if object.CompareChecksum():
                        print ("%s: Processed %s > %s : %s::" % (threadName, subsys_ids[object.origin_id], subsys_ids[object.destination_id], object.payload))
                    else:
                        print("%s processing checksum error" % (threadName))
                
                queueLock.release()
                time.sleep(1)


        threadList = ["Thread-1", "Thread-2", "Thread-3"]
        messageList = ['{"CID": "car10393", "HC": 1, "DID": "brs", "CKS": "8fcffdcd1c1dbd62c199aa2a13c9043a", "TTL": 100, "OID": "ccs", "PLD": "payload: This message format defined by subteams", "TS": "1475104399.039066"}',
                       '{"CID": "car10393", "HC": 2, "DID": "mls", "CKS": "8fcffdcd1c1dbd62c199aa2a13c9043a", "TTL": 100, "OID": "ccs", "PLD": "payload: This message format defined by subteams", "TS": "1476102339.032081"}', 
                       '{"CID": "car10393", "HC": 3, "DID": "dts", "CKS": "8fcffdcd1c1dbd62c199aa2a13c9043a", "TTL": 100, "OID": "ccs", "PLD": "payload: This message format defined by subteams", "TS": "1475104399.039066"}', 
                       '{"CID": "car10393", "HC": 4, "DID": "ems", "CKS": "8fcffd1c1dbd62c199aa13c9043azdsd", "TTL": 100, "OID": "ccs", "PLD": "payload: This message format defined by subteams", "TS": "1475104399.039066"}' 
                       ]
        queueLock = threading.Lock()
        workQueue = queue.Queue(10)
        threads = []
        threadID = 1

        # Create new threads
        for tName in threadList:
            thread = myThread(threadID, tName, workQueue)
            thread.start()
            threads.append(thread)
            threadID += 1

        # Fill the queue
        queueLock.acquire()
        for message_received in messageList:
            workQueue.put(message_received)
        queueLock.release()

        # Wait for queue to empty
        while not workQueue.empty():
            pass

        # Notify threads it's time to exit
        exitFlag = 1

        # Wait for all threads to complete
        for t in threads:
            t.join()
        print ("Exiting Main Thread")



    #This method takes a serial json representation of a message that is 
	#intercepted on the communication bus and attempts to turn it into a
	#local message object. If successful, returns object and also updates
	#the "lastHeardFrom" time for the subsystem from which the message 
	#originated from.                
    def CreateNewMessage(self, recieved_message):
        pass
    
    #This method sends a ping to the destination subsystem as a status
	#request to see that the subsystem is still functioning and healthy
	#To implement, create a new message object and populate it with the
	#correct data (universal code needed for status update request)
    def PingSystem(self, destination_id):
        pass
    
    #This method sets the last time the subsystem in question broadcasted 
	#a message. This is vital to reset this time for the watchdog to work
    def SetLastHeardFrom(self, origin_id):
        pass
        
    #This method returns the last time the subsystem in question broadcaste a message. 
    def GetLastHeardFrom(self, subsystem_id):
        pass
    
    #This method compares the last time each subsystem has communicated
	#with the current system time. If the difference is greater than a
	#set time limit, the method calls PingSystem(subsystem_id) in an 
	#attempt to see if everything is still functioning properly. If even
	#more time passes, this method calls ThrowUnresponsiveError()
    def CheckWatchdog(self):
        pass
    
    #This method sends out an error message to warn the driver that a 
	#subsystem is unresponsive if it hasn't sent a status update over 
	#a set period of time
    def ThrowUnresponsiveError(self, subsystem_id):
        pass


mon = Monitor()
