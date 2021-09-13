#################################################
#################### Day 2 ######################
#################################################

# implicit Conversions examples
num1 = 10
num2 = 20.5
implicit_conv_sum = num1 + num2
implicit_conv_sum += num2 #increasing num1 by num2

# arithmetic operators
no1 = 100
no2 = 20
total = no1 + no2
diff = no1 - no2
product = no1 * no2
quotient_float = no1 / no2
quotient_not_float = no1//no2 #floor division
remainder = no1 % no2

# relational operators
is_greater = (no1 > no2)
is_smaller = (no1 > no2)
is_equal = (no1 == no2)
is_not_equal = (no1 != no2)

# assignment
a = 100
b = 5
a += b # increment assignment operation
a = 100
b = 5
a -= b # decrement operation
a = 100
b = 5
a /= b # divided and assigned
a = 100
b = 5
a *= b # multiplied and assigned
a = 100
b = 5
a //= b #floor divided and assigned
a = 100
b = 5
a %= b # remainder is assigned

# logical operators
a = True
b = False
print(a and b)
print(a or b)
print(a is not b)

# conditional/ternary operator
is_greator = True if a > b else False

##################################################
############### ESCAPE SEQUENCES #################
##################################################
'''
\n - new line
\t - tab space
\r - carriage return
\\ - backslash
\' - apostrophe
\" - double apostrophe
\b - backspace
\f - form feed
\ooo - octal
\xhh - hexadeximal
\u - unicode
'''

#done with day2
