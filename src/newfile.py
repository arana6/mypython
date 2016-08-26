filename=raw_input("Enter name for new File : ")
target=open(filename,'w')

target.write(raw_input("Enter content for the new file"))

target.close()

print "\nlets read the contents of the file again\n"

target_read=open(filename)

print target_read.read()


print "all cool, lets close it"
target_read.close()
    
