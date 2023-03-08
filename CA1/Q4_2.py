T = int(input())
finall_result = []
for t in range(T):
    N, k_ = map(int, input().split())
    program_list = list(map(int, input()))
    max_zero = 0
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
            if zero > max_zero:
                max_zero = zero
        
    finall_result.append(max_zero)    
    # print(max_zero)


    
for i in finall_result:
    print(i)

    