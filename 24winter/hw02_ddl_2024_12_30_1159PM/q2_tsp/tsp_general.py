from math import inf, isinf

def tsp_general(graph, path=[0], shortest=inf):
    """
    The backtracking implementation of the TSP
    """
    size     = len(graph)
    
    result   = path if iscycle(path, graph) else []

    targets  = []

    for target in (set(range(size))-set(path)):
        # calculate choice set
        if distance(path+[target], graph) < shortest:

            targets += [target]
    
    for target in targets:
        # recursive step
        tour = tsp_general(graph, path+[target], shortest)
        cost = distance(tour, graph)

        if tour and cost < shortest:
            # update current best
            shortest = cost
            result   = tour

    return result


def distance(path, graph):
    """
    The distance of {path} in {graph}
    """

    size   = len(graph)
    length = len(path)

    result = 0 if length < size else graph[path[-1]][0]

    for i in range(length-1):
        result += graph[path[i]][path[i+1]]

    return result

def iscycle(path, graph):
    """
    Is {path} a Hamiltonian cycle in {graph}?
    """

    size   = len(graph)
    result = set(path) == set(range(size)) # is it a permutation?

    if result:

        result = path[0] == 0 # does it start at 0?
        
        for i in range(size):

            if not result:
                break

            result = not isinf(graph[path[i]][path[(i+1)%size]]) # is there an edge?

    return result

def mincost(path, graph):
    """
    The MinCostBound function (see Stinson Th 4.2 pp 129--131)
    """

    size   = len(graph)
    result = distance(path, graph)

    if len(path) != size:

        for i in (set(range(size))-set(path[:-1])):

            result += min(graph[i])

    return result
