
#prompt the user for numerical input in celsius. string is converted to a
#numerical value and assigned cel
cel = int(raw_input("Enter a temperature in celsius (C) : "))

#calculate fahrenheit and assign the value of the expression to far
far = cel * 1.8 + 32

#prints the F equivalent of C
print "%s C in fahrenheit is %s F" % (cel,far)
