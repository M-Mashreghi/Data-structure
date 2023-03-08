n, m = map(int, input().split())
hooks = list(map(int, input()))
stones = [int(input()) for i in range(m)]
seen_0 =0
seen_1 =0
seen_2 =0
seen_3 =0
seen_4 =0
seen_5 =0
seen_6 =0
seen_7 =0
seen_8 =0
seen_9 =0
list =[]
for i in range(n):
    if hooks[i] == 0:
        seen_0 += 1
    elif hooks[i] == 1:
        seen_1 += 1
    elif hooks[i] == 2:
        seen_2 += 1
    elif hooks[i] == 3:
        seen_3 += 1
    elif hooks[i] == 4:
        seen_4 += 1
    elif hooks[i] == 5:
        seen_5 += 1
    elif hooks[i] == 6:
        seen_6 += 1
    elif hooks[i] == 7:
        seen_7 += 1
    elif hooks[i] == 8:
        seen_8 += 1
    elif hooks[i] == 9:
        seen_9 += 1
    list.append([seen_0,seen_1,seen_2,seen_3,seen_4,seen_5,seen_6,seen_7,seen_8,seen_9])
for i in stones:
    sum = abs(list[i-1][0]*(hooks[i-1]-0))+abs(list[i-1][1]*(hooks[i-1]-1))+abs(list[i-1][2]*(hooks[i-1] - 2)) +  abs(list[i-1][3]*(hooks[i-1]-3))+abs(list[i-1][4]*(hooks[i-1]-4))+abs(list[i-1][5]*(hooks[i-1]-5)) +   abs(list[i-1][6]*(hooks[i-1]-6))+abs(list[i-1][7]*(hooks[i-1]-7))+abs(list[i-1][8]*(hooks[i-1]-8)) +abs(list[i-1][9]*(hooks[i-1]-9))
    print(sum)
         
        
          
          

