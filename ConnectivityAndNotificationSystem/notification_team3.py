LITHIUMKWHPACKFULL = 100
LITHIUMKWHPACKHIGH = 75
LITHIUMKWHPACKMEDIUM = 50
LITHIUMKWHPACKLOW = 25
NOTIFYLEVEL = ''

class notificationLevel:
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
