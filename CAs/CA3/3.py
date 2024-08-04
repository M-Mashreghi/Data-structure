class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parant = None
        self.left = None
        self.right = None

def find_root(nodes):
    root = nodes[0]
    while root.parant != None:
        root = root.parant
    return root

def build_tree_from_input(input_lines, n):
    # Initialize an array to store nodes
    nodes = []

    # Create nodes and populate values
    for line in input_lines:
        value, left_index, right_index = map(int, line.split())
        nodes.append(TreeNode(value))

    # Connect nodes based on indices
    for i in range(n):
        if nodes[i]:
            left_index, right_index = map(int, input_lines[i].split()[1:])
            if left_index != -1:
                nodes[i].left = nodes[left_index - 1]
                nodes[left_index - 1].parant = nodes[i]
            if right_index != -1:
                nodes[i].right = nodes[right_index - 1]
                nodes[right_index - 1].parant = nodes[i]

    return find_root(nodes)  # Return the root node

def count_misplaced_nodes(root, lower=float('-inf'), upper=float('inf')):
    if not root:
        return 0
    print()
    misplaced_count = 0
    if root.value <= lower or root.value >= upper:
        misplaced_count += 1

    # Recurse on left and right subtrees
    misplaced_count += count_misplaced_nodes(root.left, lower, min(root.value, upper))
    misplaced_count += count_misplaced_nodes(root.right, max(root.value, lower), upper)

    return misplaced_count

n = int(input())
input_lines = []
for _ in range(n):
    input_lines.append(input())

root_node = build_tree_from_input(input_lines, n)
misplaced_nodes = count_misplaced_nodes(root_node)

print(misplaced_nodes)