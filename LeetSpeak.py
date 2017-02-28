"""
create a function to change charaters to leet

create a for loop that accesses each character

"""


# make an original string and a copy that will be constantly edited
string = "I'm so glad that our counterpick tree finally grew and sprouted fruitful counterpicky counterpicks. I mean, imagine, we can make counterpickade, key counterpick pie counterpick meringue pie. i think it's the most valuable piece of property that we have. i think we should go to the bank and get a loan, actually I think we should go to the bank and get the loan, actually i think we should just get counterpick tree insurance and then get a loan and use the counterpick tree as collateral because it is now insured. I truly do love our counterpick tree. Just imagin a likfe full of counterpick trees, and all our beautiful counterpicks, endless possiblities. They're so beautiful, I wish I was a counterpick. you wish you were a counterpick? if you were a counterpick i would put you on my shelf and cherish you like I cherish all our counterpick. that's so beautiful, like I only hope that the whores aren't stealing our counterpicks you know those naughty whores always steals counterpicks. we do have a couple of counterpick whores in this community, those damn counterpick-stealing whores I hate them no one will take our prized counterpicks from us. Hey, has it been about 10 secounds since we looked at out counterpick tree? It has been about 10 seconds till we looked at our counterpick tree. hey what the fuck"
string2 = string

#look at the current character within the string list and check whether it can be a leet character
#if so then replace it with leet
def leetfy(s):
    s = s.upper()
    if (s == 'A'):
        s = '4'
    elif (s == 'E'):
        s = '3'
    elif (s == 'G'):
        s = '6'
    elif (s == 'I'):
        s = '1'
    elif (s == 'O'):
        s = '0'
    elif (s == 'S'):
        s = '5'
    elif (s == 'T'):
        s = '7'
    return s


#takes in the current index, the leet character and the entire string to insert the Leet character in
#splits the string like this: left = contents to the left of undesired character, right = contents to the right of undesired character
# then add contents to the left of undesired character + Leet character + contents to the right of undesired character

#you could have used stg.replace, smh

def swapChar(index, c, stg):
    left= ""
    right= ""
    i = 0

    while (i < len(stg)):
        if (i < index):
            left += stg[i]
        #i dont want to include the index, it is explictly left out
        elif(i > index):
            right += stg[i]
        i += 1
    #print (left + c + right)
    return left + c + right



x = 0
#theres no parentheses in a for loop
#take in the string and loop through it to swap the characters in for leet speak
for char in string:
    #update the revised string that will have Leet speak
     string2 = swapChar(x ,leetfy(char), string2)
     x += 1
print string2
