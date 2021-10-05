class Clock:
# 3 parameters, set all fields to the parameters
#Precondition: All parameters are within normal ranges for hours, minutes, and seconds
    def __init__(self,h,m,s):
        self.h = h
        self.m = m
        self.s = s
    def getHours(self):
        return self.h
    def getMinutes(self):
        return self.m
    def getSeconds(self):
        return self.s
#toString
#* This method returns a String in the format of hour:minute:second
#return  String    	returns the fields in a formatted String
    def toString(self):
        return (str(self.h) + ":" + str(self.h) + ":" + str(self.s))
#* timeInSeconds
#This method converts the Time object into an int of seconds
# Returns the fields all converted into seconds
    def timeInSeconds(self):
        a = self.h*60
        a = a+self.m
        a = a*60
        a = a + self.s
        return a
#changeTheTime
#This method will move replace the current time with another time
#Precondition: All parameters are within normal ranges for hours, minutes, and seconds
# @param    	h       	This is the number of hours
#@param    	m       	This is the number of minutes
#@param    	s       	This is the number of seconds
    def changeTheTime(self, h,m,s):
        self.h = h
        self.m= m
        self.s=s
#* twelveHourClock
#This method will return as a String, the Time object with an am or pm reference
#@return       String    This will be the time, but converted to the am or pm version of the time
    def twelveHourClock(self):
        if(self.h==0) or (self. h==0):
            return (str (self.h+12) + ":" + str(self.m) + ":" + str(self.s) + " AM")
        elif (self.h<=11):
            return(self.toString() + "AM")
        else:
            return (str(self.h-12) + ":" + str(self.m) + ":" + str(self.s) + "PM")
#whatTimeIsIt
#	* Based on the time, return morning, afternoon, evening, or nighttime
#	* @return      String      	if time is between 6-12, return morning
#	*				if time is between 12 - 5 return afternoon
#*				if time is between 5 - 10 return evening
#*				if time is between 10 - 6 return nighttime
    def whatTimeIsIt(self):
        if(self.h >=6) and (self.h<12):
            return "morning"
        elif (self.h >=12) and (self.h<17):
            return "afternoon"
        elif (self.h>=17) and (self.h<22):
            return "evening"
        else:
            return "nighttime"
#compareTo
 #       	* This method compares the Time object that called the method to the Time object parameter
#	* The difference between the two times should be the number of seconds between the two time objects
 #       	* @param    	t       	This is a Time object
 #       	* @return    	int    	negative means the object that called the method is before the parameter
 #       	*                              	positive means the object that called the method is after the parameter
  #      	*                              	zero means the object and the parameter are the same time
    def compareTo(self, t):
        return (self.timeInSeconds() - t.timeInSeconds())
#timeTill
  #      	* This method returns a Time object representing how long from the current time to the parameter Time
  #      	* @parameter          	t       	This Time object represents a time in the future
  #      	* @return  Time      	returns a Time object that represents how long till the Time parameter
    def timeTill(self, t):
        sec = t.compareTo(self)
        hours=sec//3600
        sec = sec-(hours*3600)
        min = sec//60
        min1= min*60
        sec = sec - (min1)
        return(Time(hours,min,sec))



