
#ensures that all words are words from the alphabet
def validatedInput(word):
    while(True):
        for c in word:
            #if s is not part of the alphabet, capitalized or not,
            if not((ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122)):
                word = raw_input("Try Again. Enter a new word: ")
                break
        return word


def LetterHistogram(word):
    LetterHistogram = {}
    for c in word:

        # when there are no values in key s to get, make the first value 0.
        # then right after add by 1. now the key at letterhistogram has incremented by one value
        # loop through the entire word, treating each character as a key and record occurances as
        # the value

        LetterHistogram[c] = LetterHistogram.get(c,0)+1
    return LetterHistogram

#long variables because this for loop is cryptic and I need all the help i can get
def printHistogram(dictionary):

    # for each character, bring up the values of the occurances at each character
    # key within the dictionary in question

    for character, occurances in dictionary.items():
         print "%d occurances of %s" % (occurances,character)

def getLetterHistogram():



dictionary = {}
word = validatedInput(raw_input("Enter a word: "))
dictionary = LetterHistogram(word)
printHistogram(LetterHistogram(word))
