import heapq
import sys

class PointManager:
    def __init__(self):
        self.points = []  # Stores the original points
        self.removed_indices = set()  # Keeps track of removed points by their indices
        self.heaps = {
            'd1': [],  # Max-heap for x + y
            'd2': [],  # Max-heap for x - y
            'd3': [],  # Max-heap for -x + y
            'd4': []   # Max-heap for -x - y
        }
        self.counter = 0  # Unique index for each point
    
    def add_point(self, x, y):
        idx = self.counter
        self.points.append((x, y, idx))
        heapq.heappush(self.heaps['d1'], (-(x + y), idx))
        heapq.heappush(self.heaps['d2'], (-(x - y), idx))
        heapq.heappush(self.heaps['d3'], (-(y - x), idx))
        heapq.heappush(self.heaps['d4'], (-(-x - y), idx))
        self.counter += 1
    
    def remove_nth_point(self, n):
        if 0 <= n < len(self.points):
            self.removed_indices.add(n)
    
    def _clean_heap(self, heap):
        # Remove all points from the heap that are marked as removed
        while heap and heap[0][1] in self.removed_indices:
            heapq.heappop(heap)
    
    def query_max_manhattan_distance(self, x, y):
        # Ensure heaps are clean and up-to-date
        self._clean_heap(self.heaps['d1'])
        self._clean_heap(self.heaps['d2'])
        self._clean_heap(self.heaps['d3'])
        self._clean_heap(self.heaps['d4'])
        
        # Get the maximum value from each heap (if not empty)
        max_d1 = -self.heaps['d1'][0][0] if self.heaps['d1'] else float('-inf')
        max_d2 = -self.heaps['d2'][0][0] if self.heaps['d2'] else float('-inf')
        max_d3 = -self.heaps['d3'][0][0] if self.heaps['d3'] else float('-inf')
        max_d4 = -self.heaps['d4'][0][0] if self.heaps['d4'] else float('-inf')

        # Compute the maximum distance using the current point (x, y)
        max_distance = max(
            max_d1 - (x + y),
            max_d2 - (x - y),
            max_d3 - (y - x),
            max_d4 - (-x - y)
        )
        
        return max_distance

def main():
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    n = int(data[0].strip())
    point_manager = PointManager()

    for i in range(1, n + 1):
        command = data[i].split()
        
        if command[0] == '+':
            x, y = int(command[1]), int(command[2])
            point_manager.add_point(x, y)
        
        elif command[0] == '-':
            index = int(command[1]) - 1
            point_manager.remove_nth_point(index)
        
        elif command[0] == '?':
            qx, qy = int(command[1]), int(command[2])
            max_distance = point_manager.query_max_manhattan_distance(qx, qy)
            print(max_distance)

if __name__ == "__main__":
    main()