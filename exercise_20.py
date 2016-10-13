from sys import argv

script, filename = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print line_count, f.readline()

def print_arbitrary_line(line_count,lines):
    print lines[line_count]

current_file = open(filename)

print "First, let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines: "
current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# save all lines in the file into lines list
# set the file read Head pointer to start of file, so readlines will read the
# lines from begin of file to end of file
rewind(current_file)
lines = current_file.readlines()
lines_num = len(lines)

print "The number of lines in the %r: %d" % (filename,lines_num)

line_id = int(raw_input("Please input a line number that you want to display: "))
print_arbitrary_line(line_id-1,lines)


