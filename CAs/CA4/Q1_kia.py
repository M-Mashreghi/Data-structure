def detect_cycle(n, edges):
    goups = []
    all = []
    a = []

    for u, v in edges:
        all.append(u)
        all.append(v)
        flag = False
        for g in goups:
            if u in g and v in g:
                flag = True
                continue
            f = g.copy()
            if u in f:
                if flag:
                    return -1
                flag = True
                g.append(v)
            if v in f:
                if flag:
                    return -1
                flag = True
                g.append(u)
        if not flag:
            goups.append([u, v])

    for i in range(1,n+1):
        if i not in all:
            a.append(i)


    for node in goups:
        number = len(set(node))
        node.sort()

        if number > 3:
            return -1
        if number == 2 and len(a) > 0:
            node.append(a.pop(0))
        if number == 1 and len(a) > 1:
            node.append(a.pop(0)) 
            node.append(a.pop(0)) 

    if len(goups) * 3 != n:
        if len(a) % 3 != 0:
            return -1

        while len(a) > 2:
            goups.append([a.pop(0),a.pop(0),a.pop(0)])
    return goups



n, m = map(int, input().split())
friendships = []
for _ in range(m):
    a, b = map(int, input().split())
    friendships.append((a, b))
result = detect_cycle(n, friendships)
if result == -1:
    print("-1")
else:
    for i in result:
        print(" ".join(map(str, i)))
