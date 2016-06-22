from sys import argv

script, weather, feeling = argv

print "Hot or Cold?"
weather = raw_input()

print "Happy or Sad?"
feeling = raw_input()

print "The name of the script is:", script
print "The day is:", weather
print "Today I am feeling:", feeling