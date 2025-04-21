from math import inf, isinf
from tsp_general import distance, isinf

def tsp_bounding(graph, path=[0], shortest=inf, bound=distance):
    """
    Backtracking solution to the TSP with prunning using {bound}
    """
    size     = len(graph)
    result   = path if iscycle(path, graph) else []

    for target in (set(range(size))-set(path)):
        
        # prune according to bound

        tour, cost = [], inf

        if bound(path+[target], graph) < shortest:
            
            tour  = tsp_bounding(graph, path+[target], shortest)
            cost  = distance(tour, graph)

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