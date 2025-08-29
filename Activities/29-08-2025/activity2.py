#question2
# Write a program to check if a string is a palindrome.
from activity1 import reverse_string
def is_pallindrom(input_string):
    input_string=input_string.lower()
    print(input_string == reverse_string(input_string))

#is_pallindrom(input_string=input('enter the string to check is palindrom or not:'))
