from collections import defaultdict, deque


def prettiest_permutation(n, p, A):


    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if A[i][j] == '1':
                graph[i].append(j)
                graph[j].append(i)


    visited = [False] * n
    components = []

    def bfs(start):
        queue = deque([start])
        component = []
        visited[start] = True
        while queue:
            node = queue.popleft()
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return component

    for i in range(n):
        if not visited[i]:
            components.append(bfs(i))


    result = [0] * n
    for component in components:

        indices = sorted(component)
        values = sorted(p[i] for i in indices)

        for idx, value in zip(indices, values):
            result[idx] = value

    return result

n = int(input())
p = list(map(int, input().split()))
A = [input().strip() for _ in range(n)]

result = prettiest_permutation(n, p, A)
print(" ".join(map(str, result)))
