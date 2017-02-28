
#Ceasar Cipher Version 2

cipher = "Lbh zhfg, hayrnea$ Jung 98lbh #unir yrnearq"
list1 = []
list2 = []
factor = 13
index = 0
string = ""

#create the list of the alphabet
for n in range(26):
    list1.append(chr(n+97))

#double the list of the alphabet to not deal with wraping around index 25 and out of bounds
list1.extend(list1)

for n in cipher:

    #if dealing with uppercase letters, change the cipher character into an
    #numerical ascii value. Then add it by the factor. next, because this character
    #is capitalized, subtract by 65 on the ascii table to bring it down to index values
    #that can be interpreted by list1. find the matching index of the number to the
    #character on list1. Append its evaluted value to the growing list2
    if (ord(n) >= 65 and ord(n) <= 90):
         newCharacterNum = ((ord(n)) + factor ) - 65
         deciperedChar = list1[newCharacterNum]
         list2.append(deciperedChar.upper())

    #if dealing with lowercase letters, change the cipher character into an
    #numerical ascii value. Then add it by the factor. next, because this character
    #is lowercase, subtract by 97 on the ascii table to bring it down to index values
    #that can be interpreted by list1. find the matching index of the number to the
    #character on list1. Append its evaluted value to the growing list2
    elif (ord(n) >= 97 and ord(n) <= 122):
        newCharacterNum = ((ord(n)) + factor ) - 97
        deciperedChar = list1[newCharacterNum]
        list2.append(deciperedChar)

    #else leave anything that is not of the alphabet alone, append to list2 as is
    else:
        list2.append(n)

for s in list2:
    string += s
print string
