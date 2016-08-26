from sys import argv

script,filename =argv

print "we are gonna delete %r" %filename
print "if you dont want that press Ctrl-C(^c) else hit return"
raw_input("?")
print "Opening file: %r" %filename
target = open(filename,"w")
print "now to delete the file"
target.truncate()

print "Now enter 3 lines"
line1=raw_input("Line1 : ")
line2=raw_input("Line2 : ")
line3=raw_input("Line3 : ")

print "Now these lines are going to be added to the file"

target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")


print "Now closing the updated file"
target.close()


print "lets read the updated file"
read_target_filename=raw_input("Enter file name")

read_target=open(read_target_filename)

print read_target.read()


print "cool its updated \n Lets close it now"
read_target.close()

print "The End"
