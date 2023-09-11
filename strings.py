# Set the variable brian on line 3!

brian = "Hello life!"

# Assign your variables below, each on its own line!





# Put your variables above this line
# caesar = "Graham"
# praline = "John"
# viking = "Teresa"
# print caesar
# print praline
# print viking

# The string below is broken. Fix it using the escape backslash!

# 'This isn\'t flying, this is falling with style!'

"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
# fifth_letter = "MONTY"[4]

# print fifth_letter

# parrot = "Norwegian Blue"
# print len(parrot)

# parrot = "Norwegian Blue".lower()
# print parrot

# parrot = "norwegian blue".upper()

# print parrot

# """Declare and assign your variable on line 4,
# then call your method on line 5!"""

# pi = 3.14
# print str(pi)

# ministry = "The Ministry of Silly Walks"

# print len(ministry)
# print ministry.upper()

# """Tell Python to print "Monty Python"
# to the console on line 4!"""

# print("Monty Python")

# """Assign the string "Ping!" to
# the variable the_machine_goes on
# line 5, then print it out on line 6!"""


# the_machine_goes = "Ping!"
# print(the_machine_goes)

# Print the concatenation of "Spam and eggs" on line 3!

# print("Spam " + "and " + "eggs")

# # Turn 3.14 into a string on line 3!

# print "The value of pi is around " + str(3.14)

# string_1 = "Camelot"
# string_2 = "place"

# print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

# name = "Alex"
# quest = "Teaching Python"
# color = "Blue"

# print "Ah, so your name is %s, your quest is %s, " \
# "and your favorite color is %s." % (name, quest, color)

# pratice
# Write your code below, starting on line 3!

# my_string = "hi"
# print len(my_string)
# print my_string.upper()

from datetime import datetime

# from datetime import datetime
# now = datetime.now()
# print now

# from datetime import datetime
# now = datetime.now()
# current_year = now.year
# current_month = now.month
# current_day = now.day
# print now
# print current_year
# print current_month
# print current_day

# from datetime import datetime
# now = datetime.now()

# print '%02d/%02d/%04d' % (now.month, now.day, now.year)

# from datetime import datetime
# now = datetime.now()

# print '%02d:%02d:%02d' % (now.hour, now.minute, now.second)

# from datetime import datetime
# now = datetime.now()


print '%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second)

def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
      print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
      print "Of course this is the Argument Room, I've told you that already!"
    else:
      print "You didn't pick left or right! Try again."
      clinic()

clinic()