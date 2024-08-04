
input_func = input
string = input_func()
answer_num = int(input_func())
finall_answer = []

for _ in range(answer_num):
    test_case = list(map(int, input_func().split()))
    start = test_case[0] - 1
    end = test_case[1]
    stack_list = []
    stack_list.append(string[start])

    for char in string[start + 1:end]:
        if stack_list and ord(char) == ord(stack_list[-1]) + 32:
            stack_list.pop()
        else:
            stack_list.append(char)

    if not stack_list:
        finall_answer.append(1)
    else:
        finall_answer.append(0)

print(''.join(map(str, finall_answer)))
