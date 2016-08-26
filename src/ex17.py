from sys import argv
from os.path import exists

script,from_file,to_file=argv

in_file=open(from_file)
indata=in_file.read()

#indata=open(from_file).read() alternate way to read

print "the input file is %d bytes long" % len(indata)

print "Does the output file exists %r" % exists(to_file)

print "press enter to continue , ctrl-c to abort"
raw_input("? ")

if exists(to_file) is False:
    out_file   =open(to_file,'w')
else :
    out_file   =open(to_file,'a')
    out_file.write("\n")

out_file.write(indata)

print "Alright,Done! \nLets clise the files"

in_file.close()
out_file.close()

print "lets read  the new file"

readdata=open(to_file).read()
print "\n %s\n" % readdata
