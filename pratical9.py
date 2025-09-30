class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children or []

def minimax(node, depth, player):
    if depth == 0 or not node.children:
        return node.value
    
    if player == "MAX":
        best_value = float('-inf')
        for child in node.children:
            val = minimax(child, depth - 1, "MIN")
            best_value = max(best_value, val)
        return best_value
    else:
        best_value = float('inf')
        for child in node.children:
            val = minimax(child, depth - 1, "MAX")
            best_value = min(best_value, val)
        return best_value

# Example tree:
#          MAX
#       /       \
#     MIN       MIN
#    /  \      /   \
#   3    5    2     9

# Leaf nodes
leaf1 = Node(3)
leaf2 = Node(5)
leaf3 = Node(2)
leaf4 = Node(9)

# MIN nodes
min1 = Node(children=[leaf1, leaf2])
min2 = Node(children=[leaf3, leaf4])

# MAX root
root = Node(children=[min1, min2])

result = minimax(root, depth=3, player="MAX")
print("Minimax result:", result)

