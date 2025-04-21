from math import inf
from tsp_general import mincost, iscycle, distance

def tsp_branchAndBound(graph: list, path=[0], shortest=inf, bound=mincost) -> list:
    """
    Solve TSP using backtracking with branch and bound.
    """
    size = len(graph)
    result = path if iscycle(path, graph) else []  # If path is a valid cycle, return it

    tries = []  # List to store possible next nodes

    # Add all feasible targets to tries
    for target in (set(range(size)) - set(path)):

        if bound(path + [target], graph) < shortest:
            tries.append(target)

    sort_tries(graph, tries, path)  # Sort tries (no return value used here)

    # Explore each try recursively
    for i in range(len(tries)):

        tour, cost = [], inf

        if bound(path + [tries[i]], graph) < shortest:
            tour = tsp_branchAndBound(graph, path + [tries[i]], shortest)
            cost = distance(tour, graph)

            if tour and cost < shortest:  # Update shortest tour if a better one is found
                shortest = cost
                result = tour

    return result


def sort_tries(graph, tries, path, bound=mincost):
    """
    Sort possible next nodes based on estimated cost.
    """
    return sorted(tries, key=lambda x: bound(path + [x], graph))