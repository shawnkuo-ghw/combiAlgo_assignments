import sys
import time
import random
import matplotlib.pyplot as plt
from numpy import dot
from tsp_general        import *
from tsp_bounding       import *
from tsp_branchAndBound import *
from tsp_compare        import *
from tsp_test_cases     import *

def main():

    '''
    1. Generate test cases
    '''
    if len(sys.argv) != 4:
        print('Usage: python test_tsp <Num> <Init> <Step>.')
        print(
            f'<Num>:  the number of test cases\n',
            f'<Init>: the inital number of nodes number\n',
            f'<Step>: the step nodes number is increased each loop\n',
            sep = ''
        )
        return
    testFile = 'knapsack_test_cases'
    num  = int(sys.argv[1])  # the number of test cases to generate
    init = int(sys.argv[2])  # the initial value of test size
    step = int(sys.argv[3])  # the step test size is increased each loop
    maxDist = 20             # maximum value of edge distance
    conRate = 0.83           # possibility rate of the connection between two nodes
    tsp_generate_test_cases(testFile, num, init, step, maxDist, conRate)
    
    '''
    2. Run tests with different backtracking algorithms, check their correctness
       and compare their running times.
    '''

    algos = [
        tsp_general,
        tsp_bounding,
        tsp_branchAndBound,
        # tsp_approximation
    ]

    algoNames = [
        'TSP-General',
        'TSP-Bounding',
        'TSP-Brand-and-Bound',
        # 'TSP-Approximation'
    ]

    compare_tsp_algos( testFile, algos, algoNames, True )

if __name__ == '__main__':
    main()