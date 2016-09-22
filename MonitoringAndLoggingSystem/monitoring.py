# monitoring.py
# author: IST411 Group 2
# 9/8/2016

import json
import datetime
from Message import Message

#This class is in charge of monitoring the communications between modules in
#the automobile and checking them for health or other patterns. This module
#also has the capability to intermittedly request status updates from other
#modules and to send alerts if something isn't working correctly
class Monitor:
    
    subsys_ids = {'Braking':'BR','Climate Control':'CC', 'Energy Management':'EM', 'Command':'CO', 'Control':'CN', 'Monitoring':'MN','Logging':'LG', 'COnnectivity':'CT', 'Notification':'NT', 'Drivetrain':'DT', 'Lighting':'LT', 'Safety and Access':'SA'}
    
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
            subsys_last_heard[subsys] = start_monitor_time
    
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
