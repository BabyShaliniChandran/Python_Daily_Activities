def frequencies(nums):
    result = []

    for num in nums:
            count = nums.count(num)
            result.append((num, count))
            nums.remove(num)

    return result

nums = [4, 2, 4, 3, 2, 2]
print(frequencies(nums))  