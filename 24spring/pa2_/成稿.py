import copy
import random

class graph:
    def __init__(g, numberOfvertice):
        g.numberOfvertice = numberOfvertice
        g.adjmat = [[0] * numberOfvertice for _ in range(numberOfvertice)]

    def add_edge(g, u, v):
        g.adjmat[u][v] = 1
        g.adjmat[v][u] = 1
        
    def add_color(g, vertex, color):
        g.adjmat[vertex][vertex] = color

    def get_color(g, vertex):
        return g.adjmat[vertex][vertex]
    

def IsClique(g, curr):
    for a in range(0, len(curr)):
        for b in range(a+1, len(curr)):
            if(curr[a] == curr[b]):
                return 0
    
    for i in curr:
        for j in curr:
            if(i != j  and (g.adjmat[i][j] == 0 or g.adjmat[i][i] == g.adjmat[j][j])):
                return 0
    return 1
                

def ComputeAl(g, l, solution) -> set:
    Al = set()
    isnew = False
    for i in range(0, g.numberOfvertice):
        if(g.adjmat[l][i] != 0 and i != l):
            isnew = False
            for element in solution:
                if (g.get_color(element) == g.get_color(i)):
                    isnew = False
                    break
                isnew = True
            if(isnew):    
                Al.add(i)
    return Al

def ComputeBl(g, solution) -> set:
    copy = []
    copy = solution.copy()
    Bl = set()
    for i in range(0, g.numberOfvertice):
        Bl.add(i)
    for element in copy:
        Bl.remove(element)
    return Bl

def ComputeCl(g, l, solution, choice_set) -> set:

    Cl = ComputeAl(g,l, solution) & ComputeBl(g, solution) & choice_set

    #print('C', l, ' = ', Cl, sep='')
    return Cl


def GreedyColour(g, solution):
    #Colour = []
    k = 0
    ColourClass = []
    for i in range(g.numberOfvertice):
        if (g.adjmat[i][i] != 0):
            ColourClass.append(0)
            ColourClass[-1] = set()

    for i in range(g.numberOfvertice):
        if (g.adjmat[i][i] == 0):
            continue

        h = 0

        while(h < k and  not (ComputeAl(g, i, solution) & ColourClass[h])):
            h = h + 1
        if(h == k):
            k = k + 1
            ColourClass[h].clear()
        ColourClass[h].add(i)
        #Colour.append(h)
    return k

def GreedyBound(g, Cl, solution):
    k = GreedyColour(RestrictionGraph(g, Cl), solution)
    return len(solution) + k

def RestrictionGraph(g, Cl):
    h = graph(g.numberOfvertice)
    for element in Cl:
        h.add_color(element, g.get_color(element))
        for dest in Cl:
            if (g.adjmat[element][dest] != 0 and element != dest):
                h.add_edge(element, dest)
    return h

def PrintMatrix(g):
    for i in range(0, g.numberOfvertice):
        row = []
        for j in range(0, g.numberOfvertice):
            row.append(g.adjmat[i][j])
        print(row)
    print()





def BranchAndBound_final(g):
    global global_OptP
    global global_OptX
    MaxSize = 0

    count = 0
    AllClique = []
    Cl = set()
    for i in range(g.numberOfvertice):
        Cl.add(i)
    for i in range(0, g.numberOfvertice):
   
        solution = []
        solution.append(0)
        solution[0] = i
        choice_set = Cl.copy()
        BranchAndBound(g,1,solution, choice_set)
        #
        #PrintMatrix(g)
        #
        AllClique.append(global_OptX)

        if(global_OptP > MaxSize):
            MaxSize = global_OptP

        global_OptP = 0
        global_OptX = []

        count = count + 1

    
    print("Overall Maxsize = ", MaxSize)
    print("AllClique = ", AllClique)



def BranchAndBound(g, l, solution, choice_set):
    global global_OptP
    global global_OptX
    if(IsClique(g, solution)):
        P = len(solution)
        #
        #print(solution)
        #print(P)
        #
        if(P > global_OptP):
            global_OptP = P
            #
            #print("P=",P)
            #
            global_OptX = solution.copy()
    Cl = ComputeCl(g, solution[-1], solution, choice_set)
    
    nextchoice = []
    nextbound = []
        
    count = 0
    for x in Cl:
        nextchoice.append(0)
        nextchoice[count] = x
        ##gaile
        nextbound.append(0)
        nextbound[count] = GreedyBound(g, Cl, solution)
        ##gaile
        count = count + 1
    
    nextbound,nextchoice = Sortnext(nextbound,nextchoice)

    for i in range(0, count):

        if(nextbound[i] <= global_OptP):
            return
        BranchAndBound(g, l+1, solution + [nextchoice[i]], Cl)
    
##
def Sortnext(nextbound, nextchoice):
    for i in range(0, len(nextbound) - 1):
        for j in range(0, len(nextbound) - 1 - i):
            if (nextbound[j] < nextbound[j + 1]):
                nextbound[j], nextbound[j + 1] = nextbound[j + 1], nextbound[j]
                nextchoice[j], nextchoice[j + 1] = nextchoice[j + 1], nextchoice[j]
    
    return nextbound, nextchoice


def Random_Graph_Generator(g, density):
    h = graph(g.numberOfvertice)

    for i in range(g.numberOfvertice - 2):
        for j in range(i + 1, g.numberOfvertice - 1):
            r = random.uniform(0, 1)
            if (r >= 1 - density):
                h.add_edge(i - 1, j - 1)
    

    for i in range(g.numberOfvertice):
        r = random.randint(1, g.numberOfvertice / 2)
        h.adjmat[i][i] = r
    

    return h

global_OptP = 0
global_OptX = []


#BranchAndBound_final(g1)
g2 = graph(50)
g2 = Random_Graph_Generator(g2, 0.5)
BranchAndBound_final(g2)