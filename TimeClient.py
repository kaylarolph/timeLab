t1 = Time(3,54,23)
t2 = Time(8,34,49)
print(t1.getHours())
print(t1.getMinutes())
print(t1.getSeconds())
print(t1.toString())
print(t1.timeInSeconds())
t1.changeTheTime(14,22,48)
print(t1.toString())
print(t1.twelveHourClock())
print(t1.whatTimeIsIt())
print(t1.compareTo(t2))
print((t2.timeTill(t1)).toString())
