from sys import argv

script, user_name = argv 
prompt1 = 'Yes or No: '
prompt2 = 'Your place: '
prompt3 = 'Linux/Unix or Windows: '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt1)

print "Where do you live %s?" % user_name
lives = raw_input(prompt2)

print "What kind of computer do you have?"
computer = raw_input(prompt3)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
ANd you have a %r computer. Nice.
""" % (likes, lives, computer)