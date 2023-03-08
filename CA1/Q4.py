T = int(input())
finall_result = []
for t in range(T):
    N, k_ = map(int, input().split())
    main_program_list = list(map(int, input()))
    max_zero = 0
    program_list = main_program_list.copy()
    for i in range(N):
        flag = False
        zero = 0
        k = k_
        for remove_1 in range(i,N):
                program_list[remove_1] = 0
                k = k - 1
                if k == 0:
                    break
        for r in range(N):
          if program_list[r] == 0:
            zero = 0
            for j in range(r,N):
                if program_list[j] == 0:
                     zero += 1
                else:
                     break
            if zero > max_zero:
                max_zero = zero    
        program_list = main_program_list.copy()

    finall_result.append(max_zero)    
    # print(max_zero)




    
for i in finall_result:
    print(i)

    