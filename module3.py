# While loops and for loops enable us to make certain sections of code repeat multiple times.

# A while loop continues iterating as long as its condition remains true. Here's an example:

# ex: 
total_score = 0
while total_score < 100:    
    total_score += int(input("Enter your score for this round: "))    
    print("total so far =", total_score)
print('Your score is now >= 100')

# The loop will first test the condition. If it's true, then the code in the loop is executed. It will continue testing the condition and executing the loop until the condition is false, at which point we drop out of the loop and execution resumes with whatever code comes after it. It's important that something in the loop will eventually cause the loop condition to become false. Otherwise the loop will continue forever, which is known as an infinite loop. If you run the example below, you can hit ctrl-c to stop it.

# for loops:
# A for loop traverses a sequence (or iterable type), looping once for each element in the sequence. A loop variable takes on the value of the current element, which can then be used inside the loop. So far, strings are the only iterable type we've looked at - we'll see one more on this page and others later. Here's an example of iterating through a string:

# for loop example:
word = "apothecary"
for letter in word:    # letter is the loop variable    
    print(letter)

# The first time through the loop, letter equals "a", next time through it equals "p", next "o", and so on until the last time through, when it equals "y".

# Using ranges with for loops
# If we need a for loop to iterate over some increasing (or decreasing) sequence of integers, we can achieve that by using a range. Ranges are another iterable type. Here's an example that counts from 1 to 10:

# ex:
for num in range(1, 11):
    print(num)
# Notice that the range goes from 1 up to, but not including, 11. A range can also count by a given step size:

# counts by twos
for num in range(1, 11, 2): # the third number is the step size
    print(num)

# You can count down by using a negative step size, but if you do, then the first number (the start of the range) needs to be greater than the second number (the end of the range):

# counts down from 10 to 1
for num in range(10, 0, -1):
    print(num)

# break and continue:
# A loop can be terminated early with the "break" keyword. For example:
for num in range(1, 11):    
    if (num == 5):        
      break    
    print(num)

# This loop only prints the numbers up to 4 because when the "break" is executed, it immediately drops us out of the loop.

# The "continue" keyword allows us to skip iterations of a loop. For example, try replacing the word "break" with "continue" in line 3 of the example above. With that change, it prints the numbers from 1 through 10 except for 5, because it skips that iteration, jumping us to the next iteration of the loop.

# proper use of break:
# There may be occasions where using "break" is justified, but you should try to write your loop conditions such that "break" is not needed, since that usually makes the behavior of your loop simpler to read.

# bad example
# This code translates a positive decimal integer into binary
binary_str = ""
user_num = int(input("Please enter a positive integer: "))
while True:
    binary_str = str(user_num % 2) + binary_str
    user_num //= 2
    if user_num == 0:  # This is the real loop condition
        break
print(binary_str)

# good example
# This code translates a positive decimal integer into binary
binary_str = ""
user_num = int(input("Please enter a positive integer: "))
while user_num != 0:
    binary_str = str(user_num % 2) + binary_str
    user_num //= 2
print(binary_str)

Notice that we flipped from testing == to testing !=. That's because we were testing when to stop, but now we're testing when to keep going.

# bad example
# This code continues asking the user for integers and printing them out
# until the user enters one that is a multiple of 10
while True:
    user_num = int(input("Please enter an integer: "))
    if user_num % 10 == 0: # This is the real loop condition
        break
    else:
        print("You entered", user_num)
print("all done")

# good example
# This code continues asking the user for integers and printing
# them out until the user enters one that is a multiple of 10

# The first line declares user_num by initializing it to a value
# that will make the loop condition True (otherwise we would
# never enter the loop)
user_num = 1
while user_num % 10 != 0:
    user_num = int(input("Please enter an integer: "))
    print("You entered", user_num)
print("all done")

# If there are two things that need to be true for a loop to continue, it's easy enough to use and to connect them in the loop condition.   You can also do this when there are more than two things that need to be true, but it's possible in such cases that the loop condition could become as hard or harder to read than using break statements.

# nested loops:
# Both while loops and for loops can be nested. You can also have if statements inside loops or loops inside if statements. You can have an if statement inside a for loop inside a while loop inside another if statement if you want to.

# A nested for loop
total_num_letters = 0
print("Please enter the names of your three favorite animals.")
for val in range(1, 4):    
    animal = input()    
    for letter in animal:        
      total_num_letters += 1
print("Those names contained a total of", total_num_letters, "characters.")

# Exercises:
# (See the module overview for a link to example solutions.)

# 1. Write code that reads an integer from the user and prints out the sum of the integers from 1 to that number.
# Sample input: 3
# Expected output: 6

sum = 0
limit = int(input())
for i in range(1, limit+1):
    sum += i
print(sum)

# 2. Write code that reads a string from the user, counts how many characters are in the string, and prints out "odd" if that number is odd, but prints "even" if that number is even.
# Sample input: The harder you're thrown, why the higher you bounce
# Expected output: "odd"

str_count = 0
str = input("please enter some words: ")
for letter in str:
    str_count += 1
    if(str_count % 2 == 0)