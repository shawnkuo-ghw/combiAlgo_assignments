from numpy import dot
from knapsack_bounding import getBound, fractional

def knapsack_branchAndBound(values: list, weights: list, capacity: int) -> list:
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

    def knapsack_branchAndBound_recursive( currX: list = [] ) -> None:
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
            Step 2: Construct the choice set for current solutiuon {currX}
            '''
            if currW + weights[currl] <= capacity: # simple pruning
                choS = [0, 1]            
            else:
                choS = [0]

            '''
            Step 3: Find the next solution with higher possible value (greedy strategy)
            '''
            nextChoices = []
            nextBounds  = []

            for i in range( len(choS) ):

                nextChoices.append( currX[:] + [choS[i]] )
                nextBound = getBound( values, weights, capacity, currX + [choS[i]], fractional)
                nextBounds.append( nextBound )

            # Sort nextChoices and nextBounds so that nextBounds is in decreasing order.
            if len(choS) == 2 and nextBounds[0] < nextBounds[1]:
                
                nextBounds[0],  nextBounds[1]  = nextBounds[1],  nextBounds[0]
                nextChoices[0], nextChoices[1] = nextChoices[1][:], nextChoices[0][:]

            if nextBounds[0] <= optP: return

            '''
            Step 4: For each possible next solution, call the algorithm recursively
            '''
            for i in range( len(nextChoices) ):
                
                knapsack_branchAndBound_recursive( nextChoices[i] )

    knapsack_branchAndBound_recursive( [] )

    return optX