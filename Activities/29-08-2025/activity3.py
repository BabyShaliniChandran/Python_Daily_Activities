#question 3
# How do you remove duplicate characters from a string while maintaining order?
def remove_duplicate(input_string):
    seen=set()
    non_duplicate_string=[]
    for i in input_string:
        if i not in seen:
            seen.add(i)
            non_duplicate_string+=i
    return ''.join(non_duplicate_string)

print(remove_duplicate(input('enter a string')))
