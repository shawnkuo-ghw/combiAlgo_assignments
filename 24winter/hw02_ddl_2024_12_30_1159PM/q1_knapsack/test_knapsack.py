import sys
import time
import random
import matplotlib.pyplot as plt
from numpy import dot
from knapsack_compare       import *
from knapsack_test_tools    import *
from knapsack_general       import *
from knapsack_bounding      import *
from knapsack_brandAndBound import *


def main():
    
    # ----------------------
    # 1. Generate test cases
    # ----------------------

    if len(sys.argv) != 8:
        print('Usage: python test_knapsack <Num> <Init> <Step> <minRate> <maxRate> <minWeight> <maxWeight>')
        print(
            f'<Num>:       number of test cases',
            f'<Init>:      inital number of nodes number',
            f'<Step>:      step of item number is increased each time',
            f'<minRate>:   minimum rate of vi / (2 * wi) ',
            f'<maxRate>:   maximum rate of vi / (2 * wi)',
            f'<minWeight>: minimum of item weight',
            f'<maxWeight>: maximum of item weight',
            sep = '\n'
        )
        return
    
    fname     = 'knapsack_test_cases'
    num       = int(sys.argv[1])    # the number of test cases to generate
    init      = int(sys.argv[2])    # the initial value of test size
    step      = int(sys.argv[3])    # the step test size is increased each loop
    minRate   = float(sys.argv[4])  # minimum rate of vi / (2 * wi)
    maxRate   = float(sys.argv[5])  # maximum rate of vi / (2 * wi)
    minWeight = int(sys.argv[6])    # minimum of item weight
    maxWeight = int(sys.argv[7])    # maximum of item weight
    knapsack_generate_test_cases( fname, num, init, step, minRate, maxRate, minWeight, maxWeight )
    
    # ----------------------------------------------------------------------------
    # 2. Run tests with different backtracking algorithms, check their correctness
    #    and compare their running times.
    # ----------------------------------------------------------------------------
    algos = [
        knapsack_general,
        knapsack_bounding,
        knapsack_branchAndBound
    ]

    algoNames = [
        'Backtracking-General',
        'Backtracking-Bounding',
        'Backtracking-BranchAndBound'
    ]
    compare_knapsack_algos( fname, algos, algoNames, True )


if __name__ == '__main__':
    main()