import sys

def main():
    input_func = sys.stdin.readline

    rows, cols = map(int, input_func().split())

    grid = []

    for _ in range(rows):
        row = list(input_func()[:-1]) 
        grid.append(row)



    def max_score(matrix):
        max_score = 0
        for row in matrix:
            for score in row:
                max_score = max(max_score, score)
        return max_score + 1

    list_score_right = [[0 for _ in range(cols)] for _ in range(rows)]
    list_score_left = ([[0 for _ in range(cols)] for _ in range(rows)])
    list_score_down = ([[0 for _ in range(cols)] for _ in range(rows)])
    list_score_up = ([[0 for _ in range(cols)] for _ in range(rows)])

    # right
    for i in range(rows):
        counter_right = 0
        for j in range(cols):
            if grid[i][j] != '.':
                counter_right = 0
            if grid[i][j] == '.':
                list_score_right[i][j] = counter_right
                counter_right += 1

    counter_left = 0
    for i in range(rows):
        counter_left = 0
        for j in range(cols-1,-1,-1):
            if grid[i][j] != '.':
                counter_left = 0
            if grid[i][j] == '.':
                list_score_left[i][j] = counter_left
                counter_left += 1

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

    sum1 = []
    

    for i in range(rows):
        temp_row = []
        for j in range(cols):
            temp_row.append(list_score_left[i][j] + list_score_right[i][j] + list_score_down[i][j] + list_score_up[i][j])
        sum1.append(temp_row)
    print(max_score(sum1))

main()
