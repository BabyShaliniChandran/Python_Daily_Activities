#question 5
# How do you count the occurrence of each character in a string?

def occurrence_of_char(input_string):
    dict={}
    for i in input_string:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    return dict
print(occurrence_of_char(input('enter the string:')))



