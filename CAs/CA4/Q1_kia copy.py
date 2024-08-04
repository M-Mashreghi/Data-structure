def detect_cycle(n, edges):
    groups = []
    all_nodes = []
    isolated_nodes = []

    for u, v in edges:
        all_nodes.extend([u, v])
        group_found = False
        for group in groups:
            if u in group and v in group:
                group_found = True
                continue
            group_copy = group.copy()
            if u in group_copy or v in group_copy:
                if group_found:
                    return -1
                group_found = True
                group.extend([u, v])
                
        if not group_found:
            groups.append([u, v])

    for i in range(1, n + 1):
        if i not in all_nodes:
            isolated_nodes.append(i)

    for group in groups:
        unique_members = len(set(group))
        if unique_members > 3:
            return -1
        if unique_members == 2 and isolated_nodes:
            group.append(isolated_nodes.pop(0))
        if unique_members == 1 and len(isolated_nodes) > 1:
            group.extend(isolated_nodes[:2])
            del isolated_nodes[:2]

    if len(groups) * 3 != n:
        if len(isolated_nodes) % 3 != 0:
            return -1
        while isolated_nodes:
            groups.append(isolated_nodes[:3])
            del isolated_nodes[:3]

    return groups

n, m = map(int, input().split())
friendships = []
for _ in range(m):
    a, b = map(int, input().split())
    friendships.append((a, b))
result = detect_cycle(n, friendships)
if result == -1:
    print("-1")
else:
    for group in result:
        print(' '.join(str(v) for v in group), end=' ')
        print()
