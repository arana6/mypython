x = 'there are %d types of people' % 10
binary = "Binary"
do_not = "Don't"
y   = "those who know %s and those who %s" % (binary, do_not)

print x
print y

print "I said: %r." %x
print "I also said : %s" %y

hilarious=False
joke_evaluation="isn't that joke funny?! %r"

print joke_evaluation % hilarious

w = "this is the left side of..."
e   =   "a  string with a right side"

print w+e
