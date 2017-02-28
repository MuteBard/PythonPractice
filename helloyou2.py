name = raw_input("WHAT IS YOUR NAME? ")
name = name.upper()
name_length = len(name)
sentence = "HELLO, %s\nYOUR NAME HAS %d CHARACTERS IN IT" % (name,name_length)
print sentence
