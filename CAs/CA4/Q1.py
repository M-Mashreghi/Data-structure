from collections import defaultdict
Teams = None

from sys import setrecursionlimit

setrecursionlimit(10 ** 5)

info = input().split()
n = int(info[0])
m = int(info[1])
teamsStatus = [-1] * n
Teams = None
possible = True

def partitionTeams(prisoner, team = 0) :
    global possible
    
    if teamsStatus[prisoner] == -1 :
        teamsStatus[prisoner] = team
        
    elif teamsStatus[prisoner] == team :
        return
    
    else :
        possible = False
        return
        
    for e in range(len(Teams[prisoner])):
        partitionTeams(Teams[prisoner][e], team ^ 1)
        

def make_teams () :
    global Teams
    Teams = defaultdict(list)
    
    for i in range(m) :
        info = input().split()
        Teams[int(info[0]) - 1].append(int(info[1]) - 1)
        Teams[int(info[1]) - 1].append(int(info[0]) - 1)
        
make_teams()
    
for p in range(n) :
    if teamsStatus[p] != -1 :
        continue
    partitionTeams(p)

if possible :
    # print('Yes')
    for i in range(n) :
        print(teamsStatus[i], end = ' ')
    print
else :
    print('-1')