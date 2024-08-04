import sys

def max_area(height_of_buildings):
    stack = []
    counter = 0
    list_area = []

    while counter < len(height_of_buildings):
        if not stack or height_of_buildings[stack[-1]] <= height_of_buildings[counter]:
            stack.append(counter)
            counter += 1
        else:
            top_of_stack = stack.pop()
            if stack:
                width = counter - stack[-1] - 1
            else:
                width = counter
            area = height_of_buildings[top_of_stack] * width


            list_area.append(area)

    while stack:
        top_of_stack = stack.pop()
        if stack:
            width = counter - stack[-1] - 1
        else:
            width = counter
        area = height_of_buildings[top_of_stack] * width
        
        list_area.append(area)

    return list_area

num_of_buildings = int(sys.stdin.readline())
height_of_buildings = list(map(int, sys.stdin.readline().split()))

print(max(max_area(height_of_buildings)))
