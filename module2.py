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