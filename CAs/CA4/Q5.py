from copy import deepcopy


def solve(n, m, x, y, it, jt, maps, visited, distance=0):
    global min1  # Declare the use of the global variable
    if (x, y) == (it, jt):
        min1 = min(distance, min1)
        return
    new_visited = deepcopy(visited)  # Use deepcopy to create a new visited array
    new_visited[x][y] = True

    for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        new_x, new_y = x + dx, y + dy

        # Update boundary checks to < n and < m
        if 0 <= new_x <= n and 0 <= new_y <= m and not new_visited[new_x][new_y]:
            if (new_x, new_y) in maps.get(f'{x}{y}', []):
                new_distance = distance
            else:
                new_distance = distance + 1
            if new_distance < min1:  # Only continue if new distance is less than min1
                solve(n, m, new_x, new_y, it, jt, maps, new_visited, new_distance)

def main():
    global min1
    min1 = float('inf')  # Initialize min1 to infinity
    n, m = map(int, input().split())
    is_, js = map(int, input().split())
    it, jt = map(int, input().split())

    all = {}
    for i in range(n + 1):
        for j in range(m + 1):
            all[f'{i}{j}'] = []

    grid = []
    for i in range(n):
        grid.append(input().strip())
        for j in range(m):
            if grid[i][j] == '\\':
                all[f'{i}{j}'].append((i + 1, j + 1))
                all[f'{i + 1}{j + 1}'].append((i, j))
            if grid[i][j] == '/':
                all[f'{i + 1}{j}'].append((i, j + 1))
                all[f'{i}{j + 1}'].append((i + 1, j))
    visited = [[False] * (m + 1) for _ in range(n + 1)]
    if (abs(it - is_) + abs(jt - js)) % 2 == 1:  # Parity check
        print(-1)
        return
    solve(n, m, is_, js, it, jt, all, visited)
    print(min1)

if __name__ == "__main__":
    main()
