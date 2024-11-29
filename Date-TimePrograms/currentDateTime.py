# #Current time
# from datetime import datetime
# now = datetime.now()
# currentTime = now.strftime('%H:%M:%S')
# print(f"The current time now is: {currentTime}")

# import time
# t = time.localtime()
# C_time = time.strftime("%H:%M:%S", t)
# print(f"The current time is: {C_time}")

#Date and time
import datetime

currentTime = datetime.datetime.now()

print('The current time now is:')
print('The year is:', currentTime.year)
print('The month is:',currentTime.month)
print('The day is:',currentTime.day)
print('Hour:', currentTime.hour)
print('Minute:',currentTime.minute)
print('Second:',currentTime.second)