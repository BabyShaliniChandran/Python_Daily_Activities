#question1
# How do you reverse a string in Python without using slicing?
string=input('enter the string:')
for i in range(len(string)-1,-1,-1):
    print(string[i],end='')
print()

#BETTER VERSION
def reverse_string(input_str):
    reversed_chars = []
    for i in range(len(input_str) - 1, -1, -1):
        reversed_chars.append(input_str[i])
    return ''.join(reversed_chars)
user_input = input("Enter the string: ")
print("Reversed string:", reverse_string(user_input))

