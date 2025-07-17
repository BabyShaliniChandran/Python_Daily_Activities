text="amazing python language"
remove_space=text.replace(" ","")
str_upper=remove_space.upper()
text=str_upper.replace('A','XXX')
third_pos=text[::3]
print(third_pos[::-1])

