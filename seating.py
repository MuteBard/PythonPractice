import random

#create how large you want the list of numbers
def createList():
    seq = []
    i = 0
    number = 16
    while (i < number):
        seq.append(i)
        i += 1
    return seq


#removal by isolation
def remove(index, seq):
    #create a left side to add values
    left = []
    #create a right side to add values
    right = []
    i = 0

   #while counter i is less than the length of the list
    while  (i < len(seq)):
        #and if the counter i is strictly less than the index we want to get rid of
        if (i < index):
            #print the contents of list the left of the undesired index to left list
            left.append(seq[i])
        #and if the counter i is strictly greater than the index we want to get rid of
        elif (i > index):
            #print the contents of list the right of the undesired index to right list
            right.append(seq[i])
        #keep incrementing to be able to copy all the contents of the list BUT the value at index
        i += 1
    #return the new list, devoid of the index value
    return left+right


def randomSort(seq):
    added = []
    i = 0
    while (i < initialLength):
        #randomly generate a number that is equal to the possible remaining indexes
        #and assign it to index
        index = random.randint(0,len(seq)-1)
        #add the value of that number at the index to the added list,
        added.append(seq[index])
        #using function remove, eliminate that very number using its index to isolate it
        #within list seq. Update seq list to its new contents
        seq = remove(index,seq)
        i += 1

   #theres one last value that random generator could not touch, add the final element
    added.append(seq[0])
    return added

def convertToString(rSeq):
    randStrSeq = []
    for s in rSeq:
        if (s < 10):
            randStrSeq.append("0"+str(s))
        else:
            randStrSeq.append(str(s))
    return randStrSeq

seq = createList()
initialLength = len(seq)-1
randSeq = randomSort(seq)
rSS = convertToString(randSeq);




print "                               FRONT                               "
print "+------+------+ +------+------+     +------+------+ +------+------+"
print "|  %s  |  %s  | |  %s  |  %s  |     |  %s  |  %s  | |  %s  |  %s  |" % (rSS[0],rSS[1],rSS[2],rSS[3],rSS[4],rSS[5],rSS[6],rSS[7])
print "+------+------+ +------+------+     +------+------+ +------+------+"
print "|  %s  |  %s  | |  %s  |  %s  |     |  %s  |  %s  | |  %s  |  %s  |" % (rSS[8],rSS[9],rSS[10],rSS[11],rSS[12],rSS[13],rSS[14],rSS[15])
print "+------+------+ +------+------+     +------+------+ +------+------+"
print "                                BACK                               "
