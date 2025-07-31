list=[5,4,2,1,6,3]

for i in range(len(list)):
    index = i
    for j in range(i + 1, len(list)):
        if list[j] < list[index]:
            index = j
    list[i], list[index] = list[index], list[i]
    print(list)



