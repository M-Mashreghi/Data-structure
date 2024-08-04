import numpy as np

rows, cols = map(int, input().split())

# Read all lines of input at once and convert to 2D list
grid = [list(input()) for _ in range(rows)]

# Convert grid to numpy array for efficient operations
grid_np = np.array(grid)

# Initialize arrays for scores
list_score_right = np.zeros((rows, cols), dtype=int)
list_score_left = np.zeros((rows, cols), dtype=int)
list_score_down = np.zeros((rows, cols), dtype=int)
list_score_up = np.zeros((rows, cols), dtype=int)

# Compute scores for right, left, down, and up directions simultaneously
# Right and left
for i in range(rows):
    counter_right = 0
    counter_left = 0
    for j in range(cols):
        if grid_np[i, j] == '.':
            list_score_right[i, j] = counter_right
            counter_right += 1
        else:
            counter_right = 0

        if grid_np[i, cols - 1 - j] == '.':
            list_score_left[i, cols - 1 - j] = counter_left
            counter_left += 1
        else:
            counter_left = 0

# Down and up
for j in range(cols):
    counter_down = 0
    counter_up = 0
    for i in range(rows):
        if grid_np[i, j] == '.':
            list_score_down[i, j] = counter_down
            counter_down += 1
        else:
            counter_down = 0

        if grid_np[rows - 1 - i, j] == '.':
            list_score_up[rows - 1 - i, j] = counter_up
            counter_up += 1
        else:
            counter_up = 0

# # Output the scores (if needed)
# print("Right scores:")
# print(list_score_right)
# print("Left scores:")
# print(list_score_left)
# print("Down scores:")
# print(list_score_down)
# print("Up scores:")
# print(list_score_up)

finnal_answer = np.array(list_score_down) + np.array(list_score_left) + np.array(list_score_right) + np.array(list_score_up) 

# print(finnal_answer)
print( np.max(finnal_answer)+1)