#prompts user for a value for bill and enters a while loops if negative value
# is entered until good input

bill = float(raw_input("Enter total bill amount : "))
while(bill < 0):
    bill = float(raw_input("Enter total bill amount : "))

#prompts user for a value for service and enters a while loops if something other
#than good, fair or bad was entered until good input

service = (raw_input("What was you level of service? (good fair bad) : ")).lower()
while(not(service == "good" or service == "fair" or service == "bad")):
    service = (raw_input("What was you level of service? (good fair bad) : ")).lower()


#prints out the calculated tip and bill according to whether service was good, fair or bad
if (service == "good"):
    total = bill*1.20
    tip = bill*.20
    print "good --> 20%s : You gave $%.2f as a tip and $%.2f was your total" % ('%',tip,total)
elif (service == "fair"):
    total = bill*1.15
    tip = bill*.15
    print "fair --> 15%s : You gave $%.2f as a tip and $%.2f was your total" % ('%',tip,total)
else:
    total = bill*1.10
    tip = bill*.10
    print "fair --> 10%s : You gave $%.2f as a tip and $%.2f was your total" % ('%',tip,total)
