s = input()

def reverse_string(s):
    return s[::-1]

reversed_s = reverse_string(s)

list = []
check_point = 0
def find_list(s):
    temp = None
    counter = 0
    list = []
    check_point = 0

    for i in range(len(s)):
        if temp == s[i]:
            list.append(counter)
            counter = -check_point + i + 1
            temp = s[i]
            check_point = i
            continue

        counter +=1
        temp = s[i]
    list.append(counter)

    return list
l1 = find_list(s)
l2 = find_list(reversed_s)
l3 =  l1 + l2
# print(l3)
print(max(l3))