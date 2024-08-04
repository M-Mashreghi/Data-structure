from collections import deque

def bfs(n, m, start, end, maps):
    queue = deque([start])
    visited = [[False] * (m + 1) for _ in range(n + 1)]
    distance = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    distance[start[0]][start[1]] = 0
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x <= n and 0 <= new_y <= m and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                distance[new_x][new_y] = distance[x][y] + 1
                queue.append((new_x, new_y))
                if (new_x, new_y) == end:
                    return distance[new_x][new_y]

        for (new_x, new_y) in maps.get((x, y), []):
            if not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                distance[new_x][new_y] = distance[x][y] + 1
                queue.append((new_x, new_y))
                if (new_x, new_y) == end:
                    return distance[new_x][new_y]

    return -1
