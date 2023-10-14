# While loops and for loops enable us to make certain sections of code repeat multiple times.

# A while loop continues iterating as long as its condition remains true. Here's an example:

# ex: 
total_score = 0
while total_score < 100:    
    total_score += int(input("Enter your score for this round: "))    
    print("total so far =", total_score)
print('Your score is now >= 100')
