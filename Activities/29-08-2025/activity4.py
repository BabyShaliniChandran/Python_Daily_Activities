#question 4
#Write a program to find the first non-repeating character in a string.
def first_non_repeating_char(input_string):
    for char in input_string:
        if input_string.count(char)==1:
            return char
    return None
print(first_non_repeating_char(input('enter the string:')))
'''
#beter way
from collections import Counter

def first_non_repeating_char(input_string):
    char_count = Counter(input_string)
    for char in input_string:
        if char_count[char] == 1:
            return char
    return None
    '''