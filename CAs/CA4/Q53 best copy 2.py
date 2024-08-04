from collections import deque

def bfs(n, m, start, end, maps):
    queue = deque([(start, 0)])  # Store (coordinates, distance) tuples
    visited = [[False] * (m + 1) for _ in range(n + 1)]
    visited[start[0]][start[1]] = True

    while queue:
        (x, y), dist = queue.popleft()

        if (x, y) == end:
            return dist

        # Explore all connected nodes through maps
        for (new_x, new_y) in maps.get((x, y), []):
            if not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append(((new_x, new_y), dist + 1))

        # Explore all diagonal moves
        for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x <= n and 0 <= new_y <= m and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append(((new_x, new_y), dist + 1))

    return -1
