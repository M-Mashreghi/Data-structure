import numpy as np

rows, cols = map(int, input().split())

grid = []

for _ in range(rows):
    row = list(input())  # Convert the input string to a list of characters
    grid.append(row)







size_1d = rows * cols
# list_score_down = [0 for i in range(size_1d)]
# list_score_up = [0 for i in range(size_1d)]
list_score_right = [0 for i in range(size_1d)]
list_score_left = [0 for i in range(size_1d)]


list_score_down = [[0 for _ in range(cols)] for _ in range(rows)]
list_score_up = [[0 for _ in range(cols)] for _ in range(rows)]


grid_right =[]
for j in range(rows):
    grid_right += grid[j]
counter_right = 0
for i in range(len(grid_right)):
    if i % cols == 0:
        counter_right = 0
    if grid_right[i] != '.':
        counter_right = 0
    if grid_right[i] == '.':
        list_score_right[i] = counter_right
        counter_right += 1 

counter_left = 0
for i in range(len(grid_right)-1,-1,-1):
    if grid_right[i] != '.':
        counter_left = 0
    if grid_right[i] == '.':
        list_score_left[i] = counter_left
        counter_left += 1 
    if i % cols == 0:
        counter_left = 0

counter_down = 0
for j in range(cols):
    counter_down = 0
    for i in range(rows):
        if grid[i][j] != '.':
            counter_down = 0
        if grid[i][j] == '.':
            list_score_down[i][j] = counter_down
            counter_down += 1 
counter_up = 0
for j in range(cols-1,-1,-1):
    counter_up = 0
    for i in range(rows-1,-1,-1):
        if grid[i][j] != '.':
            counter_up = 0
        if grid[i][j] == '.':
            list_score_up[i][j] = counter_up
            counter_up += 1 
# print(list_score_down)
list_score_down_1d=[]
list_score_up_1d = []
for j in range(rows):
    list_score_down_1d += list_score_down[j]
    list_score_up_1d += list_score_up[j]

sum1 = np.array( list_score_left) + np.array(list_score_right)+ np.array(list_score_down_1d) + np.array(list_score_up_1d)
# print(list_score_left)+ np.array(list_score_down_1d) + np.array(list_score_up_1d)
# print(list_score_right)
print(list_score_down_1d)
print(list_score_up_1d)

print( np.max(sum1)+1)

