import sys
num_of_buildings = sys.stdin.readline()

height_of_buildings = list(map(int, sys.stdin.readline().split()))
sorted_height = height_of_buildings.copy()
sorted_height.sort(reverse=True)
zero_list = [0 for _ in range(len(height_of_buildings))]


list_score = []

temp_height=0
for i in range(len(sorted_height)):
    temp_height = sorted_height[i]
    for j in range(len(height_of_buildings)):
        if height_of_buildings[j] == sorted_height[i]:
            zero_list[j] = 1
    # now find the most 1
    counter = 0
    for k in range(len(zero_list)):
        if zero_list[k] == 1 :
            counter = counter + 1
        list_score.append(temp_height * counter)
        if zero_list[k] == 0 :
            counter = 0    
        
print(max(list_score))
