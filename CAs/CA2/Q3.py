# import sys
# input_func = sys.stdin.readline
import time


start_time = time.time()



input_func = input

string = input_func()
answer_num = int(input_func())
finall_answer = ''

def check_cases(string):

    if len(string) == 1 :#check letter is upper
        return False
    if string == '' or len(string) == 0 :
        return True
    if string[-2].isupper() and string[-1].islower() and string[-2] == string[-1].upper():
        return check_cases(string[:-2])

    if string[0].isupper() and string[1].islower() and string[0] == string[1].upper():
        return check_cases(string[2:])


    if string[0].isupper() and string[-1].islower() and string[0] == string[-1].upper():
        return check_cases(string[1:-1])

    else :
        return False    


for i in range(answer_num):

    test_case = list(map(int, input_func().split()))

    temp =string[test_case[0] - 1: test_case[1] ]

    if check_cases(temp):
        finall_answer += '1'
    else:
        finall_answer += '0'




print(finall_answer)



















