def T(lst):
    n = len(lst)
    result = [0] * n
    for i in range(1, n):
        result[i] = result[i-1] + abs(lst[i] - lst[i-1])
    return result
lst = [0, 2, 2, 4, 1, 5]
result = T(lst)
print(result)