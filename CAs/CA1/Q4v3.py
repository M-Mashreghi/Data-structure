import numpy as np

rows, cols = map(int, input().split())

grid = []

for _ in range(rows):
    row = list(input())  # Convert the input string to a list of characters
    grid.append(row)



size_1d = rows * cols
list_score_down = [0 for i in range(size_1d)]
# list_score_up = [0 for i in range(size_1d)]
# list_score_right = [0 for i in range(size_1d)]
# list_score_left = [0 for i in range(size_1d)]




def dfs_up_down(counter, deviate = None):
    if counter < 0 or counter >= size_1d or grid_right[counter] != '.':
        return 0 
    count = 0
    if deviate == 'down':
        count += dfs_up_down(counter + cols , deviate=  'down')  # down
    if deviate == 'up':
        count += dfs_up_down(counter - cols  , deviate=  'up')  # up

    return count + 1

def dfs_left(counter, deviate = None):
    if counter <= 0 or counter >= size_1d or grid_right[counter] != '.':
        return 0
    if counter % cols == 0 and deviate ==  'Left' and grid_right[counter] == '.':
        return 1
    
    if counter % cols == 1 and grid_right[counter] == '.' and deviate !=  'Left' :
        return 1

    count = 0
    count += dfs_left(counter - 1 , deviate=  'Left')  # right
    return count + 1

def dfs_right(counter, deviate = None):
    if counter <= 0 or counter >= size_1d or grid_right[counter] != '.':
        return 0

    if counter % cols == cols - 1 and deviate ==  'right':
        return 1
    count = 0
    if deviate == 'right':
        count += dfs_right(counter + 1 , deviate=  'right')  # right
    return count + 1

grid_right =[]
for j in range(rows):
    grid_right += grid[j]
choosen_least = []
for i in range(len(grid_right)):
    if grid_right[i] == '.':
        if i%cols != 0 and  i > cols and i < (cols-1)*rows:
            if grid_right[i-1] == '.'  and grid_right[i+1] == '.' and grid_right[i-cols] == '.' and grid_right[i+cols] == '.' :
                choosen_least.append(i)



for i in choosen_least:
    if grid_right[i] == '.':
        list_score_down[i] =  dfs_up_down(i  + cols, deviate = "down") + dfs_up_down(i - cols , deviate = "up") +dfs_right(i + 1 , deviate = "right") + dfs_left(i - 1 , deviate = "right") 

        
finnal_answer = np.array(list_score_down) 

max_index_plus_one = np.argmax(list_score_down) 

print( np.max(finnal_answer)+1)

