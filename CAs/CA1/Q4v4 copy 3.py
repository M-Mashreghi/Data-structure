
# Example usage:
rows, cols = map(int, input().split())

grid = []

for _ in range(rows):
    row = list(input())
    grid.append(row)


def flatten_2d(matrix):
    return [element for row in matrix for element in row]



def rotate_90(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

def rotate_neg_90(matrix):
    return [list(row) for row in zip(*matrix)][::-1]

def rotate_180(matrix):
    return [row[::-1] for row in matrix[::-1]]

list_score_right = [[0 for _ in range(cols)] for _ in range(rows)]
list_score_left = rotate_180([[0 for _ in range(cols)] for _ in range(rows)])
list_score_down = rotate_90([[0 for _ in range(cols)] for _ in range(rows)])
list_score_up = rotate_neg_90([[0 for _ in range(cols)] for _ in range(rows)])

def get_score(list_score_right, grid):
    #right
    for i in range(len(grid)):
        counter_down = 0
        for j in range(len(grid[0])):
            if grid[i][j] != '.':
                counter_down = 0
            if grid[i][j] == '.':
                list_score_right[i][j] = counter_down
                counter_down += 1 
    return list_score_right

def sum_score(list1,list2,list3,list4):
    for i in range(len(list1)):
        for j in range(len(list1[0])):
            list1[i][j] = list1[i][j] + list2[i][j] +list3[i][j] +  list4[i][j]
    return list1

list_score_right = get_score(list_score_right, grid)
list_score_down = get_score(list_score_down, rotate_90(grid))
# list_score_left = get_score(list_score_left, rotate_180(grid))
# list_score_up = get_score(list_score_up, rotate_neg_90(grid))
# sum_result = sum_score(rotate_180(list_score_left) ,rotate_90(list_score_up) ,rotate_neg_90(list_score_down) , list_score_right  )

# sum_result = flatten_2d(sum_result)
# print( max(sum_result) +1)

