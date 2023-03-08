n, m = map(int, input().split())
hooks = list(map(int, input()))
stones = [int(input()) for i in range(m)]

# Compute the differences between adjacent stones and accumulate them
diffrenc_list = [0] * m
j = 0
for i in range(m):
    stone_pos = stones[i] - 1
    while j < n:
        diff = abs(hooks[stone_pos] - hooks[j])
        diffrenc_list[i] += diff
        if j >= stone_pos and (j == n - 1 or abs(hooks[stone_pos] - hooks[j+1]) > diff):
            break
        j += 1

# Print the differences between adjacent stones
for diff in diffrenc_list:
    print(diff)
