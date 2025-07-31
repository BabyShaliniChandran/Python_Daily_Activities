#binary search

number=int(input("enter the number:"))
list_numbers=[1,2,3,4,5]

def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1
    not_found = True

    while low <= high:
        mid = (low + high) // 2

        if numbers[mid] == target:
            print("Found")
            not_found = False
            break
        elif target > numbers[mid]:
            low = mid + 1
        else:
            high = mid - 1

    if not_found:
        print("Not Found")

numbers = [1, 3, 5, 7, 9, 11]
target = 7
binary_search(numbers, target)



