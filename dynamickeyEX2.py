#first use of recursion

# What I want the user to do is enter a name, have that name serve as the key
dictionary_of_persons = {}

#a function that deals with input error checking
def validatedInput(choice):
    while(True):
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print "This input is invalid"

# unnessary creation of a function here but this is for my own benefit to serve
# how you can create a list to a key (in this case addingInterests(name)),
# which refers to yet another. Return a list of interests
def addingInterests(name):
    i = 1
    interests = []
    while(True):
        anInterest = (raw_input("\tEnter %s's interests. Interest %d (or Type Q to finish adding)" % (name, i))).lower()
        if (anInterest == "q"):
            return interests
        else:
            interests.append(anInterest)
        i += 1

#create a key and add it to the dictionary_of_persons
def createPerson():
    personKey = raw_input("Enter the name of the person: ")
    name = personKey
    email = raw_input("\tEnter %s's email: "% name)
    interests = addingInterests(name)

    choice1 = (raw_input("\tDo you want to list %s's friends? (Y  N): "% name)).lower()
    #if the answer is no, return the dictionary
    if validatedInput(choice1) == False:
        dictionary_of_persons[personKey] = (name,email,interests)
        return dictionary_of_persons
    #if the answer is yes, enter a loop
    elif validatedInput(choice1) == True:
        #keep adding friends if..
        while(True):
            #create the friend
            friend = createPerson()
            #make a choice whether to continue adding friends under the current person's name
            choice2 = (raw_input("\tDo you want to add another of %s's friends? (Y  N): " % name)).lower()
            #if not, return this dictionary under this person's key
            if (validatedInput(choice2) == False):
                dictionary_of_persons[personKey] = (name,email,interests,friend)
                return dictionary_of_persons

# a single call of createperson() just creates one key of one person. However, if they have friends,
# it may possess a key to other people

#traversing this would be HELL in a for loop
createPerson()
print dictionary_of_persons["Ramit"][1]
print dictionary_of_persons["Ramit"][2][0]
print (dictionary_of_persons["Ramit"][3])["Jasmine"][1]
print (dictionary_of_persons["Ramit"][3])["Jan"][2][1]

# ramit@gmail.com
# movies
# jasmine@yahoo.com
# tv
