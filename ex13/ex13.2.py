from sys import argv

script, name, age, occupation = argv

print "This code is called:", script
print "My name is:", name
print "I am %s years old.", age
print "And I am a %s.", occupation

name = raw_input("What's your name? ")
age = raw_input("How old are you? ")
occupation = raw_input("What do you do? ")

print "So, Here's the %s, %s and he is %s years old. This is %r. Thank you." % (occupation, name, age, script)
