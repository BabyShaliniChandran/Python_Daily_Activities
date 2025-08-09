with open("original.txt", "r") as original_file:
    lines = original_file.readlines()

reversed_lines = [line[::-1] for line in lines]

with open("reversed.txt", "w") as reversed_file:
    reversed_file.writelines(reversed_lines)
print(open("original.txt").read())
print(open("reversed.txt").read())
	