# Program for calendar

import calendar

yy = 2014
mm = 11


yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))