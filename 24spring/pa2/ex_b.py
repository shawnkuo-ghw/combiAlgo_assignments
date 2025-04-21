import copy
import random

class graph:
    def __init__(g, numberOfvertice):
        g.numberOfvertice = numberOfvertice
        g.adjmat = []

    
def neighbor(g: graph, solution: list):
    copy_solution = []
    copy_solution = copy.copy(solution)
    origin = copy_solution[-1]
    isnew = False
    for i in range(0, g.numberOfvertice):
        if (i != origin and g.adjmat[origin][i] != 0):
            for element in copy_solution:
                if (element == i):
                    isnew = False
                    break
                if (g.adjmat[element][i] == 0):
                    isnew = False
                    break
                if (g.adjmat[element][element] == g.adjmat[i][i]):
                    isnew = False
                    break
                isnew = True
        
        if (isnew):
            solution.append(i)
            break 
    return solution


def hill_climbing_search(g, vertex):
    solution = []
    solution.append(vertex)
    searching = True

    while (searching):
        current = len(solution)
        solution = neighbor(g, solution)
        if (len(solution) == current):
            searching = False

    return solution

def MCP_HC(g):
    solution = []
    vertice = []

    for i in range(0, g.numberOfvertice):
        vertice.append(i)
    
    random.shuffle(vertice)
    vertex = vertice[0]
    solution = hill_climbing_search(g, vertex)
    min = len(solution)
    max = len(solution)
    avg = 0
    optimal = 3
    Nopt = 0
    for element in vertice:
        solution = hill_climbing_search(g, element)
        if (len(solution) < min):
            min = len(solution)
        if (len(solution) > max):
            max = len(solution)
        if (len(solution) != optimal):
            Nopt += 1
        avg = avg + len(solution)
        print(solution)

    avg = avg / len(vertice)

    print('min = ' + str(min) + ', max = ' + str(max) + ', avg = ' + str(avg) + ', Nopt = ' + str(Nopt) + ' when = ' + str(len(vertice)))


    return

g1 = graph(6)
g1.adjmat = [[1, 1, 0, 1, 0, 0], 
             [1, 2, 0, 1, 0, 0], 
             [0, 0, 3, 1, 1, 0], 
             [1, 1, 1, 4, 1, 0], 
             [0, 0, 1, 1, 5, 0], 
             [0, 0, 0, 0, 1, 6]]
MCP_HC(g1)
