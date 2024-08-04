def solve(n, m, x, y, it, jt, maps, visited, distance=0):
    global min1
    if (x, y) == (it, jt):
        min1 = min(distance, min1)
        return
    visited[x][y] = True

    for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < n and 0 <= new_y < m and not visited[new_x][new_y]:
            if (new_x, new_y) in maps.get((x, y), []):
                new_distance = distance
            else:
                new_distance = distance + 1
            if new_distance < min1:
                solve(n, m, new_x, new_y, it, jt, maps, visited, new_distance)

    visited[x][y] = False

def main():
    global min1
    min1 = float('inf')
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
            if grid[i][j] == '/':
                maps[(i + 1, j)].append((i, j + 1))
                maps[(i, j + 1)].append((i + 1, j))

    visited = [[False] * (m + 1) for _ in range(n + 1)]
    if (abs(it - is_) + abs(jt - js)) % 2 == 1:  # Parity check
        print(-1)
        return

    solve(n, m, is_, js, it, jt, maps, visited)
    print(min1 if min1 != float('inf') else -1)  # Handle no path found

if __name__ == "__main__":
    main()
