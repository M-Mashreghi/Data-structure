T = int(input())
finall_result = []
for t in range(T):
    N, k_ = map(int, input().split())
    program_list = list(map(int, input()))
    max_zero1 = 0
    max_zero2 = 0
    max_zero_finall = 0
    for i in range(N):
        if program_list[i] == 0:
            flag = False
            zero = 0
            k = k_
            for j in range(i,N):
                if (flag == False):
                    if program_list[j] == 0:
                        zero += 1
                    else:
                        if(k >=1):
                            zero += 1
                            k = k-1
                            flag =True
                        else:
                            break
                else:
                    if program_list[j] == 0:
                        zero += 1
                        k=k-1
                    else:
                        if(k >=1):
                            zero += 1
                            k = k-1
                            flag =True
                        else:
                            break
            if zero > max_zero1:
                max_zero1 = zero
    for i in range(N-1,-1,-1):
        if program_list[i] == 0:
            flag = False
            zero = 0
            k = k_
            for j in range(i,0,-1):
                if (flag == False):
                    if program_list[j] == 0:
                        zero += 1
                    else:
                        if(k >=1):
                            zero += 1
                            k = k-1
                            flag =True
                        else:
                            break
                else:
                    if program_list[j] == 0:
                        zero += 1
                        k=k-1
                    else:
                        if(k >=1):
                            zero += 1
                            k = k-1
                            flag =True
                        else:
                            break
            if zero > max_zero2:
                max_zero2 = zero
    if(max_zero1 > max_zero2):
        max_zero_finall = max_zero1
    else:
        max_zero_finall = max_zero2
    finall_result.append(max_zero_finall)    


    
for i in finall_result:
    print(i)

    