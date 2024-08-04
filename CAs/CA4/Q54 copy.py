from collections import deque

def bfs(n, m, start, end, maps):
    queue = deque([start])
    visited = [[False] * (m + 1) for _ in range(n + 1)]
    distance = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    distance[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        if (x, y) == end:
            return distance[x][y]

        for (new_x, new_y) in maps.get((x, y), []):
            if not visited[new_x][new_y]:
                queue.append((new_x, new_y))
                distance[new_x][new_y] = min(distance[new_x][new_y], distance[x][y] + 1)

    return -1

def main():
    n, m = map(int, input().split())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    maps = {}
    for _ in range(n):
        row = input().strip()
        for j, char in enumerate(row):
            if char == '\\':
                maps.setdefault((i, j), []).append((i + 1, j + 1))
                maps.setdefault((i + 1, j + 1), []).append((i, j))
            elif char == '/':
                maps.setdefault((i, j + 1), []).append((i + 1, j))
                maps.setdefault((i + 1, j), []).append((i, j + 1))

    result = bfs(n, m, (start_x, start_y), (end_x, end_y), maps)
    print(result if result != float('inf') else -1)

if __name__ == "__main__":
    main()
