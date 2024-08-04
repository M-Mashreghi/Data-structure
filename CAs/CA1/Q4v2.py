import numpy as np

rows, cols = map(int, input().split())

grid = []

for _ in range(rows):
    row = list(input())  # Convert the input string to a list of characters
    grid.append(row)


list_score_down = [[0 for _ in range(cols)] for _ in range(rows)]
list_score_up = [[0 for _ in range(cols)] for _ in range(rows)]
list_score_right = [[0 for _ in range(cols)] for _ in range(rows)]
list_score_left = [[0 for _ in range(cols)] for _ in range(rows)]

# Function to perform DFS to count consecutive dots
def dfs(row, col, deviate = None):
    if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != '.':
        return 0
        
    count = 1
    if deviate == 'right':
        count += dfs(row, col +1 ,deviate=  'right')  # right
    if deviate == 'Down':
        count += dfs(row + 1, col  ,deviate=  'Down')  # down
    if deviate == 'Up':
        count += dfs(row - 1 , col ,deviate=  'Up')  # up
    if deviate == 'Left':
        count += dfs(row, col - 1  ,deviate=  'Left')  # left

    return count

# Initialize variables to store the best spot and its dot count
best_spot_row = 0
best_spot_col = 0
max_dot_count = 0

temp = None
counter = 0
for row in range(rows):
    counter = 0

    for col in range(cols):
        if grid[row][col]== '.':
            if col - 1 > 0 or col <= cols  or grid[row][col] == '.':
                list_score_right[row][col] = counter
                counter += 1

            else:
                list_score_right[row][col] = counter
                counter = 0
        else:
            counter = 0


temp = None
counter = 0
for row in range(rows):
    counter = 0
    for col in range(cols - 1, -1, -1):
        if grid[row][col]== '.':
            if col - 1 > 0 or col <= cols  or grid[row][col] == '.':
                list_score_left[row][col] = counter
                counter += 1
            else:
                list_score_left[row][col] = counter
                counter = 0
        else:
            counter = 0


temp = None
counter = 0
for col in range(cols):
    counter = 0

    for row in range(rows):
        if grid[row][col]== '.':
            if row - 1 > 0 or row <= rows  or grid[row][col] == '.':
                list_score_down[row][col] = counter
                counter += 1
            else:
                list_score_down[row][col] = counter
                counter = 0
        else:
            counter = 0

temp = None
counter = 0
for col in range(cols):
    counter = 0

    for row in range(rows -1 ,-1, -1):
        if grid[row][col]== '.':
            if row - 1 > 0 or row <= rows  or grid[row][col] == '.':
                list_score_up[row][col] = counter
                counter += 1
            else:
                list_score_up[row][col] = counter
                counter = 0
        else:
            counter = 0

# print(list_score_up)
# print(list_score_down)
# print(list_score_right)
# print(list_score_left)

# # find_best_row = []
# # for row in range(rows):
# #     find_best_row.append(grid[row].count('.'))
    
# # best_row = max(find_best_row)
# # # dot_count = dfs(max(find_best_row), col, time = 1)






# # for col in range(cols):
# #     if grid[max(find_best_row)][col] == '.':
# #         list_score_down[best_row][col] = dfs(best_row + 1, col  ,deviate=  'Down')  # down
# #         list_score_up[best_row][col] = dfs(best_row - 1 , col ,deviate=  'Up')  # up
# #         list_score_right[best_row][col] = dfs(best_row, col +1 ,deviate=  'right') # right
# #         list_score_left[best_row][col] = dfs(best_row, col - 1  ,deviate=  'Left')  # left

finnal_answer = np.array(list_score_down) + np.array(list_score_left) + np.array(list_score_right) + np.array(list_score_up) 

# print(finnal_answer)
print( np.max(finnal_answer)+1)
