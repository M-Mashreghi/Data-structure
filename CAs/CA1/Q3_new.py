num = int(input())

def are_divisible(number1, number2):
    return number1 % number2 == 0 or number2 % number1 == 0

def count_valid_permutations(n):
    def generate_permutations(index):
        if index == n:
            return 1
        total = 0
        for i in range(1, n + 1):
            if not used[i] and are_divisible(i, index + 1):
                used[i] = True
                total += generate_permutations(index + 1)
                used[i] = False
        return total

    used = [False] * (n + 1)
    return generate_permutations(0)

result = count_valid_permutations(num)
print(result)
