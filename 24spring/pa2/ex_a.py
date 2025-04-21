
class graph:
    def __init__(g, numberOfvertice):
        g.numberOfvertice = numberOfvertice
        g.adjmat = []

G = graph(6)
G.adjmat = [[1, 1, 0, 1, 0, 0], 
            [1, 2, 0, 1, 0, 0], 
            [0, 0, 3, 1, 1, 0], 
            [1, 1, 1, 4, 1, 0], 
            [0, 0, 1, 1, 5, 0], 
            [0, 0, 0, 0, 1, 6]]

global_COLORING        = dict()
global_COLORCLASS      = dict()
global_neighbours_list = dict()


def Neighbour_Init(G: graph, neighbours: dict) -> None:
    N = G.numberOfvertice
    for i in range(N):
        for j in range(N):
            if i != j and G.adjmat[i][j] == 1:
                if i not in neighbours:
                    neighbours[i] = [j]
                else:
                    neighbours[i].append(j)

Neighbour_Init(G, global_neighbours_list)



def GREEDYCOLORING(graph: list) -> int:
    k = 0
    for i in range(0, n):
        h = 0


    return 0

