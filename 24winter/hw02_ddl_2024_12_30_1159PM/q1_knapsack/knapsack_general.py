from numpy import dot

def knapsack_general(values: list, weights: list, capacity: int) -> list:
    '''
    The general backtracking algorithms solving 01-knapsack problem.
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

    def knapsack_general_recursive( curX: list = [] ) -> None:
        '''
        The recursive part of general backtracking algorithms solving 01-knapsack problem.
        Argumetns:
            - curX:   current solution
        '''

        nonlocal optP, optX, N

        # 1. Check feasibility of current solution {curX}
    
        if len(curX) == N:
        
            currW = dot(weights, curX) # current weight of current solution {curX}
            currP = dot(values, curX)  # current profit of current solution {curX} 

        # 2. Check whether current solution {curX} is better

            if currW <= capacity and currP > optP:

                optP = currP
                optX = curX[:]
                        
        # 3. Recursive call
        
        else:

            knapsack_general_recursive( curX + [1] )
            knapsack_general_recursive( curX + [0] ) 

    knapsack_general_recursive( [] )

    return optX


def knapsack_pruning(values: list, weights: list, capacity: int) -> list:
    '''
    A backtracking algorithms solving 01-knapsack problem with
    a simple pruning method.

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

    def knapsack_pruning_recursive( currX: list = [] ) -> None:
        '''
        The recursive part of knapsack_pruning.

        Argumetns:
            - currX:   current solution
        '''
        nonlocal optP, optX, N
        currl = len(currX)
        currX_ = currX + [0] * (N - currl)
        currW = dot(weights, currX_) # current weight of current solution {currX}

        '''
        Step 1: Check feasibility of current solution {currX}
        '''    
        if len(currX) == N:
        
            currP = dot(values, currX)  # current profit of current solution {currX} 

            # Check whether current solution {currX} is better

            if currW <= capacity and currP > optP:

                optP = currP
                optX = currX[:]

        else:
            '''
            Step 2: Construct the choice set for current solutiuon {currX}, do pruning
            '''
            if currW + weights[currl] <= capacity:
                choS = [0, 1]
            else:
                choS = [0]

            '''
            Step 3: For each possible next solution, call the algorithm recursively
            '''
            for x in choS:
                knapsack_pruning_recursive( currX + [x] )

    knapsack_pruning_recursive( [] )

    return optX


def main():
    Capacity = 5
    Weights  = [4, 3, 7]
    Values   = [1, 2, 3]
    Solution = [0, 1, 0]

    optX = knapsack_general( Values, Weights, Capacity )

    if optX == Solution:
        print("True")
    else:
        print("False")

if __name__ == '__main__':
    main()
