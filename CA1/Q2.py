n, m = map(int, input().split())
hooks = input()
differences = [abs(ord(hooks[i]) - ord(hooks[i-1])) for i in range(1, n)]
differences = [abs(ord(hooks[i]) - ord(hooks[i-1])) for i in range(1, n)]
prefix_sums = [0] * n
for i in range(n-1):
    if 1:
        prefix_sums[i+1] = prefix_sums[i] + (i+1)*differences[i]
    if 0:
        prefix_sums[i+1] = prefix_sums[i] - (i+1)*differences[i]
print((differences))
print(prefix_sums)
for i in range(m):
    stones = int(input())
    print(prefix_sums[stones-1])