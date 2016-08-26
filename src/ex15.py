from sys import argv

script,filename=argv

txt = open(filename)


print "here is your filename %r" %filename
print txt.read()
txt.close()

print "file %s  has been closed" %filename
print "type the filename again:"
file_again=raw_input("> ")

txt_again=open(file_again)

print  txt_again.read()
txt_again.close()  #file closed

print "file %s  has been closed" %file_again
