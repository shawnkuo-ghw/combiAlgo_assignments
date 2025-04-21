import time
import matplotlib.pyplot as plt
from numpy import dot
from knapsack_test_tools import *

def compare_knapsack_algos( fname: str, algos: list, names: list, if_plt: bool) -> None:

    count = 0
    tests = build_tests( fname )
    item_numbers  = [] 
    running_times = []    

    for test in tests:

        capacity, values, weights, sol_expected = test
        
        print('\n\n')
        print('----------------------- ' + f'Test No.{count+1}' + ' -----------------------\n')
        print(
            f'Items:    {len(values):02d}',
            f'Capacity: {capacity}',
            f'Values:   {values}',
            f'Weights:  {weights}',
            f'Solution: {sol_expected}\n',
            sep = '\n'
        )

        item_numbers.append( len(values) )
        item_running_times = []

        for i in range(len(algos)):
            
            startT    = time.process_time()
            sol_algo  = algos[i](values, weights, capacity)
            endT      = time.process_time()
            elapT     = endT - startT
            
            item_running_times.append( elapT )

            optP_expected = dot(values, sol_expected)
            optP_algo     = dot(values, sol_algo)
            correctness   = True if optP_expected == optP_algo else False

            print(
                f'algorithm:    {names[i]}',
                f'runningtime:  {elapT:.10f}',
                f'correctness:  {correctness}',
                f'knapsack({values},{weights},{capacity}) = {sol_algo}',
                sep = '\n',
                end = '\n\n'
            )
        
        running_times.append( item_running_times )

        count += 1

    # Plotting the results

    if if_plt:
        
        running_times = list(zip(*running_times))  # Transpose for easier plotting
        plt.figure(figsize=(10, 6))
        for i in range(len(algos)):
            plt.plot(item_numbers, running_times[i], label=names[i], marker='o')
        plt.title('Running Time Comparison of Knapsack Algorithms')
        plt.xlabel('Number of Items')
        plt.ylabel('Running Time (seconds)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()