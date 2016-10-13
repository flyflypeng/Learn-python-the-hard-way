from sys import argv
from os.path import exists

script,from_file,to_file = argv

print "Copy from %s to %s" % (from_file,to_file)

# Open from_file and read data in the from_file
in_file = open(from_file,'r')
in_data = in_file.read()

print "The input file is %d bytes long." % len(in_data)

print "Does output file exists? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file,'w')
out_file.write(in_data)

print "Alright, all done."
out_file.close()
in_file.close()