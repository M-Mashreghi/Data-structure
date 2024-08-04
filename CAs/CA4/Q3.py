from collections import deque


def can_escape(n, k, left, right):    
    queue = deque([(0, 'left', 0)])  
    visited = set((0, 'left', 0))
    
    while queue:
        current_position, current_island, time = queue.popleft()
        
        if current_position >= n:
            return "YES"
        
        island_map = left if current_island == 'left' else right
        
        next_time = time + 1
        possible_moves = []
        
        if current_position + 1 < n and island_map[current_position + 1] == '-' and current_position + 1 > time:
            possible_moves.append((current_position + 1, current_island, next_time))
        
        if current_position - 1 >= 0 and island_map[current_position - 1] == '-' and current_position - 1 > time:
            possible_moves.append((current_position - 1, current_island, next_time))
        
        jump_position = current_position + k
        if jump_position < n:  
            opposite_island_map = right if current_island == 'left' else left
            if opposite_island_map[jump_position] == '-' and jump_position > time:
                possible_moves.append((jump_position, 'right' if current_island == 'left' else 'left', next_time))
        elif jump_position >= n: 
            return "YES"
        
        for move in possible_moves:
            if move not in visited:
                queue.append(move)
                visited.add(move)
    
    return "NO"



q = int(input().strip())
results = []

for _ in range(q):
    n, k = map(int, input().strip().split())
    left = input().strip()
    right = input().strip()
    results.append(can_escape(n, k, left, right))

for result in results:
    print(result)
