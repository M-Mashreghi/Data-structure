import numpy as np


rows, cols = map(int, input().split())

grid = []

for _ in range(rows):
    row = input()
    grid.append(row)

list_score_down = [[0 for _ in range(cols)] for _ in range(rows)]
list_score_up = [[0 for _ in range(cols)] for _ in range(rows)]
list_score_right = [[0 for _ in range(cols)] for _ in range(rows)]
list_score_left = [[0 for _ in range(cols)] for _ in range(rows)]

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

best_spot_row = 0
best_spot_col = 0
max_dot_count = 0

for row in range(rows):
    for col in range(cols):
        if grid[row][col] == '.':

            list_score_down[row][col] = dfs(row + 1, col  ,deviate=  'Down')  # down
            list_score_up[row][col] = dfs(row - 1 , col ,deviate=  'Up')  # up
            list_score_right[row][col] = dfs(row, col +1 ,deviate=  'right') # right
            list_score_left[row][col] = dfs(row, col - 1  ,deviate=  'Left')  # left

finnal_answer = np.array(list_score_down) + np.array(list_score_left) + np.array(list_score_right) + np.array(list_score_up) 


print( np.max(finnal_answer)+1)
