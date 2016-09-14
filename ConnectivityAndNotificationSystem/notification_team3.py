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
	

#probably how a connection notification class should look like
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





"""
Notification properties
-------
messageCode: UC - Update Car

Methods
----------
"""
