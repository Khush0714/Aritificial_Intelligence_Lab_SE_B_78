import math

# Sample game tree represented as an adjacency list with heuristic values at leaves
# For simplicity, leaves have values, internal nodes are represented by lists of children
game_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': 3,
    'E': 5,
    'F': 6,
    'G': 9
}

# Count nodes evaluated (for comparison)
nodes_evaluated = 0

def heuristic_value(node):
    # If node is a leaf (int), return the value directly
    if isinstance(node, int):
        return node
    else:
        raise ValueError("Heuristic value requested for non-leaf node")

def alpha_beta(node, depth, alpha, beta, maximizingPlayer):
    global nodes_evaluated
    # If node is leaf or depth = 0, return heuristic value
    if isinstance(node, int) or depth == 0:
        nodes_evaluated += 1
        return heuristic_value(node) if isinstance(node, int) else 0
    
    if maximizingPlayer:
        value = -math.inf
        for child_key in node:
            child = game_tree[child_key] if isinstance(child_key, str) else child_key
            value = max(value, alpha_beta(child, depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break  # Beta cut-off
        return value
    else:
        value = math.inf
        for child_key in node:
            child = game_tree[child_key] if isinstance(child_key, str) else child_key
            value = min(value, alpha_beta(child, depth-1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break  # Alpha cut-off
        return value

# Driver code
nodes_evaluated = 0
root = game_tree['A']
optimal_value = alpha_beta(root, depth=3, alpha=-math.inf, beta=math.inf, maximizingPlayer=True)

print(f"Optimal value (with Alpha-Beta Pruning): {optimal_value}")
print(f"Nodes evaluated: {nodes_evaluated}")

