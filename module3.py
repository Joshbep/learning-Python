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
