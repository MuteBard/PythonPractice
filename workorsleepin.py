
#version1
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

day_number = int(raw_input("Please Enter a Day number (0-6) : "))
if (day_number < 0 and day_number > 7):
    day_number = int(raw_input("Please Enter A Valid Day number (0-6)"))
if(day_number == 0 or day_number == 6):
    print "Sleep in"
else:
    print "Goto work"

"""
#version2
day_number = int(raw_input("Please Enter a Day number (0-6) : "))
if (day_number < 0 and day_number > 7):
    day_number = int(raw_input("Please Enter A Valid Day number (0-6)"))

if (day_number == 0):
    print "Sleep in"
elif(day_number == 1):
    print "Goto work"
elif(day_number == 2):
    print "Goto work"
elif(day_number == 3):
    print "Goto work"
elif(day_number == 4):
    print "Goto work"
elif(day_number == 5):
    print "Goto work"
else:
    print "Sleep in"
"""
