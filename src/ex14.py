from sys import argv

script,user_name=argv

prompt  =   '>'
print "Hi %s , I'm  the %s script" %(user_name,script)

print "I'd like to ask you few questions\n"

print "Do you like working in python %s" %user_name

likes=raw_input(prompt)

print "Where do you live %s" %user_name
lives =raw_input(prompt)

print "what type of system do you have %s" %user_name
computer =raw_input(prompt)

print"""
Alright , you said %r about liking python.
you live in %r.Not sure where that is.
and you have a %r system,nice.""" %(likes,lives,computer)
