from collections import deque

def bfs(n, m, start, end, maps):
    queue = deque([(start[0], start[1])])
    visited = [[False] * (m + 1) for _ in range(n + 1)]
    distance = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    distance[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        if (x, y) == end:
            return distance[x][y]
        
        queue2 = deque([(x, y)])
        while queue2:
            x2, y2 = queue2.popleft()
            for (new_x, new_y) in maps.get((x2, y2), ()):
                if (new_x, new_y) == end:
                    return distance[x][y]
                if visited[new_x][new_y]:
                    continue
                distance[new_x][new_y] = distance[x][y]
                visited[new_x][new_y] = True
                queue2.append((new_x, new_y))

        for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x <= n and 0 <= new_y <= m:
                if not visited[new_x][new_y]:
                    distance[new_x][new_y] = distance[x][y] + 1
                queue.append((new_x, new_y))
            

    return -1

def main():
    n, m = map(int, input().split())
    is_, js = map(int, input().split())
    it, jt = map(int, input().split())

    maps = {}
    for i in range(n + 1):
        for j in range(m + 1):
            maps[(i, j)] = []

    grid = []
    for i in range(n):
        grid.append(input().strip())
        for j in range(m):
            if grid[i][j] == '\\':
                maps[(i, j)].append((i + 1, j + 1))
                maps[(i + 1, j + 1)].append((i, j))
            elif grid[i][j] == '/':
                maps[(i + 1, j)].append((i, j + 1))
                maps[(i, j + 1)].append((i + 1, j))

    if (it - is_ + jt - js) % 2 == 1:
        print(-1)
        return
    result = bfs(n, m, (is_, js), (it, jt), maps)
    print(result)

if __name__ == "__main__":
    main()
