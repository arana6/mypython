def cheese_and_crackers(cheese_count,box_of_crackers):
    print  "You have %d cheeses!" %cheese_count
    print  "You have %d boxes of crakers!" %box_of_crackers
    print   "Man that's enough for a party!"
    print   "Get a Blanket\n"


print   "We can just give the fucntion numbers directly :"
cheese_and_crackers(20,30)

print   "Or we can use variables from our script"

amount_of_cheese=10
amount_of_crackers=20


cheese_and_crackers(amount_of_cheese  ,amount_of_crackers)


print   "We can do maths inside too"

cheese_and_crackers(10+5,20+6)


print   "We can combine the two and use mathematics"

cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+200)

cheese_count=int(raw_input("Enter cheese count :"))
cracker_count=int(raw_input("Enter cracker count :"))
cheese_and_crackers(cheese_count,cracker_count)
