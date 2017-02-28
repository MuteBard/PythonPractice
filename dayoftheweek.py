
#version1
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

day_number = int(raw_input("Please Enter a Day number (0-6) : "))
if (day_number < 0 and day_number > 7):
    day_number = int(raw_input("Please Enter A Valid Day number (0-6)"))
print days[day_number]

"""
#version2
day_number = int(raw_input("Please Enter a Day number (0-6) : "))
if (day_number < 0 and day_number > 7):
    day_number = int(raw_input("Please Enter A Valid Day number (0-6)"))

if (day_number == 0):
    print "Sunday"
elif(day_number == 1):
    print "Monday"
elif(day_number == 2):
    print "Tuesday"
elif(day_number == 3):
    print "Wednesday"
elif(day_number == 4):
    print "Thursday"
elif(day_number == 5):
    print "Friday"
else:
    print "Saturday"
"""
