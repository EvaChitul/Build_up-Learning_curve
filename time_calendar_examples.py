import time

local_time = time.asctime (time.localtime(time.time()))
print (local_time)

import calendar

cal = calendar.month(1989, 9)
print ('Here is the calendar the month you were born: ')
print (cal)