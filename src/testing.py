from sys import argv

filename,number1,number2=argv;


if number1 is None:
    number1=0
else:
    number1=int(number1)


    if number2 is None:
        number1=0
    else:
        number2=int(number2)

number2=int(number2)
addnumber=int(raw_input("Enter a big number to subtract the values"))

print addnumber-((number1)+(number2))
