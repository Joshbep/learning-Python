# NOTES FOR MODULE 2

# integers are numeric values that don't contain a decimal point. These can be as long as you want them(within the limits of your computer's memory).

# Floating-point numbers are numeric values that do contain a decimal point. In mathematics, these are called real numbers. Integers are a subset of the real numbers. The value 4 is an integer, but the value 4.0 is a floating-point number.

# -Floats can also be written using scientific notation, using either e or E followed by a positive or negative integer (the exponent).
# -e maximum value of a float is 1.7976931348623157e+308. Floats are stored as binary fractions. Unfortunately most fractional values cannot be represented exactly in binary. Just as 1/3 cannot be represented exactly in decimal notation with a finite number of digits (0.333333333333333...), 1/10 cannot be represented exactly in binary notation with a finite number of digits (0.000110011001100...). Because of this, floats are approximate values, but the approximation is accurate to several decimal places.

# Strings are zero or more characters between a pair of quotation marks. You can use either single quotes or double quotes. The length of a string is only limited by your computer's memory.

# If you want to have a quotation mark be part of a string, there are two ways. One way is that if the string contains a double quote, you can use single quotes to mark the ends of the string (or vice-versa).
# EX:> print('She explained, "Mae fy hofrenfad yn llawn llyswennod."')

# another ex: > print('She explained, "Mae fy hofrenfad yn llawn llyswennod."')

# Normal strings cannot be split across multiple lines. Later we'll see a special kind of string (called a docstring) that can be.

# There are only two Boolean values - True and False. The first letter of those values must be capitalized.

# A variable is a name that refers to a particular value. It's called a variable because the value it refers to can change. An assignment statement assigns a value to a variable. If a variable of that name doesn't yet exist, then one is created. Assignment statements look like this:

# Variable names should be descriptive of their purpose to enhance the readability of your code. They must start with a letter or an underscore - subsequent characters can be numbers, letters or underscores. Variable names are case sensitive - radius, Radius, raDius, etc. would be interpreted as different variables. A variable name cannot be the same as a keyword. Python 3 has the following keywords:

# Literal values like 212, or -17.8, or "Wichita", or True, are often referred to simply as literals.

# If there are literal values that appear in your code, it can be a good idea to replace them with constants.

# the name of a constant is in all caps, for example MAX_CAPACITY or EARTH_GRAVITY. A constant is assigned a value once and then that value should never change during the program's execution. Python doesn't enforce this, because it has a philosophy of "we're all adults here", so you could change the value of a constant, but just don't. Declaring a constant gives a name to a literal value, making it easier to recognize or remember the value's purpose, so that you don't have "magic numbers" in your code.

# Something that often comes up for the output of a program is printing out specific text, but with the values of certain variables or constants filled in. There are a few different ways of doing this in Python. Here's one example:
# ex:print("Your dog is", dog_age, "years old.")

# Here's an example that uses string concatenation, which will be mentioned in the next exploration:
# print("Your dog is " + str(dog_age) + " years old.")

# Here's one more example, using something called an f-string (because of the 'f' at the beginning):
# print(f"Your dog is {dog_age} years old.")

pi = 3.14159
print(pi)

last_name = "Smith"
print(last_name)

length_in_inches = 19.3
print(type(length_in_inches))

occupation = "haberdashery"
print(type(occupation))


# Comments are notes for those reading the code, and are ignored by the Python interpreter. A comment begins with #. A comment can be either on its own line or on the same line as other code. Either way, the compiler ignores everything between the # and the end of the line.

# Addition, subtraction, multiplication and division are done with the +, -, *, and / symbols.

# The floor division operation is done with the // symbol, and gives you the rounded down result of division.
# ex:floor_1 = 7 // 2 # 3
# ex:floor_2 = -7 // 2 # -4

# Normal division results in a float value, even if the result is an integer.  For example 8 / 4 would give you 2.0.  If you need an integer remainder, use floor division.

# The mod operation is done with the % symbol, and gives you the remainder of division.
# > remainder_1 = 14 % 3 # 2
# > remainder_2 = 3 % 5 # 3

# Exponentiation is done with the ** symbol.
# > power_1 = 3 ** 4 # 81
# > power_2 = 2 ** -3 # 0.125

# The order of operations is exponentiation, followed by multiplication, division, floor, and mod, followed by addition and subtraction. However parentheses can be used to give whatever order is needed, since operations in parentheses happen first.
# > result_1 = 3 * 5 + 1 # 16, multiplication happens first
# > result_2 = 3 * (5 + 1) # 18, addition happens first

# The += operator is a slightly shorter way to express that you want to add something to an existing value. The following statements do exactly the same thing:
# > my_sum = my_sum + 8
# > my_sum += 8


# You can combine = with each of the operators above to get the following shortcut operators:

# > num += 3  # same as num = num + 3
# > num -= 3  # same as num = num - 3
# > num *= 3  # same as num = num * 3
# > num /= 3  # same as num = num / 3
# > num //= 3 # same as num = num // 3
# > num %= 3  # same as num = num % 3
# > num **= 3 # same as num = num ** 3

# The += operator is the most commonly used of these, since it's handy for accumulating totals.

# You can get the absolute value of a number like this:

# answer = abs(-12)

# The + operator can also be used with strings to concatenate them together.

# print(19%6)
# print(2**4)
# conversion_ratio. = 9/5
# num_planets = 9
# num_planets-=1
# title = "Doctor"
# last_name = "Pierce"
# print(title + " " + last_name)

# The input() function reads typed input from the user. You can use it in a couple of ways. For example, if you want to ask the user for their name, you can do this:
# print("Please enter your name.")
# name = input()
# print("Hi", name)

# User input is always a string. If you want a numeric value from user input, then you need to cast the string to an int or a float.

# > age = int(input("Please enter your age: "))
# > height_in_meters = float(input("Please enter your height in meters: "))

# Each of the lines above combines two functions. First the input function gets a string from the user. Next the int() or float() function casts that string to a numeric value. That value is then assigned to the variable. We can call those functions on separate lines if we want:

# > str_age = input("Please enter your age: ") # str_age will refer to a string value
# > int_age = int(str_age) # int_age will refer to an int value

# name = input("What is your name?")
# print("Hello" + " " + name)

# name = input("What is your name?")
# print("Hello", name)

# first_num = float(input())
# second_num = float(input())
# print("The result is", first_num * second_num)

# first_num = float(input("first number: "))
# second_num = float(input("second number: "))
# result = first_num * second_num
# print("The result is", result)
