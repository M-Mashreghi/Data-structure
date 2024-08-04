# Get the number of rows and columns
rows, cols = map(int, input().split())

# Initialize the grid
grid = []

# Read each row and store it in the grid
for _ in range(rows):
    row = input()
    grid.append(row)

# Function to perform DFS to count consecutive dots
def dfs(row, col,time =0 , deviate = None):
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

    if time == 1:
        # Explore adjacent cells
        count += dfs(row+1, col ,deviate=  'Down')  # Down
        count += dfs(row-1, col,deviate=  'Up')  # Up
        count += dfs(row, col+1,deviate=  'right')  # Right
        count += dfs(row, col-1,deviate=  'Left')  # Left
    
    return count

# Initialize variables to store the best spot and its dot count
best_spot_row = 0
best_spot_col = 0
max_dot_count = 0

# Iterate through each cell in the grid
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == '.':
            dot_count = dfs(row, col, time = 1)
            if dot_count > max_dot_count:
                max_dot_count = dot_count
                best_spot_row = row
                best_spot_col = col

# Print the best spot and its dot count
# print(best_spot_row, best_spot_col)
print(max_dot_count)
