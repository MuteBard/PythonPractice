
x = 0
print "you have %d coins." % x


#this program will loop forever unless
while (True):
    #prompt a value
    condition = (raw_input("Do you want another coin?: (yes  no) :")).lower()
    #check the value and promt again if neither yes or no
    while (not(condition == "yes" or condition == "no")):
        condition = (raw_input("Do you want another coin?: (yes  no) :")).lower()
    #the user states that they do not want a coin
    if (condition == "no"):
        break
    #other wise keep adding the value of coins and continue
    else:
        x += 1
        print "You have %d coins." % x,
print "Bye"
