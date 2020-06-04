# 4. Write a program that takes three input a, b and c and apply a exponent operator between the last tow
# variable where b is will treat as base and c will treat as power then multiply a with them.

# Getting the values from user
val1 = int(input('Enter the value of A:'))
val2 = int(input('Enter the value of B (base number):'))
val3 = int(input('Enter the value of C (power):'))
# Calculating using exponent operator
result = val1*(val2**val3)
# Showing result
print('The Result is:' ,result)