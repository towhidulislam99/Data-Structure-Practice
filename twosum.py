def twoSum(values, target):
    result = []
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] + values[j] == target:
                result.append([values[i], values[j]])
    return result if result else None
            

num = [2, 5, 8, 7, 11]
target = 13

result = twoSum(num, target)
print(result)