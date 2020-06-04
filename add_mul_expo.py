# 6.Write a program that takes 4 numbers as a,b,c,d and show the output of a+b*c**d

# Getting the values from user
val1 = int(input('Enter the value of A:'))
val2 = int(input('Enter the value of B:'))
val3 = int(input('Enter the value of C:'))
val4 = int(input('Enter the value of D:'))
# Calculating addition, multiplication and exponent (right to left approach)
result = val1+val2*val3**val4
# Showing result
print('The Result is:' ,result)