def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    # From the output of 'print args',we can draw the conclusion
    # that the parameters are organized by tuple in args
    print args

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothing."

print_two("Tom","Cat")
print_two_again("Tom","Cat")
print_one("First")
print_none()