from collections import deque

def bfs(n, m, start, end, maps):
    queue = deque([(start[0], start[1], 0)])  # (x, y, distance)
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True

    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == end:
            return dist

        for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < m and not visited[new_x][new_y]:
                if (new_x, new_y) in maps.get((x, y), []):
                    queue.append((new_x, new_y, dist))
                else:
                    queue.append((new_x, new_y, dist + 1))
                visited[new_x][new_y] = True

    return -1  # Return -1 if no path is found

def main():
    n, m = map(int, input().split())
    is_, js = map(int, input().split())
    it, jt = map(int, input().split())

    if (it - is_ + jt - js) % 2 == 1:
        print(-1)
        return

    maps = { (i, j): [] for i in range(n) for j in range(m) }

    grid = []
    for i in range(n):
        row = input().strip()
        grid.append(row)
        for j in range(m):
            if row[j] == '\\':
                if 0 <= i + 1 < n and 0 <= j + 1 < m:
                    maps[(i, j)].append((i + 1, j + 1))
                    maps[(i + 1, j + 1)].append((i, j))
            elif row[j] == '/':
                if 0 <= i + 1 < n and 0 <= j < m:
                    maps[(i, j + 1)].append((i + 1, j))
                    maps[(i + 1, j)].append((i, j + 1))

    result = bfs(n, m, (is_, js), (it, jt), maps)
    print(result)

if __name__ == "__main__":
    main()
