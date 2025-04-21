from knapsack_general       import *
from knapsack_bounding      import *
from knapsack_brandAndBound import *
import random

def knapsack_generate_test_cases(
        fname: str, 
        num: int,
        init: int, 
        step: int, 
        minRate: float, 
        maxRate: float, 
        minWeight: int,
        maxWeight: int 
    ) -> None:
    '''
    Generate test cases for 01-knapsack problem in file {fname}.
    
    Arguments:
        - fname:     the name of file that stores all the test cases
        - num:       the number of test cases to generate
        - init:      the initial value of nodes number
        - step:      the step test size is increased each loop
        - minRate:   minimum rate of vi / (2 * wi)
        - maxRate:   maximum rate of vi / (2 * wi)
        - minWeight: minimum of item weight
        - maxWeight: maximum of item weight
    '''
    
    file = open(fname, 'w')

    size  = init    # the size of test case
    count = 0

    while count < num:

        values   = [] # values of items
        weights  = [] # weights of items
        capacity = 0  # capacity of test case

        # 1. Generate weights of items
        for i in range(size):
            weight = random.randint(minWeight, maxWeight)
            weights.append(weight)
        
        # 2. Generate values of items
        for i in range(size):
            minValue = int(2 * weights[i] * minRate)
            maxValue = int(2 * weights[i] * maxRate)
            value = random.randint(minValue, maxValue)
            values.append(value)
        
        # 3. Generate capacity
        weight_sum = 0
        for weight in weights:
            weight_sum += weight
        capacity = weight_sum // 2

        # 4. Generate solution
        solution = knapsack_general(values, weights, capacity)

        # 5. Generate a test case
        case = ''
        case += str(capacity)                + '#'
        case += ' '.join(map(str, values))   + '#'
        case += ' '.join(map(str, weights))  + '#'
        case += ' '.join(map(str, solution))

        if count < num - 1: case += '\n'

        # print(case, end='')
        file.write(case)        

        count += 1
        size += step

    file.close()



def knapsack_run_test_cases( fname: str, algo ) -> None:
    '''
    Run all the test cases in file {fname} with the algorithm to test {algo}.

    Arguments:
        - fanme: the name of the file that stores all the test cases
        - algo:  the algorithm that we are going to test with
    '''

    count = 0
    tests = build_tests(fname)

    for test in tests:

        W, v, w, expectedSol = test

        '''
        W: knapsack capcity
        v: item values
        w: item weights
        expectedSol: solution
        '''

        ourSol = algo(v, w, W)
        
        expectedProfit = dot( v, expectedSol )
        ourProfit      = dot( v, ourSol) 

        flag = True if expectedSol == ourSol or expectedProfit == ourProfit else False

        print(
            f'Test No:  {count+1:02d}',
            f'items:    {len(v):02d}',
            f'knapsack( {v}, {w}, {W} ) = {ourSol}',
            f'solution: {expectedSol}',
            f'result:   {flag}',
            sep = '\n',
            end = '\n\n'
        )

        count += 1 


def build_tests(fname: list) -> list:
    '''
    Return a list consisting of all test cases in file {fname}.
    '''

    file  = open(fname, "r")
    lines = file.read().split("\n")
    file.close()

    tests = []

    for line in lines:

        test = line.split("#")

        W = int(test[0])                    # capacity of knapsack
        v = list(map(int, test[1].split())) # values of items
        w = list(map(int, test[2].split())) # weights of items
        s = list(map(int, test[3].split())) # solution of test case

        assert len(v) == len(w) and len(w) == len(s)

        tests += [(W,v,w,s)]
    
    return tests