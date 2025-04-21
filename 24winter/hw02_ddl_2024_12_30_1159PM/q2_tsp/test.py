from math import inf

def distance(path, graph):
    """
    The distance of {path} in {graph}
    """

    size = len(graph)
    length = len(path)

    result = 0 if length < size else graph[path[-1]][0]

    for i in range(length-1):
        result += graph[path[i]][path[i+1]]

    return result

def check_undirected(graph: list):
    """
    Checks if a given graph is undirected.
    """
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != graph[j][i]:
                return False
    return True

def satisfies_triangle_inequality(graph):
    """
    Checks if the given graph satisfies the triangle inequality.
    """
    n = len(graph)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:  # Ensure three distinct nodes
                    if graph[i][j] == inf or graph[j][k] == inf or graph[i][k] == inf:
                        continue  # Skip unreachable paths
                    if graph[i][k] > graph[i][j] + graph[j][k]:  # Check inequality
                        return False
    return True

def min_spanning_tree(graph: list) -> list:
    """
    Constructs a minimum spanning tree (MST) of the given graph using a greedy algorithm.
    """
    if not check_undirected(graph):
        raise ValueError("The input graph is not undirected!")

    n = len(graph)
    result = [[inf for _ in range(n)] for _ in range(n)]  # Initialize MST matrix
    T = [0]  # Start from the first node (arbitrarily chosen)

    # Iterate until all nodes are included in the MST
    while set(T) != set(range(n)):
        i, j = -1, -1
        min_weight = inf
        # Find the minimum weight edge connecting the MST set (T) to the remaining nodes
        for s in T:
            for t in (set(range(n)) - set(T)):
                if graph[s][t] < min_weight:
                    min_weight = graph[s][t]
                    i, j = s, t
        # Add the edge to the MST
        result[i][j], result[j][i] = graph[i][j], graph[j][i]
        T.append(j)  # Add the new node to the MST set

    return result

def depth_first_search(tree: list, path=[0]):
    """
    Performs a depth-first traversal on the given tree.
    """
    n = len(tree)
    result = path
    s = path[-1]  # Current node

    # Explore all unvisited neighbors of the current node
    for t in (set(range(n)) - set(path)):
        if t not in path and tree[s][t] != float('inf'):  # Check if edge exists
            result.append(t)
            result = depth_first_search(tree, result)
    
    return result

def remove_duplicate_nodes(path):
    """
    Removes duplicate nodes from a given path while maintaining the order.
    """
    tsp_path, seen = [], []  # Initialize the resulting path and a list to track seen nodes

    for node in path:
        # If the node hasn't been seen before, add it to the result and mark it as seen
        if node not in seen:
            tsp_path.append(node)
            seen.append(node)
    
    return tsp_path

def tsp_approximation(graph: list):
    """
    Approximates a solution to the Traveling Salesman Problem (TSP) using a minimum spanning tree (MST).
    """
    if not satisfies_triangle_inequality(graph):
        raise ValueError("The input matrix does not satisfy the triangle inequality!")

    # 1. Construct the minimum spanning tree
    tree = min_spanning_tree(graph)

    # 2. Perform a depth-first traversal
    traversal_path = depth_first_search(tree)

    # 3. Remove duplicate nodes to create a valid TSP path
    tsp_path = remove_duplicate_nodes(traversal_path)

    return tsp_path

g=[
    [inf, 4, inf, 3, 9, 16],
    [4, inf, 14, 4, 13, 18],
    [inf, 14, inf, 17, 7, 6],
    [3, 4, 17, inf, 12, 17],
    [9, 13, 7, 12, inf, inf],
    [16, 18, 6, 17, inf, inf],
]

r = tsp_approximation(g)
d = distance(r, g)

print(r)
print(d)