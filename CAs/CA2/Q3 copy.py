# import sys
# input_func = sys.stdin.readline
import time


start_time = time.time()



input_func = input

string = input_func()
answer_num = int(input_func())
finall_answer = ''

def check_cases(string):
    if string == '' or len(string) == 0 :
        return True
    
    if len(string) == 1 :#check letter is upper
        return False
    if ord(string[-2]) +32 == ord(string[-1]):
        return check_cases(string[:-2])

    if ord(string[0])+32 == ord(string[1]):
        return check_cases(string[2:])

    if ord(string[0])+32 == ord(string[-1]):
        return check_cases(string[1:-1])


 


for i in range(answer_num):

    test_case = list(map(int, input_func().split()))

    temp =string[test_case[0] - 1: test_case[1] ]

    if check_cases(temp):
        finall_answer += '1'
    else:
        finall_answer += '0'




print(finall_answer)



















