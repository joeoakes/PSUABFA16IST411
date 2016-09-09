# Enter notification classes here 
# define notification classes
class Connected_notification
	def cell_connection (self,Cellular)
		devicename=''		
		if (self.Cellular == True)
		print('The %s is now connected to the cellular network' % devicename)
		else 
		print ('No Cellular device is connected at the moment')
		return devicename
	def blue_connection (self,Bluetooth)
		devicename_phone=''
		if(self.Bluetooth == True)
		print('This %s is now connected via Bluetooth ' % devicename_phone )
		else
		print ('No device connected. \n Please turn on bluetooth on your device.')
		return devicename_phone
#probably how a connection notification class should look like
"""
Notification properties
-------
messageCode: UC - Update Car

Methods
----------
"""
