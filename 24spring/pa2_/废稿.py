import copy
import random

class graph:
    def __init__(g, numberOfvertice):
        g.numberOfvertice = numberOfvertice
        g.adjmat = []
    

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
                

def ComputeAl(g, l) -> set:
    Al = set()
    for i in range(0, g.numberOfvertice):
        if(g.adjmat[l][i] != 0 and i != l):
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

    Cl = ComputeAl(g,l) & ComputeBl(g, solution) & choice_set

    #print('C', l, ' = ', Cl, sep='')
    return Cl


def GreedyColour(g):
    Colour = []
    ColourClass = dict()
    for i in range(g.numberOfvertice):
        ColourClass[i] = set()
    k = 0
    for i in range(0, g.numberOfvertice):
        h = 0
        while(h < k and (ComputeAl(g, i) & ColourClass[h]) != {}):
            h = h + 1
        if(h == k):
            k = k + 1
            ColourClass[h].clear()
        ColourClass[h].add(i)
        Colour.append(h)
    return k

def GreedyBound(g, l):
    t = GreedyColour(RestrictionGraph(g, ComputeCl(g, l)))
    return l + t

def RestrictionGraph(g, Cl):
    h = graph(g.numberOfvertice)
    h.adjmat = g.adjmat.copy()
    for i in range(0, g.numberOfvertice):
        if i not in Cl:
            for j in range(0, g.numberOfvertice):
                h.adjmat[i][j] = 0
                h.adjmat[j][i] = 0
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
    MaxClique = []
    MaxCount = 0            ##This is the number of rotate in which situation has the max clique
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
        done = False
        BranchAndBound(g,0,solution, choice_set)
        print(solution)
        #
        #PrintMatrix(g)
        #
        AllClique.append(global_OptX)

        if(global_OptP > MaxSize):
            MaxSize = global_OptP
            MaxClique = global_OptX
            MaxCount = count
        global_OptP = 0
        global_OptX = []
        #print("MaxSize = ", MaxSize)
        #print("MaxClique = ", MaxClique)
        count = count + 1
        #g = MatrixEqualChange(g)

    
    print("Overall Maxsize = ", MaxSize)
    print("AllClique = ", AllClique)

    currClique = []
    MaxCliqueList = []
    
    for j in range(0, g.numberOfvertice):
        currClique = CliqueRotate(g, AllClique[j], j)
        if(len(currClique) == MaxSize and not currClique in MaxCliqueList):
            MaxCliqueList.append(currClique)

    print("MaxCliqueList is ", MaxCliqueList)
    '''
    print()
    print("Overall Maxsize = ", MaxSize)
    print("Overall MaxCount = ", MaxCount)
    print("Overall Maxclique = ", MaxClique)

    MaxClique = CliqueRotate(MaxClique)
    print("The original Maxclique = ", MaxClique)
    print("AllClique = ", AllClique)
    '''
    
def CliqueRotate(g, CurrClique, j):
    for i in range(0, len(CurrClique)):
        if(CurrClique[i] > j):
            CurrClique[i] = CurrClique[i] - j
        else:
            CurrClique[i] = CurrClique[i] - j + g.numberOfvertice
    CurrClique.sort()
    return CurrClique
#
def MatrixEqualChange(g):
    n = g.numberOfvertice
    trans = g.adjmat[0][0]
    #diagonal OK
    for i in range(1,n):
        g.adjmat[i-1][i-1]= g.adjmat[i][i]
        #PrintMatrix(g)
    g.adjmat[n-1][n-1] = trans
    PrintMatrix(g)

    transition = []
    for i in range(n-2, -1, -1):
        transition.append(g.adjmat[i][n-1])
    #print("transition = ", transition)
    #print()
    
    #Mainpart OK
    for i in range(n-2, 0, -1):
        for j in range(i-1, -1, -1):
            g.adjmat[j+1][i+1] = g.adjmat[j][i]
            #print("StartDown")
            #PrintMatrix(g)
    
    #PrintMatrix(g)
    #UpperPart OK
    for i in range(1, n):
        g.adjmat[0][i] = transition.pop()
    
    #PrintMatrix(g)

    #LowerPart OK
    for i in range(0, n):
        for j in range(0, n):
            if(i > j):
                g.adjmat[i][j] = g.adjmat[j][i]
                #PrintMatrix(g)
    #PrintMatrix(g)
    return g
#

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
    if (not Cl):
        return
    
    nextbound = [0 for v in range(g.numberOfvertice)]
    nextchoice = [0 for v in range(g.numberOfvertice)]
        
    count = 0
    for x in Cl:
        nextchoice[count] = x
        ##gaile
        nextbound[count] = 6
        ##gaile
        count = count + 1
    #nextbound,nextchoice = Sortnext(nextbound,nextchoice)

    for i in range(0, count):
        

            
        
        #print("zaizheli")
        if(nextbound[i] <= global_OptP):
            return
        solution.append(0)
        solution[-1] = nextchoice[i]
        BranchAndBound(g, l+1, solution, Cl)
        if (len(solution) >= global_OptP):
            return
    

def Sortnext(nextbound, nextchoice):
    for i in range(0, len(nextbound) - 1):
        for j in range(0, len(nextbound) - 1 - i):
            if (nextbound[j] < nextbound[j + 1]):
                nextbound[j], nextbound[j + 1] = nextbound[j + 1], nextbound[j]
                nextchoice[j], nextchoice[j + 1] = nextchoice[j + 1], nextchoice[j]
    
    return nextbound, nextchoice
                

global_OptP = 0
global_OptX = []
g1 = graph(6)
g2 = graph(4)
g1.adjmat = [[1, 1, 0, 1, 0, 0], 
             [1, 2, 0, 1, 0, 0], 
             [0, 0, 3, 1, 1, 1], 
             [1, 1, 1, 4, 1, 1], 
             [0, 0, 1, 1, 5, 1], 
             [0, 0, 1, 1, 1, 6]]
'''
g2.adjmat = [[1, 2, 3, 4],
             [2, 5, 6, 7],
             [3, 6, 8, 9],
             [4, 7, 9,10]]
MatrixEqualChange(g2)
'''
BranchAndBound_final(g1)

#print(IsClique(g1,[2,3,4,5]))
##ComputeCl(g1, 4)