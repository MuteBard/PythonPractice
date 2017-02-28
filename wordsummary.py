#What if there is a comma, period, quotes or more directly in front and behind a word? Tokenize handles that
def Tokenize(paragraph):
    #split() splits all whitespaces if the parameters are empty
    listofWords = paragraph.split()
    cleanedlistofWords = []

    #go through every single character of the paragraph
    for word in listofWords:
        word = word.lower()
        #if the last character of the word is not a letter of the alphabet (cap or not)
        lastChar = word[len(word)-1]
        if (not(ord(lastChar) >= 97 and ord(lastChar) <= 122)):
            #then slice that part off
            finalword = word[0:len(word)-1]
            #and reassign the word to its new truncated value
            word = finalword
        #if the first character of the word is not a letter of the alphabet (cap or not)
        firstChar = word[0]
        if (not(ord(firstChar) >= 97 and ord(firstChar) <= 122)):
            finalword = word[1:len(word)]
            word = finalword
        cleanedlistofWords.append(word)
    return cleanedlistofWords


def wordHistogram(listofWords):
    wordHistogram = {}
    for word in listofWords:

        # when there are no values in key s to get, make the first value 0.
        # then right after add by 1. now the key at letterhistogram has incremented by one value
        # loop through the entire word, treating each character as a key and record occurances as
        # the value

        wordHistogram[word] = wordHistogram.get(word,0)+1
    return wordHistogram

#long variables because this for loop is cryptic and I need all the help i can get
def printHistogram(dictionary):

    # for each character, bring up the values of the occurances at each character
    # key within the dictionary in question

    for word, occurances in dictionary.items():
         print "%d occurances of %s" % (occurances,word)



listofWords = Tokenize(raw_input("Enter a Paragraph: "))
printHistogram(wordHistogram(listofWords))
