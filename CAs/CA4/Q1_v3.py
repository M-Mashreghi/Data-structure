from collections import defaultdict, deque

def find_teams(n, m, friendships):
    graph = defaultdict(list)
    for a, b in friendships:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * (n + 1)
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
    
    for minion in range(1, n + 1):
        if not visited[minion]:
            components.append(bfs(minion))
    
    teams = []
    for component in components:
        if len(component) % 3 != 0:
            return -1  
        component.sort()
        for i in range(0, len(component), 3):
            teams.append(component[i:i+3])
    
    return teams

def main():
    n, m = map(int, input().split())
    friendships = []
    for _ in range(m):
        a, b = map(int, input().split())
        friendships.append((a, b))

    result = find_teams(n, m, friendships)
    if result == -1:
        print(-1)
    else:
        for team in result:
            print(" ".join(map(str, team)))

if __name__ == "__main__":
    main()
