from itertools import permutations
num = int(input())
def are_divisible(number1, number2):
    if number1 % number2 == 0 or number2 % number1 == 0:
        return True
    else:
        return False
original_list =[]
for i in range(num):
    original_list.append( i +1 )

permutation_list = list(permutations(original_list))
counter = 0


for i in range(len(permutation_list)):
    counter_inside = 0
    for j in range(len(permutation_list[i])):
        if are_divisible(permutation_list[i][j], j+1) :
            counter_inside += 1
    if counter_inside == num:
        counter+=1

print(counter)
