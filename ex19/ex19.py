# define a function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheese!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
# giving cheese_count as 20 and boxes_of_crakcers as 30
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)
# setting variables
print "OR, we can use variables the function from out script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# doing math in argv palces
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
# getting sum of variables and numbers
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
