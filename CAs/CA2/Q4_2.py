import sys
num_of_buildings =int( sys.stdin.readline())

height_of_buildings = list(map(int, sys.stdin.readline().split()))
sorted_height = height_of_buildings.copy()
sorted_height.sort(reverse=True)
zero_list = [0 for _ in range(len(height_of_buildings))]


list_score = []

temp_height=0
for i in range(len(height_of_buildings)):
    temp_height = height_of_buildings[i]
    right_index = 0
    left_index = 0
    # right moves
    for j in range(i,num_of_buildings):
        if height_of_buildings[j] < temp_height:
            break
    for k in range(i,-1,-1):
        if height_of_buildings[k] < temp_height:
            k = k+1
            break 
    # print(temp_height,j,k)
    list_score.append((j-k)*temp_height)
        
print(max(list_score))
