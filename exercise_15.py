from sys import argv

script, filename = argv

text = open(filename,"r+")

print "Here's your file %r" % filename
print text.read()
text.close()

print "Type the filename again: "
file_again = raw_input("> ")

text_again = open(file_again,"a+")
text_again.writelines("This is last sentence.")
text_again.flush()
text_again.seek(0)
print text_again.read()
text_again.close()
