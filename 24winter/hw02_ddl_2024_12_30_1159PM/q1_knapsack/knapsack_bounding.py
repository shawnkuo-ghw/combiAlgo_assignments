from numpy import dot

def knapsack_bounding(values: list, weights: list, capacity: int) -> list:
    '''
    The backtracking algorithms solving 01-knapsack problem that makes the 
    use of the fractional knapsack as a bounding function.

    Argumetns:
        - values:   the list of values of items
        - weights:  the list of weights of items
        - capacity: the capacity of knapsack
    Return:
        - optX:     the optimal solution
    '''

    # global variable

    optP = 0        # optimal profit   of 01-knapsack problem
    optX = []       # optimal solution of 01-knapsack problem
    N = len(values) # number of items

    # recursive part

    def knapsack_bounding_recursive( currX: list = [] ) -> None:
        '''
        The recursive part of knapsack_fkBound.

        Argumetns:
            - currX:   current solution
        '''
        nonlocal optP, optX, N
        currl = len(currX)
        currX_ = currX + [0] * (N - currl)
        currW = dot(weights, currX_) # current weight of current solution {currX}
        currP = dot(values, currX_)  # current profit of current solution {currX} 

        '''
        Step 1: Check feasibility of current solution {currX}
        '''    
        if len(currX) == N:

            # Check whether current solution {currX} is better

            if currW <= capacity and currP > optP:

                optP = currP
                optX = currX[:]

        else:
            
            '''
            Step 2: Calculate the bound of the current solution {currX}, do boundingly pruning
            '''
            bound = getBound( values, weights, capacity, currX, fractional ) # bound for the profit of currX
            if bound <= optP: return # boundingly pruning

            '''
            Step 3: Construct the choice set for current solutiuon {currX}, do pruning
            '''
            if currW + weights[currl] <= capacity:
                choS = [0, 1]
            else:
                choS = [0]

            '''
            Step 4: For each possible next solution, call the algorithm recursively
            '''
            for x in choS:
                
                knapsack_bounding_recursive( currX + [x] )

    knapsack_bounding_recursive( [] )

    return optX

def getBound(values: list, weights: list, capacity: int, currX: list, algo) -> float:
    '''
    Calculate the bound of profit of current solution {currX}.

    Arguments:
        - values:   list of item values
        - weights:  list of item weights
        - capacity: capacity of knapsack
        - currX:    current solution
        - algo:     algorithnm used to calculate the bound
    Return:
        - currP + optP_rX: the bound of the profit for currX
    '''
    N = len(values)
    currl = len(currX)
    currX_ = currX + [0] * (N - currl)
    currP = dot(values, currX_)  # current profit of current solution {currX} 
    currW = dot(weights, currX_) # current weight of current solution {currX}
    opt_rX = [] if N == currl else fractional( values[currl:], weights[currl:], capacity - currW )
    optP_rX = 0 if N == currl else dot( values[currl:], opt_rX )
    return currP + optP_rX


def fractional(v, w, W) -> list:
    """
    the fractional knapsack

    Arguments:
        - v: the list of values
        - w: the list of weights
        - W: the capacity  
    
    Return:
        - x: optimal fractional solution
    """

    s, v, w = sort(v, w)

    x, c, i = [0]*len(v), W, 0

    while 0 < c and i < len(v):

        x[i] = 1 if w[i] <= c else c/w[i]
        c   -= w[i] * x[i]
        i   += 1

    x = restore(s, x)

    return x

def sort(v, w):
    """
    sort the vectors of values and weights
    by value/weight ratio in decreasing order
    """
    
    z = list(zip(range(len(v)),zip(v, w)))

    z.sort(key=lambda k: (k[1][0]/k[1][1]), reverse=True)

    s, z = zip(*z)

    return s, *map(list,zip(*z))

def restore(s, x):
    """
    in conjunction with sort restores the
    solution x its original order of elements
    """

    z = list(zip(s, x))

    z.sort()

    z, r = map(list,zip(*z))

    return r