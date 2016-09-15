# Enter notification classes here 
# define notification classes

import hashlib

class Connected_notification
	def cell_connection (self,Cellular)
		devicename=''		
		if (self.Cellular == True):
		print('The %s is now connected to the cellular network' % devicename)
		else :
		print ('No Cellular device is connected at the moment')
		return devicename
	def blue_connection (self,Bluetooth)
		devicename_phone=''
		if(self.Bluetooth == True):
		print('This %s is now connected via Bluetooth ' % devicename_phone )
		else:
		print ('No device connected. \n Please turn on bluetooth on your device.')
		return devicename_phone
	def usb_connection (self,fltirelow,frtirelow,rltirelow,rrtirelow)
		Tire=''
		''' Check tire pressure function has to be created'''
		while (tirepressurelow == True )
			if (self.fltirelow == True):
			Tire = 'Front Left tire'
			print('The %s needs air ' % Tire )
			elif (self.frtirelow == True):
                        Tire = 'Front Right tire'
			print ('The %s needs air ' % Tire )
			elif (self.rltirelow == True):
                        Tire = 'Rear Left tire'
                        print('The %s needs air ' % Tire )
                        elif (self.rrtirelow == True):
                        Tire = 'Rront Right tire'
                        print ('The %s needs air ' % Tire )
	def tms_notification(self,USB)
                device=''
                if (self.USB == True):
                print('The %s is now connected through USB' % device)
                else:
                print ('No device is connected through USB')
                return device
	

#probably how a connection notification class should look like for emergency
LITHIUMKWHPACKFULL = 100
LITHIUMKWHPACKHIGH = 75
LITHIUMKWHPACKMEDIUM = 50
LITHIUMKWHPACKLOW = 25
NOTIFYLEVEL = ''

class notification_level:
    def __init__(self,kwhLevel):
        self.kwhLevel = 100

    def notifykwhLevel(kwhLevel):
        if kwhLevel <= LITHIUMKWHPACKLOW:
            NOTIFYLEVEL = 'CRITICAL'
            print (NOTIFYLEVEL)
        elif kwhLevel <= LITHIUMKWHPACKMEDIUM:
            NOTIFYLEVEL = 'HIGH'
            print(NOTIFYLEVEL)
        elif kwhLevel <= LITHIUMKWHPACKHIGH:
            NOTIFYLEVEL = 'MEDIUM'
            print(NOTIFYLEVEL)
        elif kwhLevel <= LITHIUMKWHPACKFULL:
            NOTIFYLEVEL = 'LOW'
            print(NOTIFYLEVEL)
## probabaly how a notification level is calculated for the battery


##probably how a connection notification class should look like for system/mant
redAlert = 100 #send notice on phone / manufa / dealer
orange= 75 # send notice on phone
lightOn= 50 # turn on lights in display
lightBlink= 25 # blinking lights for 10-15 mins when car starts
sMlevel = entrylogbook

class systemMant_notic:
## need idea of getting notic from logbook :(


)

class Notification:
#variables to keep track of the car; initally assumes that the car is 100% functional
#Priority for alert; The higher the number, the more of a priority it is to inform the user
HIGH_ALERT = 10
MED_ALERT = 5
LOW_ALERT = 1

#Fuel levels
LOW_FUEL = 10
MED_FUEL = 50
FUEL_LEVEL = 100
# Default settings for a car that's turned on; if settings are true, implied that is turned on. if false, it is turned off

L_LIGHT = true
R_LIGHT = true

TRDOOR = true
BRDOOR = true
TLDOOR = true
BLDOOR = true

TRWHEEL = 100
BRWHEEL = 100
TLWHEEL = 100
BLWHEEL = 100

OIL_LEVEL = 100
TRUNK = true

SEATBELT = true

# TL = TOP LEFT
# BL = BOTTOM LEFT
# TR = TOP RIGHT
# BR = BOTTOM RIGHT

# Constructor that sets up the variables
def _init_self(self, fuel, seatbelt, trunk, bldoor, brdoor, fldoor, bldoor, l_light, r_light, trwheel, brwheel, tlwheel, blwheel):

# Notification if gas is extremely low
if fuel <= LOW_FUEL:
	ALERT_SYSTEM(HIGH_ALERT, "FUEL IS EXTREMELY LOW!")
	self.FUEL_LEVEL = fuel

elif fuel <= MED_FUEL && fuel > LOW_FUEL:
	ALERT_SYSTEM(MED_ALERT, "Fuel is at 50%")
	self.FUEL_LEVEL = fuel

#Alert for seatbelt
if seatbelt == false:
	self.SEATBELT = false
	ALERT_SYSTEM(LOW_ALERT, "Please put you seatbelt on")

# Alert for when trunk is open
if trunk == false: 
	self.TRUNK = false
	ALERT_SYSTEM(LOW_ALERT, "Trunk is open")

doorCheck(bldoor, fldoor, brdoor, frdoor)

if l_light == false:
	self.L_LIGHT = false
	ALERT_SYSTEM(HIGH_ALERT, "Left Light is broken.")

if r_light == false:
	self.R_LIGHT = false
	ALERT_SYSTEM(HIGH_ALERT, "Right Light is broken.")


#Alert for car door to see if it open
def doorCheck(bldoor, fldoor, brdoor, frdoor):

if(bldoor == false):
	self.BLDOOR = false
	ALERT_SYSTEM(LOW_ALERT, "Back Left Door is open.")

elif(fldoor == false):
	self.FLDOOR = false
	ALERT_SYSTEM(LOW_ALERT, "Front Left Door is open.")

elif(brdoor == false):
	self.BRDOOR = false
	ALERT_SYSTEM(LOW_ALERT, "Back Right door is open.")
elif(frdoor == false):
	self.FLDOOR = false
	ALERT_SYSTEM(LOW_ALERT, "Front Left door is open.") 
	  
#function for the alarm system to place a priority on which alarms should be displayed more often
def ALERT_SYSTEM(self, priority, message):

#If notification priority is high, displays notfication more often
if(priority >= HIGH_ALERT):
#some code to show the noitfication for whatever it is more often

elif(priority <= MED_ALERT && priority > LOW_ALERT):
# some code

else
#some code


"""
Notification properties
-------
messageCode: UC - Update Car

Methods
----------
"""
