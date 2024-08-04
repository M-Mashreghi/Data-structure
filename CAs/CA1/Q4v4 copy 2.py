import numpy as np

rows, cols = map(int, input().split())

# Read all lines of input at once and convert to 2D array
grid_np = np.array([list(input()) for _ in range(rows)])

# Initialize variable to store the maximum score
max_score = 0

# Compute scores for right, left, down, and up directions simultaneously
for i in range(rows):
    for j in range(cols):
        if grid_np[i, j] == '.':
            # Compute score for right direction
            right_score = np.sum(grid_np[i, j:] == '.') if j < cols - 1 else 0

            # Compute score for left direction
            left_score = np.sum(grid_np[i, :j] == '.') if j > 0 else 0

            # Compute score for down direction
            down_score = np.sum(grid_np[i:, j] == '.') if i < rows - 1 else 0

            # Compute score for up direction
            up_score = np.sum(grid_np[:i, j] == '.') if i > 0 else 0

            # Calculate total score for the cell
            cell_score = right_score + left_score + down_score + up_score + 1

            # Update maximum score if necessary
            max_score = max(max_score, cell_score)

# Output the maximum score
print(max_score)
