import this #Zen of python
from datetime import date
from datetime import time
from datetime import datetime
# Get today's date from datetime class
today = datetime.now()
print(today)
# Get the current time
t = datetime.time(datetime.now())
print("The current time is", t)
#weekday returns 0 (monday) through 6 (sunday)
wd = date.weekday(today)
#Days start at 0 for monday
days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print("Today is day number %d" % wd)
print("which is a " + days[wd])
now= datetime.now() #get the current date and time
#%c - local date and time, %x-local's date, %X- local's time
print(now.strftime("%c"))
print(now.strftime("%x"))
print(now.strftime("%X"))
#%I/%H - 12/24 Hour, %M - minute, %S - second, %p - local's AM/PM
print(now.strftime("%I:%M:%S %p")) # 12-Hour:Minute:Second AM
print(now.strftime("%H:%M")) # 24-Hour:Minute
