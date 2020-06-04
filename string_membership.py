#  8.write a program that takes a string like as ‘hasib’ and take another ch value like as ‘a’.
# if ‘a’ in ‘hasib’: show a is available in that string.
# Else: show a is not available in that string

# Getting the values from user
str1 = input('Enter your nick name: ')
char = input('Enter a character to check membership: ')
# Membership check
if char in str1:
    print('Your entered character is IN the string')
else:
    print('Your entered character is NOT in the string')